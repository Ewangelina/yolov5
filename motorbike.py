DETECTION_ACTION = 0
current_snippet = -1
SNIPPETS_FOLDER_NAME = "snippets"
w = -1
h = -1
output_video_fps = 30

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


def extract_frame_size(s):
    # Extract the frame size from the string using regular expressions
    pattern = r'(\d+)x(\d+)'
    match = re.search(pattern, s)
    if match:
        return int(match.group(1)), int(match.group(2))
    else:
        return None


def snippet_maker(SNIPPETS_FOLDER_NAME, start_time, fourcc_snippet, width, height, output_video_fps):
    filename = SNIPPETS_FOLDER_NAME + "/"

    filename = filename + time_to_string(time.time() - start_time) + ".mp4"
    snippet = cv2.VideoWriter(filename, fourcc_snippet, output_video_fps, (width, height))
    return snippet

def analiseLine(textLine, frame):
    global SNIPPETS_FOLDER_NAME, h, w

    if "motorcycle" in textLine:
        if h == -1:
            h, w = extract_frame_size(textLine)
        if isShown:
            cv2.imshow('Frame', frame)  # TODO FIX
        print(textLine)
        make_snippet(frame)

def make_snippet(frame_of_video):
    global current_snippet, w, h, output_video_fps

    if current_snippet == -1:
        current_snippet  = snippet_maker(SNIPPETS_FOLDER_NAME, 0, cv2.VideoWriter_fourcc(*'mp4v'), w, h, output_video_fps)
    current_snippet.write(frame_of_video)
