from ultralytics import YOLO
import cv2 as cv
import math
import cvzone



cls = ''



cap = cv.VideoCapture("assets/CVTest.mp4")

cap.set(3,640)
cap.set(4,480)


model = YOLO("yolo_model/yolo26n.pt")





# YOLO has 80 class
classNames = coco_classes = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat',
    'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat',
    'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
    'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
    'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse',
    'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator',
    'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]





def render_loop():
        global cls   # make the var global so we can use it in the client

        cls = None
        status, frame = cap.read()


        if not status or frame is None:
            return 3

        result = model(frame,stream=True, verbose=True) # rendering video frame by frame

        for r in result:  # looping in data from model result
            boxes = r.boxes            # r.boxes is a list of boxes data

            # looping in boxes , its has 2 2D points and confidence and class ID --> used as index for classes list
            for box in boxes:
                # box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv.rectangle(frame, (x1, y1), (x2, y2), (222, 33, 0), 2)
                # text in box
                conf = math.ceil((box.conf[0] * 100))
                cls = classNames[int(box.cls[0])]
                cvzone.putTextRect(frame, f"{cls} {conf}%", (x1, y1), 1, 2, (255, 255, 255), (222, 33, 0))

        # cv.imshow("video", frame)
        cv.waitKey(20)

        return 0













'''
for result in results:
    boxes = result.boxes  # إحداثيات البوكسات والثقة والـ Class

    # لو مستخدم موديل Segmentation:
    # masks = result.masks

    # لرسم النتائج وحفظها أو عرضها:
    annotated_frame = result.plot()  # بترجع الصورة مرسوم عليها

    cv.imshow("YOLO Result", annotated_frame)
    cv.waitKey(0)
    cv.destroyAllWindows()
'''