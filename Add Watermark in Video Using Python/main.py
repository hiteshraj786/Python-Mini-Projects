from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"})


clip = VideoFileClip("lord.mp4")

text_clip = TextClip("Hare Krishna", fontsize=70, color='blue')
text_clip = text_clip.set_position("center").set_duration(clip.duration)

video = CompositeVideoClip([clip, text_clip])

video.write_videofile("test.mp4")
