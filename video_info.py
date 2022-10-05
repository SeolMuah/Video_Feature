import cv2

file_path = "/data2/maseol/Charades/Charades_v1/6HT0J.mp4"

cap = cv2.VideoCapture(file_path)

if not cap.isOpened() :
    print("Could not open : ", file_path)
    # exit(0)

len = cap.get(cv2.CAP_PROP_FRAME_COUNT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print("Frame Count : ", len)
print("Frame width : ", width)
print("Frame height : ", height)
print("FPS : ", fps)

