print(" *** Wind classification ***")
wind_speed = float(input("Enter wind speed (km/h) : "))

if wind_speed >= 209.00:
    print("Wind classification is {}.".format("Super Typhoon"))
elif wind_speed >= 102.00:
    print("Wind classification is {}.".format("Typhoon"))
elif wind_speed >=56.00:
    print("Wind classification is {}.".format("Tropical Storm"))
elif wind_speed >= 52.00:
    print("Wind classification is {}.".format("Depression"))
elif wind_speed >= 0.00:
    print("Wind classification is {}.".format("Breeze"))
else:
    print("!!!Wrong value can't classify.")