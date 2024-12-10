from gui2 import *


def main():
    window = Tk()
    window.title('Project 2')
    window.geometry('500x600')
    window.resizable(False, False)

    GradeApp(window)
    window.mainloop()


if __name__ == '__main__':
    main()
