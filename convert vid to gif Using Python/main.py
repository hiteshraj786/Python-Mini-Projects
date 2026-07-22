from moviepy.editor import *

video = VideoFileClip("tech.mp4").subclip(00,5).rotate(180)
video.write_gif("tech2.gif")