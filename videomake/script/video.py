import cv2
import numpy as np
import os

def running_string(string):
    dur = 3
    fps = 30

    weight, hight = 100, 100

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    file_path = os.path.dirname(os.path.abspath(__file__)) + "\\output.mp4"
    video_output = cv2.VideoWriter(file_path, fourcc, fps, (weight, hight))
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_thickness = 2
    font_color = (255, 255, 255)
    x, y = 100, 70
    shift = max((len(string) * 30 + 150) // 90, 2)
    for _ in range(dur * fps):
        frame = np.zeros((weight, hight, 3), dtype=np.uint8)
        frame[:] = (255, 0, 255)
        x -= shift
        cv2.putText(frame, string, (x, y), font, font_scale, font_color, font_thickness)
        video_output.write(frame)
    video_output.release()

