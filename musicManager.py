from pygame import mixer


class playMusic:
    def __init__(self, song, volume):

        mixer.init()
        # Load audio file
        mixer.music.load(song)
        # Set preferred volume
        mixer.music.set_volume(volume)
        # Play the music
        mixer.music.play()

        self.mixer = mixer


    def stop(self,):
        self.mixer.music.stop()


