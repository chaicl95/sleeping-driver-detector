import os
import tkinter
import interface
from camera import Camera


def main():
    app = interface.App(tkinter.Tk(), os.path.join(os.path.dirname(__file__), "../assets/best.onnx"))
    app.start()
    return

if __name__ == "__main__":
    main()
