#Checker on Maker RPA
from time import *
import threading
import sys, os

score = 0
def countdown():
    global my_timer
    my_timer = 5
    
    for x in range(5):
        my_timer = my_timer - 1
        sleep(1)
        
    if score == 1:
        pass
    else:
        print("Action has not complete")
        os.execv(sys.executable,['RPAChecker'] + sys.argv)

countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()

for o in range(8):
    print(str(o))
    sleep(1)

print("Action completed")
score = 1




