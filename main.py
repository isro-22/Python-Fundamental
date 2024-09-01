# Sequential

print ("One day, a mother asked her son to buy food.\n"
       "Then, his finally went to the shop.")

# Main Program
def Buying_Something():
    print("The child asked, does it have milk (yes/no)?")
    command_A = input()

    conclusion = "Conclusion is His son come home and \nthe result is "

    if command_A == "yes":
        print("His son asked again, do you have eggs (yes/no)?")
        command_B = input()
        if command_B == "yes":
            print(conclusion + "His son bought 6 eggs and 1 bottle of milk in the end")
        else:
            print(conclusion + "His son only bought 1 bottle of milk")
    else:
        print(conclusion + "Not buying anything")

# Running Program
Buying_Something()
