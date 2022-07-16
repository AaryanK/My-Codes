from bs4 import BeautifulSoup
import requests





class Chelsea:
    def __init__(self):
        self.soup = BeautifulSoup(requests.get('https://www.goal.com/en-in/team/chelsea/fixtures-results/9q0arba2kbnywth8bkxlhgmdr').text,'lxml')
        self.f_r =self.soup.find(class_='widget-entity-matches__list')

    def get_results_all(self):
        results = []
        for i in self.f_r.find_all(class_="match-row match-row--status-pld"):
            results.append(f'{i.text.strip()}')
        return results

    def get_fixtures_all(self):
        fixtures = []
        for i in self.f_r.find_all(class_="match-row match-row--status-fix"):
            fixtures.append(f'{i.text.strip()}')
        return fixtures


print(Chelsea().get_results_all())
print(Chelsea().get_fixtures_all())
