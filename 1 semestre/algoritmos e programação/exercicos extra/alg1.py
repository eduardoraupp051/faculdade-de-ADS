import pyautogui
import subprocess
import time

# Caminho para o executável do Google Chrome
chrome_path = "C:\Program Files\Google\Chrome\Application"

# Comando para abrir o Chrome
comando = f'"{chrome_path}"'

# Executa o comando para abrir o Chrome
subprocess.Popen(comando)

# Aguarda alguns segundos para o Chrome abrir
time.sleep(5)

# Obtém as coordenadas da barra de pesquisa do Chrome
x, y = pyautogui.locateCenterOnScreen('caminho/para/imagem_da_barra_de_pesquisa.png')

# Clica na barra de pesquisa do Chrome
pyautogui.click(x, y)

# Digita a URL do Spotify
pyautogui.typewrite('https://www.spotify.com')
pyautogui.press('enter')
