import sys
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from PySide6.QtCore import QUrl

from UI.media_player_ui import Ui_Media_Player

class MediaPlayer (QWidget, Ui_Media_Player):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.audio()
        # self.player.metaDataChanged.connect(self.update_song_title)


    def audio(self):
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile('Qt/Media_Player/Audio_Files/piano.mp3'))
        self.audio_output.setVolume(0.1)
        self.player.play()

    # def update_song_title(self):
    #     song_title = self.player.metaData(QMediaMetaData.Title)
    #     self.lb_song_title.setText(song_title)

#creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    player = MediaPlayer()
    player.show()

    # terminates the program if it is exited
    sys.exit(app.exec())