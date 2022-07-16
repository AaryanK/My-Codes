# import cv2
import pafy


def video_url(url):
    video = pafy.new(url)
    best = video.getbest(preftype="mp4")
    return best.url


# capture = cv2.VideoCapture(video_url('https://www.youtube.com/watch?v=WQeoO7MI0Bs'))
# capture = cv2.VideoCapture(0)
# capture.set(3,1280)
# capture.set(4,720)



# while True:
#     success,frame=capture.read()
#     cv2.imshow("OpenCV",frame)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break