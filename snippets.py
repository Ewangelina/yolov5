current_snippet = None
SNIPPETS_FOLDER_NAME = "snippets"

from datetime import datetime
import cv2
import re
import numpy

def time_to_string():
    now = datetime.now()
    return now.strftime("%Y%m%d %H%M%S")

def snippet_maker(SNIPPETS_FOLDER_NAME, fourcc_snippet, width, height, output_video_fps):
    filename = SNIPPETS_FOLDER_NAME + "/"
    temp = filename + time_to_string() + ".txt"
    f = open(temp, 'w')
    f.write("text2")
    f.close()

    filename = filename + time_to_string() + ".mp4"
    snippet = cv2.VideoWriter(filename, fourcc_snippet, output_video_fps, (width, height))
    return snippet

def make_snippet(frame_of_video, video):
    global current_snippet
    
    if current_snippet is None:
        h = len(frame_of_video)
        w = len(frame_of_video[0])
        output_video_fps = 30 #video CHANGE
        
        current_snippet = snippet_maker(SNIPPETS_FOLDER_NAME, cv2.VideoWriter_fourcc(*'mp4v'), w, h, output_video_fps)
        
    current_snippet.write(numpy.asarray(frame_of_video))

def end_snippet():
    global current_snippet
    print(f"Saving {current_snippet}")
    current_snippet.release()
    current_snippet = None
