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
        self.play_audio()

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

    # method that controls the audio playback
    def play_audio(self):
        
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


#creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    player = MediaPlayer()
    player.show()

    # terminates the program if it is exited
    sys.exit(app.exec())