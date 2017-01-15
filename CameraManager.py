import cv2
import time

class CameraManager():
    def __init__(self, cameraIndex):
        self.cap = cv2.VideoCapture(cameraIndex)
        self.type = cameraIndex
    def getFrame(self):
        for i in xrange(10):
            success, frame = self.cap.read()
            if success:
                end_time = time.time()
                return frame
            else:
                continue
        print("Cannot get frame")
        return None



if __name__ == "__main__":
    cap = CameraManager(0)
    cv2.namedWindow("cap")
    counter = 0
    print(cap.getFrame())
    while cv2.waitKey(1) == -1:
        a = cap.getFrame()
        cv2.imshow('cap',a)
        if counter>100:
            break
        counter+=1