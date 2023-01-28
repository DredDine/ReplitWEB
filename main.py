################## 🍣 Import of libraries 🍣 ##################

from selenium import webdriver # Importing webdriver ❤️‍🔥
from selenium.webdriver.chrome.options import Options # Importing Options 📢
from time import sleep # Importing sleep ⛑️
from os import system, name # Importing os 👀
from simple_chalk import chalk, greenBright, magentaBright, cyanBright, yellowBright, redBright, whiteBright # Importing simple_chalk ☂️

################## 🚩 Library preparation 🚩 ##################

chrome_options = Options()

##### Options 🐸

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

##### Driver 🚩

driver = webdriver.Chrome(options=chrome_options)

################## 🌚 Variables/Constants 🌚 ##################

##### Colors 🦑

green = chalk.greenBright # Green! 🙈
magenta = chalk.magentaBright # Magenta! ♥️
cyan = chalk.cyanBright # Cyan! 🤞
yellow = chalk.yellowBright # Yellow! 🥰
red = chalk.redBright # Red! 🐱
white = chalk.whiteBright # White! 👽

################## 🌲 Functions 🌲 ##################

def line(): # Line function! 🎂
    print()

def line_info(): # Line info function! 📢
    color_1 = cyan('========================')
    color_2 = magenta('=====================')
    print(color_1 + color_2 + color_1 + color_2)

def clear(): # Clear function! 😈
    if name == 'nt':
        _ = system('cls') # Windows 💌
    else:
        _ = system('clear') # Linux 🌆

################## 🌴 Start of ReplitWEB 🌴 ##################

clear()
sleep(1)
line()
sleep(1)
line_info()
line()
sleep(1)
print(cyan('['), magenta('-'), cyan(']'), yellow('-'), white('Made by:'), yellow('HiroBeet'))
sleep(1)
print(cyan('['), magenta('-'), cyan(']'), yellow('-'), white('ReplitWEB has just'), green('started'))
line()
line_info()
driver.get("https://google.com")
