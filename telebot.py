from moviepy.editor import *
import moviepy.editor as mp
import moviepy.video.fx as fx
import textwrap
import numpy as np
import requests
import os
from pathlib import Path
from io import BytesIO
from PIL import Image
from gtts import gTTS





def color_clip(size, duration = 0.1, fps=25, color=(0,0,0), output='./videoclips/color.mp4'):
    ColorClip(size, color, duration=duration).write_videofile(output, fps=fps)


def tts(text):

    language = 'en'
    tld='com.au'

    with open(text) as f:
        lines = f.read()
    lines = lines.replace('\n',' ')
    textlist = lines.split('. ')

    if textlist[-1] == '':   
        textlist = textlist[:-1]
        print('last line blank')

    for i, line in enumerate(textlist):
        try:
            myobj = gTTS(text=line, lang=language, tld=tld, slow=False)
            myobj.save(f'./audio/{i}.mp3')
        except:
            pass

def getimage(url):

    with open(url) as f:
        lines = f.read()
    lines = lines.replace('\n',' ')
    print(lines)

    response = requests.get(lines)
    img = Image.open(BytesIO(response.content))
    return(img)

def addimage(url, size):
    
    with open(url) as f:
        lines = f.read()
    lines = lines.replace('\n',' ')
    print(lines)

    w, h = moviesize = (size)
    response = requests.get(lines)
    img = Image.open(BytesIO(response.content))
    
    if (img.width > img.height):
        perchange = (size[0] / img.width)
        img = img.resize((size[0], int(img.height * perchange)))
        if img.width > size[0]:
            perchange = (img.height / size[1])
            img = img.resize((size[0], int(h)))
        img = np.array(img)
        im = ImageClip(img)
    else:
        perchange = (size[1] / img.height)
        img = img.resize((int(img.width * perchange), size[1]))
        if img.width > size[0]:
            perchange = (size[0] / img.width)
            img = img.resize((int(w), size[1]))
        img = np.array(img)
        im = ImageClip(img)

    clip = VideoFileClip('./videoclips/color.mp4')

    cc = CompositeVideoClip([im.set_pos("center")], size=moviesize)

    cc.subclip(0, clip.duration).write_videofile("./image/image.mp4", fps=24)


def addtext(video, text, out, size):

    w, h = moviesize = (size)
    wrapper = textwrap.TextWrapper(width=30)
    word_list = wrapper.wrap(text=text)
    video = mp.VideoFileClip(video)
    text = "\n".join(word_list)
    text = TextClip(text, font='DejaVu Sans', bg_color = 'black', stroke_color = 'black', fontsize = (70), color = 'white').set_pos(('center',(h//2))).set_duration(video.duration)
 
 
    final = mp.CompositeVideoClip([video, text]) 
    final.write_videofile(f'{out}.mp4')

def textdir(text, size):
    with open(text) as f:
        lines = f.read()
    lines = lines.replace('\n',' ')
    textlist = lines.split('. ')
    if textlist[-1] == '':   
        textlist = textlist[:-1]


    for i, line in enumerate(textlist):
        try:
            addtext(f'./image/image.mp4', line, f'./textclips/textclip{i}', size)
        except: 
            addtext(f'./videoclips/color.mp4', line, f'./textclips/textclip{i}', size)

def looper(vid, aud):

    audio = AudioFileClip(aud)
    clip = VideoFileClip(vid)
    loopedClip = clip.loop(duration = audio.duration)

    loopedClip = clip.set_audio(audio)

    loopedClip.write_videofile(f"{aud}.mp4")

def loopdir():
    import ffmpeg
    import os
    path = os.listdir('./audio')
    
    for i, aud in enumerate(path):
        try:
            audio = AudioFileClip(f'./audio/{i}.mp3')
            clip = VideoFileClip(f'./textclips/textclip{i}.mp4')
            loopedClip = clip.loop(duration = audio.duration)
            loopedClip = clip.set_audio(audio)
            loopedClip.write_videofile(f"./videoclips/{i}.mp4")
        except:
            pass


def concat():
    import ffmpeg
    import os
    loaddir = os.listdir('./textclips')
    clips =[]
    clip_num = 0

    path_to_file = './image/image.mp4'
    path = Path(path_to_file)

    if path.is_file():
        final = mp.VideoFileClip('./image/image.mp4')
        blank = mp.VideoFileClip('./image/image.mp4')
    else:
        final = mp.VideoFileClip('./videoclips/color.mp4')
        blank = mp.VideoFileClip('./videoclips/color.mp4')

    for i, aud in enumerate(loaddir):
        if aud.startswith('textclip'):
            clips.append(f'textclip{clip_num}.mp4')
            clip_num += 1

    for i, clip in enumerate(clips):
        new_clip = mp.VideoFileClip(f'./videoclips/{i}.mp4')
        new_clip = new_clip.set_end((new_clip.duration - 0.3))
        final = mp.concatenate_videoclips([final, new_clip])

        
    final.write_videofile(f'./final/final.mp4')
