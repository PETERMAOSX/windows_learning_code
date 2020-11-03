# 图片的操作
#     读入图片
#     cv2.imread() 读入图片
#     cv2.imread("图片路径",如何读取图片)
#     cv2.IMREAD_COLOR:读入一张彩色图片
#     cv2.IMREAD_GRAYSCALE:以灰度模式读入图像
#     #import cv2
#     #img = cv2.imread("Mao.jpg",0)
#
#     显示图片
#     cv2.imshow() 显示图像
#     cv2.imshow("窗口的名字",img(图片变量名字引用))
#     #cv2.imshow("image",img)
#     cv2.waitKey(0) #键盘绑定函数
#     cv2.destoryAllWindows()
#
#     保存图片
#     cv2.imwrite('messigray.png',img) #将图片img保存为messigray.png
#
#
# 例子
#     import numpy as up      #导入库
#     import cv2
#
#     img = cv2.imread('Mao.jpg',0)
#     cv2.imshow('image',img)
#     k = cv2.waitKey(0)
#     if k== 27: #按下ESC键
#         cv2.destoryAllWindows()
#     elif k == ord('s'):
#         cv2.imwrite('messigray.png',img)
#         cv2.destoryAllWindows();
#
# 在树莓派上打开摄像头
#     from picamera.array import PiRGBArray
#     from picamera import PiCamera
#     import time
#     import cv2
#
#     camera = PiCamera()
#     camera.resolution = (640,480)
#     camera.framerate = 32
#     rawCapture = PiRGBArray(camera,size=(640,480))
#
#     time.sleep(0.1)
#
#     for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=Ture):
#         image = frame.array