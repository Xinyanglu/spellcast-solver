import engine
import imageprocess
import PyQt5


def main():
    imageprocess.findBoard(image=imageprocess.getImageFromClipboard())
    
if __name__ == "__main__":
    main()
