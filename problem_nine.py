#  Run rate for ODI mathch

target = int(input("Enter the target run:"))
current_run = int(input("Enter the Current run:"))
current_over = input("Enter the current over:")
def Runrate(run,over,target):
    Over = over.split(".")
    ball = int(Over[0])*6 + int(Over[1])
    bal_left = 300-ball
    runleft = target - run
    CurrR =(run/ball)*6
    ReqR = (runleft/bal_left)*6
    print("Current run rate:",round(CurrR,3))
    print("Requried run rate:",round(ReqR,3))

Runrate(current_run,current_over,target)


