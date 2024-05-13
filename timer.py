import time

h, m, s = 0, 0, 0
print('[commands]\nadd : add time\nstart : start the timer\nstop : stop the timer\n-')

def formatTime(h, m, s):
    
    while s>=60:
        s -= 60
        m += 1
        
    while m>=60:
        m -= 60
        h += 1
        
    print(f"time: {h:0>2d}:{m:0>2d}:{s:0>2d}")

while True:

    inp = input()
    
    if inp == "add":
        
        h1, m1, s1 = map(int, input("enter time: ").split())
        h += h1
        m += m1
        s += s1
        formatTime(h, m, s)
        
    elif inp == "start":
        
        print("timer started")
        startTime = time.time()
        
    elif inp == "stop":

        print("timer stopped")
        endTime = time.time()
        usedTime = abs(round(startTime - endTime))
        s += usedTime
        formatTime(h, m, s)

    else:
        print("invalid command")

