'''1) Navegue até o site https://cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
3) Clique em alerta, para gerar a alerta
4) Feche a alerta
5) Suba a página totalmente para cima
6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o 
quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"'''

import pyautogui
from time import sleep
import webbrowser

# 1 - Abrir o site  https://cursoautomacao.netlify.app/
webbrowser.open_new('https://cursoautomacao.netlify.app/')
sleep(2)
# 2 - rolar a pagina até encontra o campo "Exemplos alerta"
# pyautogui.moveTo(1475,-314,duration=2)
pyautogui.moveTo(1246,-800,duration=2)
pyautogui.scroll(-1100)

# 3 - Clicar no campo e digitar seu nome
pyautogui.click(1477,-798,duration=2)
pyautogui.typewrite('Thiago Alvaro',interval=0.1)
sleep(2)
# 4 - Clique em alerta, para gerar a alerta
pyautogui.click(1487,-747,duration=2)

# 5 - Fechar Alerta clicando em OK
pyautogui.click(1166,-856, duration=2)
sleep(1)
# 6 - subir a pagina toda pra cima
pyautogui.scroll(1100)
sleep(1)
# 7 - descer até a secção para fazer os downloads
pyautogui.scroll(-1300)
# 8 - clicar no botão fazer download da planilha excel 
pyautogui.click(419,-148,duration=2)
#e no botao salvar
pyautogui.click(557,-558,duration=2)

# 10 - clicar no botão fazer download do arquivo excel
pyautogui.click(601,-132,duration=2)
#e no botao salvar
# 11 - criar alertar " VOCE TERMINOU !".

