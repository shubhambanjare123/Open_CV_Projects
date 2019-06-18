import time
from pygame import mixer
mixer.init()
mixer.music.load("D:\Shubham\Python Program\Open CV Projects\Open_CV_Projects\Media\Biba.mp3")

mixer.music.play()
    
time.sleep(30)                                           

mixer.music.pause()

