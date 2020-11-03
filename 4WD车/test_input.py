import win32api
import win32con

class MyLibrary(object):
    def keybd_event(self,VK_CODE): #VK_CODE为键盘编码
        # @Keyboard
        # input
        VK_CODE = int(VK_CODE)
        #print ":::VK_CODE:", VK_CODE
        print(";;;VK_CODE:{0}".format(VK_CODE))
        win32api.keybd_event(VK_CODE, 0, 0, 0)
        win32api.keybd_event(VK_CODE, 0, win32con.KEYEVENTF_KEYUP, 0)
        #print ":::press", str(VK_CODE), "successfully!"
        print(";;;press {0}".format(str(VK_CODE)))
        time.sleep(2)

if __name__ == '__main__':
        keybd_event(40) #键盘按下方向向下键
