import cv2
import pytesseract
import multiprocessing as mp

# Path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def process_video(video_path, start_time=0, run_for_10_sec=True, step=30):
    vidcap = cv2.VideoCapture(video_path)

    fps = vidcap.get(cv2.CAP_PROP_FPS)  # Frames per second
    start_frame = int(start_time * fps)  # Converting start time to start frame
    end_frame = start_frame + 10 * int(fps) if run_for_10_sec else int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_texts = []

    for frame_num in range(start_frame, end_frame, step):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        success, image = vidcap.read()
        if success:
            frame_texts.append(extract_text_from_frame(image))

    vidcap.release()

    return "\n".join(frame_texts)

def write_text_to_file(output_file_path, text):
    with open(output_file_path, 'a', encoding='utf-8') as f:  # 'a' to append to the file
        f.write(text)

# Usage
video_path = r'C:\Users\Shubham Tyagi\Downloads\Shikwa.mp4'
output_file_name = video_path.split("\\")[-1].split(".")[0] + "-Txt.txt"
output_file_path = r'C:\Users\Shubham Tyagi\Desktop\\' + output_file_name

start_time = 0  # Start at the 0th second
run_for_10_sec = True  # Run for 10 seconds

vidcap = cv2.VideoCapture(video_path)
total_video_length_sec = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT) / vidcap.get(cv2.CAP_PROP_FPS))

# Run the loop until the total video length is reached
for i in range(start_time, total_video_length_sec, 10 if run_for_10_sec else total_video_length_sec):
    print(f"Processing from second {i} to second {i+10 if run_for_10_sec else total_video_length_sec}")  # Debugging
    text = process_video(video_path, i, run_for_10_sec)
    print("Writing to file...")  # Debugging
    write_text_to_file(output_file_path, text)
