import face_recognition
import cv2
# import socket
class FrameModifier():


    def resizer(frame,ratio,orignal=False):
        if orignal==True:
            frame = cv2.resize(frame, (0, 0), fx=ratio, fy=ratio)
            return frame
        else:
            small_frame = cv2.resize(frame, (0, 0), fx=ratio, fy=ratio)
            return small_frame


    def RGBmaker(frame,orignal=False):
        if orignal==True:
            frame = frame[:, :, ::-1]
            return frame
        else:
            small_frame = frame[:, :, ::-1]
            return small_frame


class FaceRecognizer():
    def __init__(self,use_default_faces=True):
        self.use_default_faces=use_default_faces

    def webcam_capturer(self):
        pass

    def screen_capturer(self):
        pass

    def video_capturer(self):
        pass

    def image_capturer(self):
        pass

    def yt_video_capturer(self):
        pass
