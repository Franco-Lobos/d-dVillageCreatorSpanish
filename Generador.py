import sys, random, os
import Gestor, Generador

header = (80 * '=')
footer = (80 * '=')
line = (80* '-')
names = Gestor.opennames('nombres.txt')
lastnames = Gestor.opennames('apellidos.txt')

class Aldeano(object):
    def __init__(self):
        self.name = self.selectname()
        self.lastname = self.selectlastname()
        self.age = self.setage()
        self.strength = self.setstrength()
        self.job = self.setjob(self.strength)
        self.lider = self.setlidernumber(self.strength, self.age)
        self.status = 'alive'

    def selectname(self):
        return random.choice(names)
    
    def selectlastname(self):
        return random.choice(lastnames)
        
    def setage(self):
        return random.randint(20, 60)

    def setstrength(self):
        return 20 + Gestor.dado(10) + Gestor.dado(10)
    
    def setjob(self, strength):
        if strength <= 25:
            job = 'Artist'
        elif strength > 25 and strength <= 35:
            job = 'Farmer'
        elif strength > 35 and strength <= 40:
            job = 'Warrior'
        elif strength > 40:
            job = 'Golden warrior'
        return job

    def setlidernumber(self, strength, age):
        number = (strength * 10000) + (age * 100) + (random.randint(1, 99))
        return number

def setnumberpeople():
    test = input(f'¿Cuánta gente quieres crear?\n')
    try:
        if type(eval(test)) is int:
            return int(test)
    except:
        print('Numero invalido, por favor intente nuevamente')
        return setnumberpeople()
    
def populationcreator(number):
    populationdata = {}
    for i in range(number):
        i = i + 1
        person = Aldeano()
        populationdata[i] = [i,person.name, person.lastname, person.age, person.strength, person.job, person.lider, person.status]

    return populationdata




