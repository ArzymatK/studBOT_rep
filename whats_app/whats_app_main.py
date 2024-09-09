import webbrowser
import pyautogui
import time

phone_number = '+996554192006'
message = 'darkside'

webbrowser.open(f'https://web.whatsapp.com/send?phone={phone_number}&text={message}')

time.sleep(1)
pyautogui.press('Enter')