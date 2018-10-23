count =1
while True:
    pin=int(input("enter a pin no:"))
    if pin ==6668:
        print("The user is valid")
        break
    else:
        print("Invalid user ")
        count+=1
        if count>3:
            print("The user is blocked and Exceeded the Limit of 3 times")
            break
        ans = int(input("press 1 continune the process: "))
        if ans == 1:
            continue
        else:
            break

