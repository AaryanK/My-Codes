class SanbeedthLaudu:

    def __init__(self,name):
        self.name=name

    def display_identity(self):
        name = self.name
        print("The name of the laudu is: ",name)

    def disletter(self):
        name = self.name
        print("The first letter of the laudu is:  ",name[0])

    def dis6letter(self):
        name = self.name
        print("The sixth letter of the laudu is:  ",name[5])

sanbeedth = SanbeedthLaudu('Sanbeedth Jung Thapa')
sanbeedth.dis6letter()      


        


