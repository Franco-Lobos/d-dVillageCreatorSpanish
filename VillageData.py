import os, sys, pandas as pd
from pandas.core.frame import DataFrame
import Generador, Gestor

header = (80 * '=')
footer = (80 * '=')
line = (80* '-')
directorio = os.getcwd()

class Village():
    def __init__(self, test):
        self.status = test
        if self.status == 'new':
            self.name = self.setvillagename(False, '').lower()
        else:
            self.name = test
        self.numberpeople = Generador.setnumberpeople()
        self.people = Generador.populationcreator(self.numberpeople)
        self.lider = Gestor.selectlider(self.people)

    def setvillagename(self, used, name):
        os.system('clear')
        print(header)
        if used == True:
            print (f'Lo siento, pero {name} ya está creado\n')
        test = input(f'¿Cómo quiere llamar a este pueblo?\n').lower()
        if self.metodoescritura(f'Aldea_{test}.xlsx') == 'a':
            return self.setvillagename(True, test)
        return test

    def presentpopulation(self):
        print(line)
        print(f'representados por el {self.lider[4]} {self.lider[0]} {self.lider[1]}, de {self.lider[2]} años y con fuerza {self.lider[3]}, habitan {self.name}:')
        for i in self.people:
            print(f'{i}){self.people[i][0]} {self.people[i][1]}: {self.people[i][2]} años, {self.people[i][3]} de fuerza y trabaja de {self.people[i][4]}')
        selection = input(f'{line}\nDesea guardar estos cambios?\n 1) Si, guardar {self.name} y su gente \n 2) No, eliminar datos\n{footer}\n')
        if Gestor.validint(selection) is True:
                selection = int(selection)
                if selection == 1:
                    os.system('clear')
                    self.savechanges(self.name)
                    print('Los datos han sido guardados exitosamente')
                    self.deletevillagedata()
                    
                elif selection == 2:
                    os.system('clear')
                    self.deletevillagedata()
                    print('Los datos han sido eliminados exitosamente')
                    
                elif selection > 2:
                    os.system('clear')
                    print('Numero invalido, por favor intente nuevamente\n')
                    self.presentpopulation() 
        else:
            os.system('clear')
            print('Valor invalido, por favor intente nuevamente\n')
            self.presentpopulation()

    def deletevillagedata(self):
        self.name = None
        self.numberpeople = None
        self.people = None
        self.lider = None
        
    def createdataframe(self, name, columnas):
        df = pd.DataFrame(list(self.people.values()), columns= columnas)
        if self.status == 'new':
            return df
        else:
            exist = pd.read_excel(f'{directorio}/Aldea_{name}.xlsx', sheet_name= 'People')
            startrow = int(exist.iloc[-1, 0])
            for i in self.people:
                inumb = i + startrow
                self.people[i][0] =  inumb
            df2 = pd.DataFrame(list(self.people.values()), columns= columnas)
            df = pd.concat([df,df2], axis = 0)
        return df

    def metodoescritura(self, filename):
        metodo = 'w'
        if filename in os.listdir():
            metodo = 'a'
            return metodo
        return metodo
        
    def savechanges(self, name):
        columnas = ['numberid', 'name', 'lastname', 'age', 'stength', 'job', 'lider', 'status']
        data = self.createdataframe(name, columnas)
        writer = pd.ExcelWriter(f"{directorio}/Aldea_{self.name}.xlsx", engine = "openpyxl")
        data.to_excel(writer, "People", index=False)
        writer.save()
        writer.close()
        
