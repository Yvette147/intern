"""
    使用python实现：读取USB摄像头的画面
"""
# 导入CV2模块
import cv2
import os
import time
import random

# 设置图片保存路径
path = r"D:\file\code\photo"


def read_usb_capture():
    curTime = time.localtime()
    intTimeInfo = [curTime.tm_year, curTime.tm_mon, curTime.tm_mday]
    timeInfo = [str(x) for x in intTimeInfo]
    r = random.randint(1000000, 9999999)
    t_name = '-'.join(timeInfo)
    # 选择摄像头的编号
    cap = cv2.VideoCapture(0)
    # 设置分辨率
    cap.set(3,4096)
    cap.set(4,4096)
    # 添加这句是可以用鼠标拖动弹出的窗体
    cv2.namedWindow('real_img', cv2.WINDOW_NORMAL)
    i = 1
    while(cap.isOpened()):
        # 读取摄像头的画面
        ret, frame = cap.read()
        # 真实图
        cv2.imshow('real_img', frame)
        k = cv2.waitKey(1) & 0xFF

        # 按's'存T3
        if k == ord('s'):
            filename = '_'.join([t_name, str(i), ".bmp"])
            print(filename)
            cv2.imwrite(os.path.join(path, filename), frame)
            i += 1
        # 按下'q'就退出
        elif k == ord('q'):
            break
    # 释放画面
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':


    read_usb_capture()


