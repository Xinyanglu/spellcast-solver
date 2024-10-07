import Engine
import ImageProcess
import PyQt5


def main():
    ImageProcess.findBoard(image=ImageProcess.getImageFromClipboard())
    
if __name__ == "__main__":
    main()
