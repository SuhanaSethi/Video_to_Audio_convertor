import moviepy.editor
from tkinter.filedialog import *

vid = askopenfilename()
video = moviepy.editor.VideoFileClip("4091133-hd_1280_720_30fps.mp4")

aud = video.audio

aud.write_audiofile("converted_audio.mp3")

print("---End---")


