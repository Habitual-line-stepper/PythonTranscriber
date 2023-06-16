import sys
import os
import speech_recognition as speech
from pydub import AudioSegment
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
    QPushButton, QFileDialog, QTextEdit


class TranscribingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Video to text transcriber')

        self.file_path = None

        layout = QVBoxLayout()

        self.label = QLabel('Select a file to transcribe')
        layout.addWidget(self.label)

        self.transcription_output = QTextEdit()
        self.transcription_output.setReadOnly(True)
        layout.addWidget(self.transcription_output)

        self.file_button = QPushButton('Select File')
        self.file_button.clicked.connect(self.select_file)
        layout.addWidget(self.file_button)

        self.transcribe_button = QPushButton('Transcribe')
        self.transcribe_button.clicked.connect(self.transcribe)
        self.transcribe_button.setEnabled(False)
        layout.addWidget(self.transcribe_button)

        self.setLayout(layout)

    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Video Files (*.mp4)')
        if file_dialog.exec_():
            self.file_path = file_dialog.selectedFiles()[0]
            self.label.setText(f'Selected file: {self.file_path}')
            self.transcribe_button.setEnabled(True)

    def transcribe(self):
        if self.file_path:
            audio_path = 'audio.wav'
            video_file = AudioSegment.from_file(self.file_path, format="mp4")

            audio = video_file.set_channels(1). \
                set_frame_rate(16000).set_sample_width(2)
            audio.export(audio_path, format='wav')

            recognition = speech.Recognizer()
            with speech.AudioFile(audio_path) as source:
                audio_text = recognition.record(source)

            text = recognition.recognize_google(audio_text, language='en-US')
            self.transcription_output.setPlainText(text)

            os.remove(audio_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranscribingApp()
    window.show()
    sys.exit(app.exec_())
