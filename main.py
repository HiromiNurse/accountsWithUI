from logic import *


def main():
    """
    Function Opens 1 window
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()
