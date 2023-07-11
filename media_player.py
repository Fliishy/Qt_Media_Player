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
        self.song_name()

        # runs the player_timer when the track is playing
        self.player.positionChanged.connect(self.player_timer)

        self.pb_play_pause.clicked.connect(self.play_pause_button)
        self.pb_stop.clicked.connect(self.stop_button)
        # self.pb_back.clicked.connect(self.back_button)
        # self.pb_forward.clicked.connect(self.forward_button)

    
    '''
        Method that runs on startup and allows the user to choose an audio file
        file_filter lists the file types we want to show to the user
        file_path opens a window and lets us choose a file
        file_path returns a tuple with the file path and data types
    '''
    def select_file(self):
        file_filter = 'Data file (*.mp3 *.wav *.aac *.flac)'
        self.file_path = QFileDialog.getOpenFileName(
            caption='Select a file', # shows what text appears at the top of the windw
            dir='Qt/Media_Player/Audio_Files', # initialises the directory we display
            filter=file_filter # uses the filter list from earlier to only show files of a certain type
            )
        
    '''
    Method that initialises audio
    Sets the url to be the selected file path
    QAudioOutput represents an output channel for audio
    Sets the QMediaPlayer audio output to be the defined audio output
    Tells the player the source of the file is the file we selected in the select_file method
    Sets the initial volume of the audio output
    '''
    def set_audio(self):
        
        file_url = QUrl.fromLocalFile(self.file_path[0])
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(file_url)
        self.audio_output.setVolume(.2)
        self.player.play()

    '''
        Converts the file path to a QFileInfo object
        We set file path to index 0 so as to only retrieve the path, not the data types
        Gives us the name of the file from the QFileInfo object
        Sets the song title label to be the file name we just extracted
    '''
    def song_name(self):
        file_name_info = QFileInfo(self.file_path[0])
        file_name = file_name_info.fileName()
        self.lb_song_title.setText(file_name)

    '''
        Gets the player position in milliseconds
        Converts milliseconds into seconds and minutes with a // (floor operator)
        Sets the song_time label text to be a string with the minutes and seconds
    '''
    def player_timer(self):
        milliseconds = self.player.position()
        seconds = milliseconds // 1000
        minutes = seconds // 60

        self.lb_song_time.setText(str(f'{minutes}:{seconds}'))

    '''
        If the player is playing audio it will pause the player
        If the player is not playing audio it will play the currently active sound file
    '''
    def play_pause_button(self):
        if self.player.isPlaying() == True:
            self.player.pause()
        else:
            self.player.play()

    '''
        When the stop button is pressed stops playing and resets the play position to the beginning
        Sets the active track to an index that doesn't exist so it doesn't play anything
        Sets the song title text to be a dash
    '''
    def stop_button(self):
        self.player.stop()
        self.lb_song_title.setText('-')
        self.player.setActiveAudioTrack(-1)


# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    player = MediaPlayer()
    player.show()

    # terminates the program if it is exited
    sys.exit(app.exec())