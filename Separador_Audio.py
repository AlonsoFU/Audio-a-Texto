from pydub import AudioSegment
import math

# Código para Dividir el Audio
class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        self.audio = AudioSegment.from_wav(self.filepath)
        self.generated_files = 0  
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(self.generated_files) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            self.generated_files += 1  # Aumentar el contador
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')
        return self.generated_files # retornan el total de archivos generados