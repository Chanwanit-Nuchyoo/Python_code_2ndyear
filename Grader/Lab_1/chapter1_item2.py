h, w = input("Enter your High and Weight : ").split()

BMI = float(w) / (float(h)**2)

if BMI >= 30:
    print("Fat")
elif BMI >= 25:
    print("Getting Fat")
elif BMI >= 23:
    print("More than Normal Weight")
elif BMI >= 18.50:
    print("Normal Weight")
else:
    print("Less Weight")
