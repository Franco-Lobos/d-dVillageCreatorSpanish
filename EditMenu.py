import os
import Gestor, Generador, VillageData

header = (80 * '=')
footer = (80 * '=')
line = (80* '-')
directorio = os.getcwd()
menu = f'Bienvenido al editor de aldeas y aldeanos, que pueblo desea editar?\n {line}'

def CheckVillage():
    exist = False
    for i in os.listdir():
        if i.startswith('Aldea_'):
            exist = True
            return exist
    return exist

def selectvillage():
    print(header,'\n' ,menu)
    options = {}
    counter = 0
    for i in os.listdir():
        if i.startswith('Aldea_'):
            counter = counter + 1
            options[counter] = i
            print(f'{counter}) {i[6:-5]}')
    selection = input(footer)
    if Gestor.validint(selection) is True:
        selection = int(selection)
        if selection in options:
            return options[selection]
        else:
            os.system('clear')
            print(f'Lo siento, valor inválido.\n')
            options = None
            return selectvillage()
    else:
        os.system('clear')
        print(f'Lo siento, no le entiendo.\n')
        options = None
        return selectvillage()
    
def renamevillage(select, name):
    os.system('clear')
    newname = input(f'{header}\nPor favor, selccione el nuevo nombre que reemplazará a {name}\n {line}\n').lower()
    confirm = input(f'Está seguro que desea cambiar el nombre de {name} a {newname}?\n 1) Si, renombrar \n 2) No, cancelar\n{footer}')
    if Gestor.validint(confirm) is True:
        confirm = int(confirm)
        if confirm == 1:
            os.rename(select, f'Aldea_{newname}.xlsx')
            os.system('clear')
            print(f'Enhorabuena, {name} ahora se llama {newname}!')
        elif confirm ==2:
            os.system('clear')
            print('Edición cancelada\n')
    else:
        os.system('clear')
        print(f'{header}\n Lo siento, no le entiendo.\n')
        renamevillage(select, name)

def deletevillage(select, name):
    os.system('clear')
    confirm = input(f'{header}\nEstá seguro que desea exterminar a {name} y toda su gente?\n 1) Si, genocidio \n 2) No, cancelar\n')
    if Gestor.validint(confirm) is True:
        confirm = int(confirm)
        if confirm == 1:
            os.remove(f'{directorio}/{select}')
            print(f'Enhorabuena, {name} ha sido borrada del mapa!')
        elif confirm ==2:
            os.system('clear')
            print('Genocidio cancelado\n')
    else:
        os.system('clear')
        print(f'{header}\n Lo siento, no le entiendo.\n')
        renamevillage(select, name)  

def editormenu(selection):
    name = selection[6:-5]
    print(f'Bienvenido a {name}, que desea hacer por aquí? \n {line}\n 1) Renombrar {name}\n 1) Invitar aldeanos a {name} \n 3) Mostrar aldeanos existentes\n 4) Eliminar {name} \n{footer}\n')
    choice = input('') 
    if Gestor.validint(choice) is True:
        choice = int(choice)
        if choice == 1:
            renamevillage(selection, name)
        elif choice == 2:
            newpeople = VillageData.Village(name)
            newpeople.presentpopulation()
        elif choice == 3:
            Gestor.showpopulation(selection)
            
        elif choice == 4:
            deletevillage(selection, name)
        elif choice > 4:
            os.system('clear')
            print(f'{header}\n Lo siento, número inválido.\n')
            editormenu(selection)
    else:
        os.system('clear')
        print(f'{header}\n Lo siento, no le entiendo.\n')
        editormenu(selection)
    