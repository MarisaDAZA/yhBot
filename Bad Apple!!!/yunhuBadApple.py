import cv2
from braille import image_to_braille
from yunhu import *
import time

set_recvId("7525795")
size = (77,58) #(62,46)

video = cv2.VideoCapture('Bad Apple!!.mp4')


def boardBadApple():
    last_time = time.time()
    frame_count = 0
    ret = True
    while ret:
        ret, frame = video.read()
        if frame_count % 10 == 0:
            board(image_to_braille(frame, size))
            sleep_time = 0.33 - (time.time() - last_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
            #print(time.time() - last_time, end='\r')
            last_time = time.time()
        frame_count += 1
    print(board_dismiss())

def editBadApple():
    last_time = time.time()
    frame_count = 1
    ret, frame = video.read()
    msgId = send(image_to_braille(frame, size),)['data']['messageInfo']['msgId']
    while ret:
        ret, frame = video.read()
        if frame_count % 10 == 0:
            edit(image_to_braille(frame, size), msgId)
            sleep_time = 0.33 - (time.time() - last_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
            #print(time.time() - last_time, end='\r')
            last_time = time.time()
        frame_count += 1
    recall(msgId)

if __name__ == '__main__':
    #boardBadApple()
    #editBadApple()
    pass