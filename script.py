import random,keyboard,time,pyautogui,datetime
from PIL import ImageGrab

pyautogui.FAILSAFE = False

def take_screenshot():#only for debugging
    img = ImageGrab.grab()
    img.save(f"{str(datetime.datetime.now()).replace(':','-')[0:16]}.png")


def move(key1,key2,key3):#moves character along x, y and z axis
    keyboard.press(key1)
    keyboard.press(key2)
    keyboard.press(key3)
    time.sleep(1)
    keyboard.release(key1)
    keyboard.release(key2)
    keyboard.release(key3)
    time.sleep(1)

time.sleep(3)
print("starting")

while True:
    
    keyboard.press_and_release("ctrl+windows+right")#change desktop
    time.sleep(0.5)
    keyboard.press_and_release("space")
    for i in range(3):
        pyautogui.click(960,540)#for focus change and attacking

    time.sleep(0.5)
    
    #key bind declaration
    arr1 = ["w","s"]
    arr2 = ["a","d"]
    arr3 = ["space"]
    
    #ramdom movement values 
    k1 = random.choice(arr1)
    k2 = random.choice(arr2)
    k3 = random.choice(arr3)
    move(k1,k2,k3)
    
    time.sleep(1)
    print(str(datetime.datetime.now()).replace(":","-")[0:16])
    # take_screenshot()
    
    keyboard.press_and_release("ctrl+windows+left")#change desktop
    
    time.sleep(300)#waits for 5 mins 
