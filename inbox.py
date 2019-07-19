import smtplib
import appJar

def intro():

    print("Probably the simplest SMTP server you ever will come across")
    print("\nThis is only compatible with GMAIL accounts!!\n")
    print("You're going to need to login to your account and give who you are sending this to and the message")
    print("After filling out your account details just click send and you will be on your way!")


class sending:
    def __init__(self, FROM, PASS, TO, MSG):
        self.from = FROM
        self.pass = PASS
        self.to = TO
        self.msg = MSG


def main():

    intro()




if __name__ == '__main__':

    main()
