import cv2
import pyautogui as p
import numpy as np 
import mss.tools
          
while True:   
    with mss.mss() as sct:       
        monitor = {"top": 240, "left": 80, "width": 110, "height": 130}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        im = sct.grab(monitor)
    im = cv2.cvtColor(np.array(im),cv2.COLOR_RGB2BGR)
    pixels = np.sum(im < 100) 
    cv2.imshow('im', im) 
    if pixels > 4000 and pixels < 25000:
        p.press('space')
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break