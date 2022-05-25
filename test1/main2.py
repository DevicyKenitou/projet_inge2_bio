import speech_recognition as sr
import signal
import sys
import pocketsphinx

"""
PyAudio pour utiliser le microphone 
(sur linux, installer avec sudo apt-get install portaudio19-dev python-pyaudio 
si impossible de l'installer avec pip)

voir documentation/explication ici https://pypi.org/project/SpeechRecognition/#pyaudio-for-microphone-users
"""
import pyaudio

# https://www.delftstack.com/fr/howto/python/keyboard-interrupt-python/#utilisez-des-gestionnaires-de-signaux-pour-d%C3%A9tecter-l-erreur-keyboardinterrupt-en-python
def sigint_handler(signal, frame):
    print ('KeyboardInterrupt is caught')
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

r1 = sr.Recognizer()    # instance de la reconnaissance vocale (avec google utilisé, c'est que en anglais pour l'instant)
print("####### Début #########")
while True: # boucle principale
    
    with sr.Microphone() as mic:
        print("> START MICRO")
        r1.adjust_for_ambient_noise(mic, duration=0.2)  # ajustement du son en capturant sur 0.2 secondes le bruit ambiant afin de les supprimer
        audio = r1.listen(mic)
        print("> END MICRO")

    try:
        print(">> START CONVERTION")
        text = r1.recognize_sphinx(audio)   # notre texte traduit avec la reconnaissance de google (en ligne du coup), avec en paramètre d'entrée notre micro
        text = text.lower()
        print(">> END CONVERTION")

        print(">> RESULT : " + text)

        if text == "exit":  # quand le mot prononcé est exit, on quit le programme (la boucle principale) pour tester
            break
    except KeyboardInterrupt:
        print('Bye 👋')
        break;
    # FIXME : corrigé cette erreur non pris par l'exception
    except sr.UnknownValueError:  # en cas d'erreur, mais cette erreur n'est pas acceté par Python
        r1 = sr.Recognizer()    # en cas d'erreur, on recrée une instance de la reconnaissance vocale
        continue
    except Exception as e:
        print('#### ERROR ####\n')
