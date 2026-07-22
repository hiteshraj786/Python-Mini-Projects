# import cv2
# import pyautogui
# from win32api import GetSystemMetrics
# import numpy as np
# import time
# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
# dim = (width,height)
# f = cv2.VideoWriter_fourcc(*"XVID")
# output = cv2.VideoWriter("test.mp4",f,30.0,dim)
# now_start_time = time.time()
# dur = 20+4
# end_time = now_start_time+dur
# while True:
#     image = pyautogui.screenshot()
#     frame_1 = np.array(image)
#     # frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
#     frame = cv2.cvtColor(frame_1, cv2.COLOR_RGB2BGR)

#     output.write(frame)
#     c_time = time.time()
#     time.sleep(1/30)  # 30 FPS

#     if c_time > end_time:
#         break 
# output.release()

# print("-----END-----")


import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")

frames = []
now_start_time = time.time()
dur = 24
end_time = now_start_time + dur

# Record frames and store in list
while time.time() < end_time:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_RGB2BGR)
    frames.append(frame)

    # Short sleep to reduce CPU usage
    time.sleep(0.05)

# Now calculate actual FPS
actual_duration = time.time() - now_start_time
actual_fps = len(frames) / actual_duration
print(f"Frames captured: {len(frames)}")
print(f"Actual FPS: {actual_fps:.2f}")

# Write frames to video using actual FPS
output = cv2.VideoWriter("test.mp4", f, actual_fps, dim)

for frame in frames:
    output.write(frame)

output.release()
print("-----END-----")



    