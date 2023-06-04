import time

file = None
start_time = None
sum_no_motorcycles = 0
max_no_motorcycles_in_current_detection = 0

def time_to_string(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d:%02d" % (hour, minutes, seconds)

def init_statistics():
    global file, start_time, sum_no_motorcycles

    sum_no_motorcycles = 0
    
    start_time = int(time.time())
    filename = "output/" + time.strftime("%Y%m%d %H%M%S", time.localtime()) + " statistics.txt"
    file = open(filename, "w")

def mpm(seconds, motorcycles):
    minutes = seconds / 60
    return str(motorcycles / minutes)

def motorcycles_exited_action():
    global max_no_motorcycles_in_current_detection, sum_no_motorcycles
    sum_no_motorcycles += max_no_motorcycles_in_current_detection
    line = time.strftime("%d.%m %H:%M:%S", time.localtime()) + " Noted at least " + str(max_no_motorcycles_in_current_detection) + " motorcycle(s)\n"
    file.write(line)
    max_no_motorcycles_in_current_detection = 0

def end_statistics():
    end_time = int(time.time())
    operational_time = end_time - start_time
    line = "\nOperational for: " + time_to_string(operational_time)
    file.write(line)
    line = "\nObserved motorcycles: " + str(sum_no_motorcycles)
    file.write(line)
    line = "\nWhich averages to: " + mpm(operational_time, sum_no_motorcycles) + " motorcycles per minute\n"
    file.write(line)
    file.close()

def analise_line(textLine): #returns True if there are motorcycles in frame
    global max_no_motorcycles_in_current_detection
    
    parts = textLine.split(" ")
    index = -1
    for i in range(len(parts)):
        if parts[i] == "motorcycle," or parts[i] == "motorcycles,":
            index = i - 1
            break
        
    if index == -1: #No motorcycles
        return False
    else: #there are motorcycles
        no_motorcycles = int(parts[index])
        if max_no_motorcycles_in_current_detection < no_motorcycles:
            max_no_motorcycles_in_current_detection = no_motorcycles
        return True
            
