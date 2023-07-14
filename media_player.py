import sys, pathlib
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QFileSystemModel
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QFileInfo

from UI.media_player_ui import Ui_media_player


class MediaPlayer (QMainWindow, Ui_media_player):

    current_directory = 'Qt/Media_Player/Audio_Files'

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # initialises a media player
        self.player = QMediaPlayer()

        '''
            initialses a file system in a list view(init_folder)
            applies filters so only the listed formats are shown
            nameFilterDisables(False) sets the items without the listed formats are hidden
        '''
        self.model = QFileSystemModel()
        self.model.setNameFilters(['*.mp3', '*.wav', '*.aac', '*.flac'])
        self.model.setNameFilterDisables(False)
        self.init_folder()

        # runs the player_timer when the track is playing
        self.player.positionChanged.connect(self.player_timer)

        # when the play/pause or stop buttons are pressed it runs the corresponding methods
        self.pb_play_pause.clicked.connect(self.play_pause_button)
        self.pb_stop.clicked.connect(self.stop_button)

        # allows the user to browse their files when file > browse is clicked
        self.actionBrowse.triggered.connect(self.select_file)
        
        # self.pb_back.clicked.connect(self.back_button)

        # self.pb_forward.clicked.connect(self.forward_button)

        # Controls the volume by signaling when the volume bar value is changed
        self.volume_slider.valueChanged.connect(self.volume_control)

    '''
        Method that runs on startup and allows the user to choose an audio file
        file_filter lists the file types we want to show to the user
        file_path opens a window and lets us choose a file
        file_path returns a tuple with the file path and data types
    '''
    def select_file(self):
        file_filter = '*.mp3 *.wav *.aac *.flac'
        self.file_path = QFileDialog.getOpenFileName(
            caption='Select a file', # shows what text appears at the top of the windw
            dir='Qt/Media_Player/Audio_Files', # initialises the directory we display
            filter=file_filter # uses the filter list from earlier to only show files of a certain type
            )
        self.set_audio()
        self.song_name()
        self.update_folder()

    '''
        sets the initial display folder as the current_directory path
        sets the treeView up to follow the model of the directory
    '''
    def init_folder(self):
        self.model.setRootPath(MediaPlayer.current_directory)
        self.folder_view.setModel(self.model)
        self.folder_view.setRootIndex(self.model.index(MediaPlayer.current_directory))
        
    '''
        when you switch to a different directory than the default it will update the display
        this will show the new directory you selected by overridding the current_directory path
    '''
    def update_folder(self):
        file_info = QFileInfo(self.file_url.toLocalFile())
        MediaPlayer.current_directory = file_info.absolutePath()
        self.model.setRootPath(MediaPlayer.current_directory)
        self.folder_view.setModel(self.model)
        self.folder_view.setRootIndex(self.model.index(MediaPlayer.current_directory))
        
    '''
        Method that initialises audio
        If a file is loaded it will remove it with stop so other files can be played
        Sets the url to be the selected file path
        QAudioOutput represents an output channel for audio
        Sets the QMediaPlayer audio output to be the defined audio output
        Tells the player the source of the file is the file we selected in the select_file method
        Sets the initial volume slider to be 50%
        Calls the volume control method to run which sets the output value
    '''
    def set_audio(self):
        self.player.stop()
        self.file_url = QUrl.fromLocalFile(self.file_path[0])
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(self.file_url)
        self.volume_slider.setSliderPosition(50)
        self.volume_percent.setText(f'{self.volume_slider.value} + %')
        self.volume_control()
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
        If the song title is '' (no song), the play button wont do anything
        If the player is playing audio it will pause the player
        If the player is not playing audio it will play the currently active sound file
    '''
    def play_pause_button(self):
        if self.lb_song_title.text() == '':
            pass
        elif self.player.isPlaying() == True:
            self.player.pause()
        else:
            self.player.play()

    '''
        When the stop button is pressed stops playing and resets the play position to 0
        Sets the song title and song time text to nothing
    '''
    def stop_button(self):
        self.player.stop()
        self.lb_song_title.setText('')
        self.lb_song_time.setText('')
       
    # def forward_button(self):
    #     print(self.file_path)

    '''
        Sets a variable volume to be the volume slider position / 100
        / 100 because the volume output is working on a 0 - 1 scale where 1 is 100%
        Sets the volume percentage text to equal the value of the slider
        Set the audio output to be equal to the volume variable

        Try/except block here to bypass the attribute error for changing the volume controls when no audio file has been setup
    '''
    def volume_control(self):
        try:
            self.volume = self.volume_slider.value() / 100
            self.volume_percent.setText(f'{self.volume_slider.value()}%')
            self.audio_output.setVolume(self.volume)
        except AttributeError:
            pass

# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    player = MediaPlayer()
    player.show()

    # terminates the program if it is exited
    sys.exit(app.exec())