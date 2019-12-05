import sys
import smtplib
from appJar import gui

app = gui("SMTP Server","400x200")

def intro():

    print("Probably the simplest SMTP server you ever will come across")
    print("\nThis is only compatible with GMAIL accounts!!\n")
    print("You're going to need to login to your account and give who you are sending this to and the message")
    print("After filling out your account details just click send and you will be on your way!")


class sending:
    def __init__(self):
        self.usr = self.pressM
        self.Pass = PASS
        self.to = TO
        self.msg = MSG


    def startapp():

        app.addLabel("title", "Inbox")
        app.setLabelBg("title", "gray")

        app.addLabelEntry("Email")
        app.addLabelSecretEntry("Password")

        app.addButtons(["Submit", "Exit"], press)
        
        app.go()

    def press(button):

        if button == "Exit":
            app.stop()
            sys.exit(0)

        else:

            usr = app.getEntry("Email")
            pwd = app.getEntry("Password")
            return usr, pwd

def main():

    intro()
    startapp()
    
   server = smtplib.SMTP_SSL("smtp.gmail.com", 445)
   server.login()

if __name__ == '__main__':

    main()
