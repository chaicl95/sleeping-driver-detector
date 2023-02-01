import os
import tkinter
import interface
from camera import Camera


def main():
    app = interface.App(tkinter.Tk(), os.path.join(os.path.dirname(__file__), "../assets/ssd_resnet101_v1_fpn_640x640_coco17_tpu-8/saved_model"), 640, 640)
    app.start()
    return

if __name__ == "__main__":
    main()
