balance =float(input("enter account balance"))
withdrawal=float(input("enter amount to withdraw"))
if withdrawal <= 0:
    print("invalid request")
elif withdrawal <=balance:
    print("withdrawal successful")
    balance = balance - withdrawal
    print ("your balance now is ", balance )
else:
    print("insufficient balance")
