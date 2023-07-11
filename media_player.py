import sys
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QFileInfo

from UI.media_player_ui import Ui_Media_Player

class MediaPlayer (QWidget, Ui_Media_Player):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # initialises a media player
        self.player = QMediaPlayer()
        
        self.select_file()
        self.set_audio()

        self.pb_play_pause.clicked.connect(self.play_pause_button)
        self.pb_stop.clicked.connect(self.stop_button)
        # self.pb_back.clicked.connect(self.back_button)
        # self.pb_forward.clicked.connect(self.forward_button)

    # method that runs on startup and allows the user to choose an audio file
    def select_file(self):
        # filtering the type of files we want to show to the user
        file_filter = 'Data file (*.mp3 *.wav *.aac *.flac)'
        # opens a window and lets us choose a file
        # returns a tuple with the file path and data types
        self.file_path = QFileDialog.getOpenFileName(
            # shows what text appears at the top of the windw
            caption='Select a file',
            # initialises the directory we display
            dir='Qt/Media_Player/Audio_Files',
            # uses the filter list from earlier to only show files of a certain type
            filter=file_filter
            )
        # converts the file path to a QFileInfo object
        # we set file path to index 0 so as to only retrieve the path, not the data types
        file_name_info = QFileInfo(self.file_path[0])
        # gives us the name of the file from the QFileInfo object
        file_name = file_name_info.fileName()
        # sets the song title label to be the file name we just extracted
        self.lb_song_title.setText(file_name)

    # method that initialises audio
    def set_audio(self):
        
        # sets the url to be the selected file path
        file_url = QUrl.fromLocalFile(self.file_path[0])
        # represents an output channel for audio
        self.audio_output = QAudioOutput()
        # sets the QMediaPlayer audio output to be the defined audio output
        self.player.setAudioOutput(self.audio_output)
        # tells the player the source of the file is the file we selected earlier
        self.player.setSource(file_url)
        # sets the initial volume of the audio output
        self.audio_output.setVolume(.2)
        self.player.play()

    # when the play/pause button is pressed
    def play_pause_button(self):
        # if the player is playing audio it will pause the player
        if self.player.isPlaying() == True:
            self.player.pause()
        # if the player is not playing audio it will play the currently active sound file
        else:
            self.player.play()

    def stop_button(self):
        # stops playing and resets the play position to the beginning
        self.player.stop()
        # sets the active track to an index that doesn't exist so it doesn't play anything
        self.player.setActiveAudioTrack(-1)
        # sets the song title text to be a dash
        self.lb_song_title.setText('-')

#creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    player = MediaPlayer()
    player.show()

    # terminates the program if it is exited
    sys.exit(app.exec())