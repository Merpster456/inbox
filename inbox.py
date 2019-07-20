import sys
import smtplib
from appJar import gui

app = gui("SMTP Server","400x200")
usr = ""
pwd = ""

def intro():

    print("Probably the simplest SMTP server you ever will come across")
    print("\nThis is only compatible with GMAIL accounts!!\n")
    print("You're going to need to login to your account and give who you are sending this to and the message")
    print("After filling out your account details just click send and you will be on your way!")


def startapp():

    app.addLabel("title", "Inbox")
    app.setLabelBg("title", "gray")

    app.addLabelEntry("Email")
    app.addLabelSecretEntry("Password")

    app.addButtons(["Submit", "Exit"], press)

    app.go()

def press(button):

    global usr
    global pwd

    while button != "Exit":

        usr = app.getEntry("Email")
        pwd = app.getEntry("Password")

        if button == "Submit":

            app.stop()
            break

    app.stop()
    sys.exit(0)


def main():

    global usr
    global pwd

    intro()
    startapp()

    #server = smtplib.SMTP_SSL("smtp.gmail.com", 445)
    try:
        print(usr, pwd)

    except:
        print("It failed")

if __name__ == '__main__':

    main()
