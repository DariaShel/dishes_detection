from ultralytics import YOLO
import cv2

def process_video(model_path, video_path):
    model = YOLO(model_path, task='detect')
    cap = cv2.VideoCapture(video_path)
   
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    output_path = 'output.mp4'
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (height, width))
    while cap.isOpened():
        success, frame = cap.read()

        if success:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            results = model(frame)
            annotated_frame = results[0].plot()
            out.write(annotated_frame)
            cv2.imshow("YOLOv11n", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

video_path = "PATH_TO_VIDEO"
model_path = "PATH_TO_BEST_CHECKPOINT" 
process_video(model_path, video_path)