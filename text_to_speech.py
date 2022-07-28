import pyttsx3


# utilize pyttsx3 text to speech library
class TextToSpeech:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    volume = engine.getProperty('volume')
    rate = engine.getProperty('rate')

    # initiate text to speech engine
    def __init__(self, voice_num):
        self.engine.setProperty('voice', self.voices[voice_num].id)

    # change voice from male to female or vice versa 0 for male 1 for female
    def change_voice(self, voice_num):
        self.engine.setProperty('voice', self.voices[voice_num].id)

    # change volume with some arbituary number,
    def change_voice(self, volume_num):
        self.engine.setProperty('volume', volume_num)

    # change rate in wpm, default 200
    def change_rate(self, rate_num):
        self.engine.setProperty('rate', rate_num)

    # wip
    def save_to_file(self):
        pass

    # says inputted speech
    def speak(self, speech):
        self.engine.say(speech)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()
