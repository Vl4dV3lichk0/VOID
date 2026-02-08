from librosa import load, util
from soundfile import *
from numpy import *
from .constants import *
from .exceptions import *

class AudioLoader():
    def __init__(self, target_sample_rate=TARGET_SAMPLE_RATE, normalize=True, mono=True):
        self.target_sample_rate = target_sample_rate
        self.normalize = normalize
        self.mono = mono

    def load_from_file(self, file_path):
        if ''.join(file_path[-4:-1]) not in AUDIO_FORMATS and ''.join(file_path[-5:-1]) != '.flac':
            raise UnsupportedFormatError(f'{file_path[-4:-1]} format is not supported.')
        try:
            audio = load(file_path, sr=self.target_sample_rate, mono=True, duration=MAX_DURATION)
        except AudioLoadError as e:
            print(e)
        finally:
            if self.normalize is True:
                audio = util.normalize(audio)
            return audio, self.target_sample_rate
        
class MicrophoneStreamer():
    def __init__(self):
        self.channels = 1
        self.sample_rate = TARGET_SAMPLE_RATE

    def record_from_microphone(duration_seconds):
        pass
