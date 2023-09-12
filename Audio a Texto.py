import speech_recognition as sr
import Separador_Audio as Sep

# Crear un reconocedor de voz
recognizer = sr.Recognizer()

# Cargar el archivo de audio (asegúrate de que el archivo de audio esté en el mismo directorio)
filename = rf"C:\Github\__pycache__\Audios\Recording_40.mp3"

split_wav = Sep.SplitWavAudioMubin(folder, file)
split_wav.multiple_split(min_per_split=1)

# initialize the recognizer
r = sr.Recognizer()


# Abrir el archivo de audio usando SpeechRecognition
with sr.AudioFile(filename) as source:
    audio_data = recognizer.record(source)  # Leer el audio

    # Utilizar el reconocimiento de voz en español
    try:
        text = recognizer.recognize_google(audio_data, language="es-ES")
        print("Texto transcribido en español: " + text)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz: {0}".format(e))





