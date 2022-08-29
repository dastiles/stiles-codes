balance = 1000


def send_money():
    number = int(input("enter number to send money"))
    amt = int(input("enter amount"))
    if amt > 1000:
        print("sorry you have insufficient balance")
    else:
        print(
            f"you have successfully send {1000-amt} \n your new balance is {1000-amt}")


def options():
    option = int(
        input("choose from the available (1,send money 2,recive money 3,update pin  )"))
    if option == 1:
        send_money()
