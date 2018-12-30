#MUSIC PLAYER --- HOBBY MODE
#2018 - Concept By Dorgival Filho

from tkinter import *
from tkinter import filedialog
import taglib
from pygame import mixer

Player = Tk()
Player.title('Music Player --- Concept By Dorgival Filho')
Player.geometry('480x360')
Player.config(background='black')

mFile = ''
vol = StringVar()
InfoMusic = {'Title': StringVar(), 'Artist':StringVar(), 'Album':StringVar(), 'Date':StringVar()}
InfoTags = None
loaded = False

def OpenMusic():
    global mFile
    global loaded
    global TagMusic
    global InfoTags
    mFile = filedialog.askopenfilename(filetypes=[('File', '.mp3'), ('File', '.ogg')], initialdir='/home/dorgyfilho/Musica')
    if mFile != None:
        mixer.music.load(mFile)
        InfoTags = taglib.File(mFile)
        loaded = True
        InfoMusic['Title'].set(InfoTags.tags['TITLE'][0])
        InfoMusic['Artist'].set(InfoTags.tags['ARTIST'][0])
        InfoMusic['Album'].set(InfoTags.tags['ALBUM'][0])
        InfoMusic['Date'].set(InfoTags.tags['DATE'][0])
        InfoMusic['Title'].get()
        mixer.music.play()
    else:
        pass

def Volume(comd):
    global vol
    VolStr = mixer.music.get_volume()
    vol.set(VolStr)
    if comd == '+':
        VolStr = str(round(float(mixer.music.get_volume()+0.1), 1))
        vol.set(VolStr)
    elif comd == '-':
        VolStr = str(round(float(mixer.music.get_volume()-0.1), 1))
        vol.set(VolStr)
    mixer.music.set_volume(float(vol.get()))

def Play(OpenFile):
    if not OpenFile:
        return 'Null'
    else:
        mixer.music.unpause()
        pass

def Pause():
    pMusic = True
    mixer.music.pause()

def Stop():
    mixer.music.stop()

def TagMusic(Tag):
    global InfoTags
    if Tag == 'Title':
        if InfoMusic:
            return InfoMusic['Title']
        else:
            return None
    
    if Tag == 'Artist':
        if TagMusic:
            return InfoMusic['Artist']
        else:
            return None

    if Tag == 'Album':
        if TagMusic:
            return InfoMusic['Album']
        else:
            return None
    
    if Tag == 'Date':
        if TagMusic:
            return InfoMusic['Date']
        else:
            return None

mainMenu = Menu(Player)
fMenu = Menu(mainMenu, tearoff=0)
fMenu.add_command(label='Open', command=lambda:OpenMusic())
fMenu.add_separator()
fMenu.add_command(label='Exit', command=lambda:exit())
mainMenu.add_cascade(label='File', menu=fMenu)
Player.config(menu=mainMenu)

PlayMusic = Button(Player, text='Play', fg='black', bg='white', font=('Kalimati', '7'), height=1, width=5, command=lambda:Play(mFile))
PlayMusic.grid(row=2, column=0)

PauseMusic = Button(Player,text='Pause', fg='black', bg='white', font=('Kalimati', '7'), height=1, width=5, command=lambda:Pause())
PauseMusic.grid(row=2, column=1)

StopMusic = Button(Player, text='Stop', fg='black', bg='white', font=('Kalimati', '7'), height=1, width=5, command=lambda:Stop())
StopMusic.grid(row=2, column=3)

VolumeMusic = Label(text='Volume: ', fg='black', bg='white', font=('Kalimati', '10'))
VolumeMusic.grid(row=2, column=4)

DecVol = Button(Player, text='-', fg='black', bg='white', font=('Kalimati', '7'), command=lambda:Volume('-'))
DecVol.grid(row=2, column=5)

IncVol = Button(Player, text='+', fg='black', bg='white', font=('Kalimati', '7'), command=lambda:Volume('+'))
IncVol.grid(row=2, column=6)

TitleMusic = Label(text='Title', fg='white', bg='black', font=('Kalimati', '10'))
TitleMusic.grid(row=3, column=0)
TitleLabel = Label(textvariable=TagMusic('Title'))
TitleLabel.grid(row=3, column=1)

ArtMusic = Label(text='Artist:', fg='white', bg='black', font=('Kalimati', '10'))
ArtMusic.grid(row=4, column=0)
ArtMusicLabel = Label(textvariable=TagMusic('Artist'))
ArtMusicLabel.grid(row=4, column=1)

AlbumMusic = Label(text='Album:', fg='white', bg='black', font=('Kalimati', '10'))
AlbumMusic.grid(row=5, column=0)
AlbumLabel = Label(textvariable=TagMusic('Album'))
AlbumLabel.grid(row=5, column=1)

DateLabel = Label(text='Date:', fg='white', bg='black', font=('Kalimati', '10'))
DateLabel.grid(row=6, column=0)
DateLbl = Label(textvariable=TagMusic('Date'))
DateLbl.grid(row=6, column=1)

mixer.init()
Player.mainloop()

