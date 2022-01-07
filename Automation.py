import dropbox
import cv2
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(1,100)
    video_capture_object = cv2.VideoCapture(0)
    result = True
    while(result):
        img_name = "Image"+number+".png"
        ret,frame = video_capture_object.read()
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    video_capture_object.release()
    cv2.destroyAllWindows()
    print("Snapshot Taken!!!")

take_snapshot()

def upload_image(img_name):
    access_token = "sl.A_lZuE2pZ6uivi0MQU69DRnv1Qq4n4yO8GqEtccVbmzgqOxnyTg7XwJ506vBanEI6eHKwwit5bw5W5Lu8XxYWrbH-W63b7wtEsFWrgq20AenfWkgOseF2TPFSYReezAcy35YvsoC1z4"
    name = img_name
    file_from = name
    file_to = "/test_dropbox/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("Files Uploaded!!!")

def main():
    while(True):
        if((time.time()-start_time) >= 5):
            name = take_snapshot()
            upload_image(name)

main()