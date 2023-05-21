DETECTION_ACTION = 0
current_snippet = None
SNIPPETS_FOLDER_NAME = "snippets"
w = -1
h = -1
#delete w and h
output_video_fps = 30
hasStarted = False
isShown = True

from datetime import datetime
import cv2
import re
import numpy

def time_to_string():
    now = datetime.now()
    return now.strftime("%Y%d%m %H%M%S")

def snippet_maker(SNIPPETS_FOLDER_NAME, start_time, fourcc_snippet, width, height, output_video_fps):
    filename = SNIPPETS_FOLDER_NAME + "/"
    temp = filename + time_to_string() + ".txt"
    f = open(temp, 'w')
    f.write("text2")
    f.close()

    filename = filename + time_to_string() + ".mp4"
    #change filename to reflect real time
    snippet = cv2.VideoWriter(filename, fourcc_snippet, output_video_fps, (width, height))
    return snippet

def analiseLine(textLine, frame):
    global SNIPPETS_FOLDER_NAME, h, w, hasStarted

    if "motorcycle" in textLine:
        if not hasStarted:
            hasStarted = True
        if h == -1:
            h, w = len(frame), len(frame[0])
        make_snippet(frame)
    else:
        if hasStarted:
            end_snippet()

def make_snippet(frame_of_video):
    global w, h, output_video_fps, current_snippet

    if current_snippet is None:
        current_snippet = snippet_maker(SNIPPETS_FOLDER_NAME, 0, cv2.VideoWriter_fourcc(*'mp4v'), w, h, output_video_fps)
    current_snippet.write(numpy.asarray(frame_of_video))

def end_snippet():
    global current_snippet, hasStarted
    print(f"Saving {current_snippet}")
    current_snippet.release()
    hasStarted = False
