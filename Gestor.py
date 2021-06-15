import sys, random, pandas as pd, os

header = (80 * '=')
footer = (80 * '=')
line = (80* '-')
directorio = os.getcwd()

def opennames(data):
    names = []
    data = open(f'{data}')
    for eachline in data.readlines():
        names.append(eachline[0:-2])
    data.close()
    return names

def dado(number):
    result = random.randint(1,number)
    while result == number:
        result = result + dado(number)
    return result

def validint(value):
    try:
        if type(eval(value)) is int:
            isint = True
    except:
        isint = False
    return isint

def selectlider(people):
    lider = (0,'Moises', 'Elpeluca', 22, 20, 'Pescador', 222001)
    for i in people:
        if int(people[i][6]) > lider[6]:
            lider = (people[i][0], people[i][1], people[i][2], people[i][3], people[i][4], people[i][5], people[i][6], people[i][7])
    return lider  

def showpopulation(filename):
    df = pd.read_excel(f'{directorio}/{filename}', sheet_name= 'People')
    os.system('clear')    
    print(header, f'\nHe aquí la gente de {filename[6:-5]}:\n', line, '\n', df, '\n', line)
    back = input('Ingrese \'Gracias jarvis\' para volver al menu Principal\n').lower()
    if back == 'gracias jarvis':
        os.system('clear')
        print('Por nada ciudadno promedio')
        pass
    else:
        showpopulation(filename)
    
def loadingbar(i, total):
    percentage = i*100/total
    dec = int(percentage/10)
    os.system('clear')
    print('█'*dec + '░'*(10-dec))
    print(percentage, '%')
    if percentage == 100:
        print('Proceso completo!')


