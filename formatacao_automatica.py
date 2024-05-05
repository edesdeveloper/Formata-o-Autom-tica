import os
import subprocess
import pyautogui
import time

# Matriz de dados com endereços dos computadores
dados = []  

print("Digite 'fim' para sair")

while True:
    elemento = input("Digite o elemento: ")
    if elemento.lower()=='fim':
        break
    dados.append(elemento)

# Solicitar nome de usuário e senha ao usuário
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

def manusearCentral():
    # Move o mouse para sistemas operacionais
    pyautogui.moveTo(300, 250,duration=0.5)
    pyautogui.click()
    time.sleep(2)
    #Move o mouse para a matriz NICE
    pyautogui.moveTo(550, 300,duration=0.5)
    pyautogui.click()
    time.sleep(2)
    #Move o mouse para instalar a matriz
    pyautogui.moveTo(640, 300,duration=0.5)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1100, 640,duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(1050, 650,duration=0.5)
    pyautogui.click()

def minimize_mstsc():
    os.system('cmd /c "start /min taskkill /IM mstsc.exe /F"')

def open_central():
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.typewrite('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft System Center\Configuration Manager\Central de Software.lnk')
    pyautogui.press('enter')
    time.sleep(1)  

# Loop sobre os endereços na matriz dados
for i in range(len(dados)):
    
    
    # Pressiona Win+R para abrir a janela Executar
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('mstsc')
    pyautogui.press('enter')
    time.sleep(2)  # Aguarda um segundo para a janela Executar abrir
    
    # Digita o endereço do computador da posição i
    pyautogui.typewrite(dados[i])
    time.sleep(1)  # Aguarda um segundo para o endereço ser digitado
    
    # Pressiona Enter para iniciar a conexão
    pyautogui.press('enter')
    time.sleep(5)  # Aguarda alguns segundos para a conexão ser estabelecida
    
    # Digita o nome de usuário
    #pyautogui.typewrite(usuario)
    #pyautogui.press('tab')  # Move para o campo de senha
    
    # Digita a senha
    pyautogui.typewrite(senha)
    pyautogui.press('enter')  # Pressiona Enter para fazer login
    time.sleep(4)
    pyautogui.keyDown('left')
    time.sleep(2)  # Aguarda alguns segundos para o login ser concluído e a conexão ser estabelecida
    pyautogui.press('enter')  # Pressiona Enter para fazer login
    time.sleep(40)  # Aguarda alguns segundos para o login ser concluído e a conexão ser estabelecida
    
    outputLogin = f"query user /server:{dados[i]}"
    output = subprocess.check_output(outputLogin, shell=True, text=True)

    while usuario not in output:
        time.sleep(1)
        output = subprocess.Popen(f"query user /server:{dados[i]}", shell=True, stdout=subprocess.PIPE)
        output = output.stdout.read().decode('utf-8').strip()

    time.sleep(15)
    
        
    open_central()


    # Abre a "Central de Software"
    #pyautogui.hotkey('win', 's')  # Abre a barra de pesquisa do Windows
    #time.sleep(5)
    #pyautogui.typewrite("Central de Software")  # Digita o nome do programa
    #time.sleep(1)
    #pyautogui.press('enter')  # Pressiona Enter para abrir o programa
    #time.sleep(2)  # Aguarda alguns segundos para o programa ser aberto

    central=f'tasklist /S {dados[i]} /FI "IMAGENAME eq SCClient.exe"'
    outputCentral = subprocess.check_output(central, shell=True, text=True)
    cont=0
    while 'SCClient' not in outputCentral:
        time.sleep(1)
        cont=cont+1
        central=f'tasklist /S {dados[i]} /FI "IMAGENAME eq SCClient.exe"'
        outputCentral = subprocess.check_output(central, shell=True, text=True)
        if cont > 40:
            open_central()
            
    time.sleep(40)
    manusearCentral()
    time.sleep(5)
    minimize_mstsc()
    time.sleep(15)
