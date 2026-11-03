attempt_1007 = 1
MAX_ATTEMPS_1007 = 3
correct_pin_1007 = "1234"
pin_1007 = input("Enter PIN: ")


while pin_1007 != correct_pin_1007 and attempt_1007 < MAX_ATTEMPS_1007:
    print("Incorrect PIN.")
    pin_1007 = input("Enter PIN: ")
    attempt_1007 += 1

if pin_1007 == correct_pin_1007:
    print("Access granted")
else:
    print("Account locked")

        


