import speech_recognition as sr

"""
PyAudio pour utiliser le microphone 
(sur linux, installer avec sudo apt-get install portaudio19-dev python-pyaudio 
si impossible de l'installer avec pip)

voir documentation/explication ici https://pypi.org/project/SpeechRecognition/#pyaudio-for-microphone-users
"""
import pyaudio


r1 = sr.Recognizer()    # instance de la reconnaissance vocale (avec google utilisé, c'est que en anglais pour l'instant)

while True: # boucle principale
    try:
        with sr.Microphone() as mic:

            r1.adjust_for_ambient_noise(mic, duration=0.2)  # ajustement du son en capturant sur 0.2 secondes le bruit ambiant afin de les supprimer
            audio = r1.listen(mic)

            text = r1.recognize_sphinx(audio)   # notre texte traduit avec la reconnaissance de google (en ligne du coup), avec en paramètre d'entrée notre micro
            text = text.lower()

            print(text)

            if text == "exit":  # quand le mot prononcé est exit, on quit le programme (la boucle principale) pour tester
                break

    # FIXME : corrigé cette erreur non pris par l'exception
    except sr.UnknownValueError():  # en cas d'erreur, mais cette erreur n'est pas acceté par Python
        r1 = sr.Recognizer()    # en cas d'erreur, on recrée une instance de la reconnaissance vocale
        continue
