import solver
import imageprocess


def main():
    imageprocess.findBoard(image=imageprocess.getImageFromClipboard())
    
if __name__ == "__main__":
    main()
