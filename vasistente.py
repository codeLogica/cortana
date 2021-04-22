import os, time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from threading import Thread
os.system('cls')

filenames = ['cortana1.txt',
              'cortana2.txt',
              'cortana3.txt',
              'cortana4.txt',
              'cortana5.txt',
              'cortana6.txt',
              'cortana7.txt',
              'cortana8.txt',
              'cortana9.txt',
              'cortana10.txt',
              'cortana11.txt',
              'cortana12.txt',
              'cortana13.txt',
              'cortana14.txt',
              'cortana15.txt',
              'cortana16.txt']
frames = []

def animation(filenames, delay= 0.2, repets= 10):
    for name in filenames:
        with open(name, 'r', encoding='utf8') as f:
            frames.append(f.readlines())

    for i in range(repets):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system('cls')

respuesta_asistente = 'Te observo desde tu web cam Jonathan'

def micro_on():
    r= sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Usa Cortana cada vez que hables\nEjemplo: 'Hola, Cortana' o 'Cortana ¿que piensas de...'")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es-ES')
            print(text)
            if 'Cortana' in text or 'cortana' in text:
                if 'hola' in text or 'Hola' in text:
                    voice = gTTS(text='Hola Jefe', lang='es')
                    voice.save('asistente.mp3')
                    playsound('asistente.mp3')
                    micro_on()
                if 'Dante' in text or 'dante' in text:
                    voice5= gTTS(text='Gran maestro de python, buena persona, ojalá un día le pases mi codigo para que lo mejore jajaja', lang='es')
                    voice5.save('dante.mp3')
                    playsound('dante.mp3')
                else:
                    voice3 = gTTS(text='Hable bien carnal, no se le entiende', lang='es')
                    voice3.save('hable_bien-mp3')
                    playsound('hable_bien.mp3')
        except:
            repetir= gTTS(text='No te entendi Jefe Maestro', lang='es')
            repetir.save('repetir.mp3')
            playsound('repetir.mp3')
            micro_on()
            


Thread(target = micro_on).start()
Thread(target = animation(filenames)).start()
