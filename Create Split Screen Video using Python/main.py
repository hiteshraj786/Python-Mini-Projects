from moviepy.editor import * 



clip_1 = VideoFileClip("black.mp4").subclip(00,5)
clip_2 = VideoFileClip("live.mp4").subclip(00,5)
clip_3 = VideoFileClip("lord.mp4").subclip(00,5)
clip_4 = VideoFileClip("tech.mp4").subclip(00,5)


comb = clips_array([[clip_1,clip_2],[clip_3,clip_4]])
comb.write_videofile("test.mp4")