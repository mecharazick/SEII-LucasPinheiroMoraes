weight = float(input("Weight: "))
unities = input("(K)g or (L)bs: ").lower()
k_to_l = 2.205
if unities == 'k':
    print("Weight in Lb: " + str(weight * k_to_l))
elif unities == 'l':
    print("Weight in Kg: " + str(weight / k_to_l))
else:
    print("Invalid unit")

