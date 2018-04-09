import os
import shutil
import cv2
import sys


def video_2_frames(video_file, image_dir='./image_dir/', frame_rate=10, start_frame=0):
    """convert video to images
    Args:
        video_file:video file(str)
        image_dir: Directry whitch you want to create images from vidio(str)
        frame_rate:interval of frames images(int, optinal)
        start_frame:start frame. if you want to convert video to images from the middle, use this.
    """

    # Delete the entire directory tree if it exists.
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)

    # Make the directory if it doesn't exist.
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Video to frames
    i = 0

    image_file = 'img_%s.png'
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()
        if flag == False:
            break
        if i % frame_rate == 0 and i > start_frame:
            # save a frame
            cv2.imwrite(image_dir+image_file % str(i).zfill(7), frame)
            print('Save', image_dir+image_file % str(i).zfill(7))
        i += 1

    cap.release()  # When everything done, release the capture


if __name__ == "__main__":
    file_name = sys.argv[1]
    print(file_name)
    video_2_frames(video_file=file_name)
