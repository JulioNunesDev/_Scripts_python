import os
from time import sleep
import webbrowser
import random



#big-button play
# Script - para executar no pc da pessoa, abrir 1 - site,
# 2 - criar basta no directory main 
#webbrowser.open_new('https://www.nasa.gov/')
sistema = os.environ
driver = 'C:\\'
user = sistema['USERNAME']
gambiarra = 'Users\\'
destino = '\\Documents'
caminho = os.path.join(driver, gambiarra + user + destino)



frase = "O Anonymous surgiu em 2003 no fórum 4chan, representando as idéias de muitos usuários online e offline sobre anarquia e o cérebro global digitalizado. Membros anônimos (conhecidos como “Anons”) podem ser distinguidos em público pelo uso de máscaras de Guy Fawkes, um personagem do filme V de Vingança"





for pastas in range(1):
    nome = random.randint(0, 50000)
    teste = str(nome) + '#av77' + ''
    try:
        
        s =  os.mkdir(f'{teste}')
    except FileExistsError:
           print('file exists') 
    for root, subpast, files  in os.walk(teste):
        print(root)
        with open(root + '\\xx_unger.txt', 'w') as t:
            sleep(0.2)
            t.write(frase + '\n' + frase)
            print(t)
    webbrowser.open_new('https://www.nasa.gov/')
    webbrowser.open_new('https://www.xxx.com/')
                






