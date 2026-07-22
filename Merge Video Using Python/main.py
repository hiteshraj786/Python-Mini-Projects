from moviepy.editor import *


clip1 = VideoFileClip("tech.mp4").subclip(00,5)

clip2 = VideoFileClip("live.mp4").subclip(00,5)

clip2 = clip2.set_position((45,150))
final_video = concatenate_videoclips([clip1,clip2])
final_video.write_videofile("new.mp4")