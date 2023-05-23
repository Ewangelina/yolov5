import time


file = None
start_time = None
no_motorcycles = 0

def time_to_string(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d.%02d.%02d" % (hour, minutes, seconds)

def init_statistics():
    global file, start_time
    
    start_time = int(time.time())
    filename = "snippets/" + time.strftime("%Y%m%d %H%M%S", time.localtime()) + " statistics.txt"
    file = open(filename, "w")

def mpm(seconds, motorcycles):
    minutes = seconds / 60
    return str(motorcycles / minutes)


def end_statistics():
    end_time = int(time.time())
    operational_time = end_time - start_time
    line = "\nOperational for: " + time_to_string(operational_time)
    file.write(line)
    line = "\nObserved motorcycles: " + str(no_motorcycles)
    file.write(line)
    line = "\nWhich averages to: " + mpm(operational_time, no_motorcycles) + " motorcycles per minute\n"
    file.write(line)
    file.close()

init_statistics()
input()
end_statistics()
