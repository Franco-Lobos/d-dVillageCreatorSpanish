import VillageData, Gestor, EditMenu
import sys, os

header = (80 * '=')
footer = (80 * '=')
line = (80* '-')
main = f'Bienvenido al gestor de aldeas y aldeanos, que desea hacer?\n {line} \n\n 1) Crear un pueblo \n 2) Editar un pueblo \n 3) Salir\n'

def mainselection(choice):
    if Gestor.validint(choice) is True:
        choice = int(choice)
        if choice == 1:
            village1 = VillageData.Village('new')
            village1.presentpopulation()
        elif choice == 2:
            if EditMenu.CheckVillage() is True:
                os.system('clear')
                selection = EditMenu.selectvillage()
                os.system('clear')
                print(header)
                EditMenu.editormenu(selection)
                
            else:
                os.system('clear')
                print(header)   
                selection = input(f'Lo siento, aún no hay aldeas para editar, primero cree alguna\n {main} {footer}\n')
                mainselection(selection)
        elif choice == 3:
            sys.exit()
            
        elif choice > 3:
            os.system('clear')
            print(header)
            selection = input(f'Lo siento, valor inválido.\n {main} {footer}\n')
            mainselection(selection)
    else:
        os.system('clear')
        selection = input(f'{header}\n Lo siento, no le entiendo.\n {main}\n {footer}\n')
        mainselection(selection)
    
def mainmenu():
    selection = input(f'{header}\n {main}\n {footer}\n')
    mainselection(selection)

os.system('clear')
while True:
    mainmenu()