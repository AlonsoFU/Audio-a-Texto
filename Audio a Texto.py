import speech_recognition as sr
import Separador_Audio as Sep


# Cargar el archivo de audio (asegúrate de que el archivo de audio esté en el mismo directorio)
folder=r"C:\Github Audio a Texto\__pycache__\Audios\\"
file="Recording_43.wav"
split_wav = Sep.SplitWavAudioMubin(folder, file)
num_archivos=split_wav.multiple_split(min_per_split=5)
print("Cantidad de Archivos Generados:", num_archivos)

# initialize the recognizer

lista = list(range(num_archivos))

for i in lista:
 print("Número Archivo",i)
 r = sr.Recognizer()
 filename = rf"C:\Github Audio a Texto\__pycache__\Audios\{i}_Recording_43.wav"
 # Abrir el archivo de audio usando SpeechRecognition
 with sr.AudioFile(filename) as source:
     audio_data = r.record(source)  # Leer el audio

     # Utilizar el reconocimiento de voz en español
     try:
         text = r.recognize_google(audio_data, language="es-ES")
         print("Texto transcribido en español: " + text)
     except sr.UnknownValueError:
         print("No se pudo reconocer el audio.")
     except sr.RequestError as e:
         print("Error en la solicitud al servicio de reconocimiento de voz: {0}".format(e))




