import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time


Api_key =  	'tKGxgNTsijsk'
pt = 'tBt5a0w5VLbO'
rt = 'twarZhT7UbEB'





class Data:
	def __init__(self,api_key,project_token):
		self.api_key=Api_key
		self.project_token=pt
		self.params = {
			'api_key':self.api_key
		}
		self.get_data()
	def get_data(self):
		response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		self.data = json.loads(response.text)

	def get_total_cases(self):
		data = self.data['total']

		for content in data:
			if content['name']=='Coronavirus Cases:':
				return content['value']

		return 'Data is outdated'

	def get_total_deaths(self):
		data = self.data['total']

		for content in data:
			if content['name']=='Deaths:':
				return content['value']

		return 'Data is outdated'

	def get_total_recovered(self):
		data = self.data['total']

		for content in data:
			if content['name']=='Recovered':
				return content['value']

		return 'Data is outdated'

	def get_country_data(self,country):
		data = self.data['country']
		
		for content in data:
			if content['name'].lower() == country.lower():
				return content

		return 'Data is not updated'		

	def get_list_of_countries(self):
		countries = []
		for country in self.data['country']:
			countries.append(country['name'].lower())

		return countries


	def update_data(self):
			response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run', params=self.params)

			def poll():
				time.sleep(0.1)
				old_data = self.data
				while True:
					new_data = self.get_data()
					if new_data != old_data:
						self.data = new_data
						print("Data updated")
						speak("Data updated")
						break
					time.sleep(5)


			t = threading.Thread(target=poll)
			t.start()




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)


def get_audio():

    #It takes input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listening')
        r.phrase_time_limit=1
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-uk')
        print(f'Aaryan said: {said}\n')
    except: 
        return "None"
    return said.lower()



def main():
	print("Program started")
	data = Data(Api_key,pt)
	END_PHRASE = "stop"
	country_list = data.get_list_of_countries()

	TOTAL_PATTERNS = {
					re.compile("[\w\s]+ total [\w\s]+ cases"):data.get_total_cases,
					re.compile("[\w\s]+ total cases"): data.get_total_cases,
                    re.compile("[\w\s]+ total [\w\s]+ deaths"): data.get_total_deaths,
                    re.compile("[\w\s]+ total deaths"): data.get_total_deaths,
                    re.compile("[\w\s]+ recovered"): data.get_total_recovered

					}

	COUNTRY_PATTERNS = {
					re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_country_data(country)['total_cases'],
                    re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_country_data(country)['total_deaths'],
					re.compile("[\w\s]+ today\'s cases [\w\s]+"):lambda country: data.get_country_data(country)['new_cases'],
					re.compile("[\w\s]+ critical cases [\w\s]+"):lambda country: data.get_country_data(country)['critical'],
					re.compile("[\w\s]+ today\'s deaths' [\w\s]+"):lambda country: data.get_country_data(country)['new_deaths'],
					re.compile("[\w\s]+ recovered [\w\s]+"):lambda country: data.get_country_data(country)['recovered'],
					re.compile("[\w\s]+ active [\w\s]+"):lambda country: data.get_country_data(country)['active']


					}



	UPDATE_COMMAND = "update"

	while True:
		text = get_audio()
		result = None

		for pattern, func in COUNTRY_PATTERNS.items():
			if pattern.match(text):
				words = set(text.split(" "))
				for country in country_list:
					if country in words:
						result = func(country)
						break

		for pattern, func in TOTAL_PATTERNS.items():
			if pattern.match(text):
				result = func()
				break

		if text == UPDATE_COMMAND:
			result = "Data is being updated. This will take a while"
			data.update_data()

		if result:
			speak(result)

		if text.find(END_PHRASE) != -1:  
			print("Exit")
			break

main()