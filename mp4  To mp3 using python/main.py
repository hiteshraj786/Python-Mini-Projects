# import moviepy
# from tkinter.filedialog import*

# vid = askopenfilename()

# video = moviepy.editor.VideoFileClip(vid)


# aud = video.audio
# aud.write_audiofile("demo.mp3")

# print("----END------")


from moviepy import VideoFileClip
from tkinter.filedialog import askopenfilename

vid = askopenfilename()
video = VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("demo.mp3")

print("----END------")
