import telebot
import req
from telebot import *
import os

def run(sub, size = (1080,1920)):
    os.system(f'mkdir ./audio')
    os.system(f'mkdir ./videoclips')
    os.system(f'mkdir ./textclips')
    os.system(f'mkdir ./final')
    os.system(f'mkdir ./image')
    
    req.uest(sub)
    telebot.color_clip(size)
    telebot.tts('text.txt')
    #telebot.getimage('url.txt')
    try:
        telebot.addimage('url.txt', size)
    except:
        pass
    telebot.textdir('text.txt', size)
    telebot.loopdir()
    telebot.concat()
    clear()

def clear():
    os.system(f'rm -rf ./audio')
    os.system(f'rm -rf ./videoclips')
    os.system(f'rm -rf ./textclips')
    os.system(f'rm -rf ./image')
    os.system(f'rm -f text.txt')
    os.system(f'rm -f url.txt')
