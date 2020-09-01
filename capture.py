import ctypes
from idlelib.pyshell import PROCESS_SYSTEM_DPI_AWARE

import cv2
import numpy as np
import win32gui
import win32process
from PIL import ImageGrab


class Capture:

    def __init__(self, filename, name):
        self.filename = filename
        self.window_name = name
        file_extension = filename.split('.')[1]
        if file_extension == 'avi':
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        elif file_extension == 'mp4':
            self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    def capture_screen(self):
        whnd = win32gui.FindWindow(None, self.window_name)

        errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_SYSTEM_DPI_AWARE)
        print("found handle ", whnd)
        win32gui.SetForegroundWindow(whnd)
        rect = win32gui.GetWindowRect(whnd)
        winsize = win32gui.GetClientRect(whnd)
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        print("rect ", rect)
        print("client ", winsize)
        print("x = " + str(x) + " y = " + str(y) + " w = " + str(w) + " h = " + str(h))
        vid = cv2.VideoWriter(self.filename, self.fourcc, 25, (w, h))

        while True:
            # img = ImageGrab.grab(bbox=(2, 2, 1422, 1200))
            img = ImageGrab.grab(bbox=(x, y, w+x, h+y))
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            vid.write(frame)
            cv2.imshow("frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break

        vid.release()
        cv2.destroyAllWindows()


def main():
    capture = Capture("capture.mp4", "Spotify Premium")
    # capture = Capture("capture.mp4", "Task Manager")
    capture.capture_screen()


if __name__ == "__main__":
    main()
