import cv2 as cv
from ultralytics import YOLO
import supervision as sv

from utils.downloader import download_video_if_needed
from utils.constants import IMAGE_POINTS, WORLD_POINTS
from config.settings import *

from modules.mapping import Cam2WorldMapper
from modules.speedometer import Speedometer
from modules.annotators import get_annotators
from zone.zone_trigger import create_zone

def main():
    source_video = download_video_if_needed()
    video_info = sv.VideoInfo.from_video_path(source_video)
    FPS = video_info.fps
    WIDTH = round(video_info.width / 32) * 32
    HEIGHT = round(video_info.height / 32) * 32

    cap = cv.VideoCapture(source_video)

    # Setup
    mapper = Cam2WorldMapper()
    mapper.find_perspective_transform(IMAGE_POINTS, WORLD_POINTS)
    zone = create_zone()
    annotators = get_annotators(FPS)
    speedometer = Speedometer(mapper, FPS, MPS_TO_KPH)
    model = YOLO(MODEL_PATH)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = model.track(
            frame,
            classes=CLASSES_TO_TRACK,
            conf=CONFIDENCE_THRESHOLD,
            imgsz=(HEIGHT, WIDTH),
            persist=True,
            verbose=False,
            tracker="bytetrack.yaml"
        )

        detections = sv.Detections.from_ultralytics(result[0])
        detections = detections[zone.trigger(detections=detections)]
        trace_ids = detections.tracker_id
        labels = []

        for trace_id in trace_ids:
            trace = annotators["trace"].trace.get(trace_id)
            speedometer.update_with_trace(trace_id, trace)
            speed = speedometer.get_current_speed(trace_id)
            labels.append(f"#Vehicle Id:{trace_id} Speed:{speed} km/h")

        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.cvtColor(frame_gray, cv.COLOR_GRAY2BGR)

        frame = annotators["bbox"].annotate(frame, detections)
        frame = annotators["trace"].annotate(frame, detections)
        frame = annotators["label"].annotate(frame, detections, labels=labels)

        cv.imshow("Vehicle Speed Estimation - YOLOv11", frame)
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
