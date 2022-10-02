import pyautogui as pg
import time
import webbrowser as web
import cowsay
import datetime

print(cowsay.cow("Bot by Dis"))

print(datetime.date)
print("1. Открыть ClassRoom")
print("2. Написать меседж в 'Мои заметки' в Viber")
print("3. Запустить Roblox")
saf = input("Выбери фунцию бота 1, 2, 3: ")

if saf == "1":
    web.open('https://classroom.google.com/u/1/')
if saf == "2":
    print("1. Закрыт")
    print("2. Открыт")
    cof = input("Вайбер закрыт или открыт? 1/2: ")
if cof == "1":
    msg = input("Write a messege: ")

    yn = pg.confirm('Start msg send bot?', buttons=['Yes', 'No'])

    if yn == 'Yes':
        time.sleep(1)
        pg.press('Win')
        time.sleep(1)
        pg.write('Viber')
        pg.press('Enter')
        time.sleep(10)
        pg.leftClick(x=38, y=154)
        time.sleep(1)
        pg.leftClick(x=892, y=1356)
        time.sleep(1)
        pg.write(msg)
        pg.press('Enter')

if cof == "2":
    msg = input("Write a messege (use only englesh languge): ")

    yn = pg.confirm('Start msg send bot?', buttons=['Yes', 'No'])
    
    if yn == 'Yes':
        pg.press('Win')
        time.sleep(1)
        pg.write('Viber')
        pg.press('Enter')
        time.sleep(1)
        pg.leftClick(x=38, y=154)
        time.sleep(1)
        pg.leftClick(x=892, y=1356)
        time.sleep(1)
        pg.write(msg)
        time.sleep(1)
        pg.press('Enter')
if saf == "3":
    web.open('https://www.roblox.com/home')
    time.sleep(1)
else:
    print("Okay bye, gl")