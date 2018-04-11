from PIL import Image, ImageStat
import picamera
import requests
import time
while True :
    while True :
        print("first while")
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture("/home/pi/test.jpg")
            print("Picture taken.")
            im = Image.open("test.jpg").convert("RGB")
            stat = ImageStat.Stat(im)
            if sum(stat.sum)/3 != stat.sum[0]:#not black
                print("second while")
                camera.capture("/home/pi/light.jpg")
                print("d")
                camera.capture("/home/pi/test.jpg")
                print("dd")
                im = Image.open("test.jpg").convert("RGB")
                print("ddd")
                stat = ImageStat.Stat(im)
                print("dddd")
            else:
                #if sum(stat.sum)/3 == stat.sum[0]:#black
                print("black and send light pic")
                URL = "http://192.168.1.3:5000/"
                files = {'image':open('/home/pi/light.jpg')}
                r=requests.post(URL, files=files)
                print(r.text)
                break 
    
    time.sleep(5)        
        #sum(stat.sum)/3 == stat.sum[0]:
            
            #print("Black Pic")
            #print("take pic again")
            #.capture("/home/pi/Myimage.jpeg")
            #count=count-
   # print("Light Pic")
   # URL = "http://192.168.1.3:5000/"
    #files = {'image':open('/home/pi/light.jpg')}
    #r=requests.post(URL, files=files)
    #print(r.text)
    #time.sleep(2)
      