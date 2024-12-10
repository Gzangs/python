from gui1 import *


def main():
    window = Tk()
    window.title('Project 1')
    window.geometry('400x300')
    window.resizable(False, False)

    VotingApp(window)
    window.mainloop()


if __name__ == '__main__':
    main()
