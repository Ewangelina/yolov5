DETECTION_ACTION = 0
current_snippet = None
SNIPPETS_FOLDER_NAME = "snippets"
w = -1
h = -1
#delete w and h
output_video_fps = 30
hasStarted = False
isShown = True

import time
import cv2
import re

def time_to_string(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d.%02d.%02d" % (hour, minutes, seconds)


def snippet_maker(SNIPPETS_FOLDER_NAME, start_time, fourcc_snippet, width, height, output_video_fps):
    filename = SNIPPETS_FOLDER_NAME + "/"

    filename = filename + time_to_string(time.time() - start_time) + ".mp4"
    #change filename to reflect real time
    snippet = cv2.VideoWriter(filename, fourcc_snippet, output_video_fps, (width, height))
    return snippet

def analiseLine(textLine, frame):
    global SNIPPETS_FOLDER_NAME, h, w, hasStarted

    if "motorcycle" in textLine:
        if not hasStarted:
            hasStarted = True
        if h == -1:
            h, w = frame.shape[0], frame.shape[1]
        make_snippet(frame)
    else:
        if hasStarted:
            end_snippet()

def make_snippet(frame_of_video):
    global w, h, output_video_fps, current_snippet

    if current_snippet is None:
        current_snippet = snippet_maker(SNIPPETS_FOLDER_NAME, 0, cv2.VideoWriter_fourcc(*'mp4v'), frame.shape[1], frame.shape[0], output_video_fps)
    current_snippet.write(frame_of_video)

def end_snippet():
    global current_snippet, hasStarted
    print(f"Saving {current_snippet}")
    current_snippet.release()
    hasStarted = False
