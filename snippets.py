current_snippet = None
SNIPPETS_FOLDER_NAME = "output"
output_video_fps = 3

from datetime import datetime
import cv2
import re
import numpy
import os

def time_to_string():
    now = datetime.now()
    return now.strftime("%Y%m%d %H%M%S")

def snippet_maker(SNIPPETS_FOLDER_NAME, fourcc_snippet, width, height, output_video_fps):
    filename = SNIPPETS_FOLDER_NAME + "/"

    filename = filename + time_to_string() + ".avi"
    snippet = cv2.VideoWriter(filename, fourcc_snippet, output_video_fps, (width, height))
    return snippet

def make_snippet(frame_of_video):
    global current_snippet
    
    if current_snippet is None:
        h = len(frame_of_video[0])
        w = len(frame_of_video[0][0])
        
        current_snippet = snippet_maker(SNIPPETS_FOLDER_NAME, cv2.VideoWriter_fourcc(*'XVID'), w, h, output_video_fps)
    current_snippet.write(numpy.asarray(frame_of_video[0]))


def end_snippet():
    global current_snippet

    if current_snippet is None:
        return
    current_snippet.release()
    current_snippet = None
    print("Saved snippet")
