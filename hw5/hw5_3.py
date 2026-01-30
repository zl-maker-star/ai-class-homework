#******************************************************
# Zoey Lutky 9th 5 #
#******************************************************

# קלט מהירות הנהג
speed = float(input("Enter the speed in km/h: "))

# הגדרת המהירות המותרת בעיר
allowed_speed = 55

# בדיקה והשוואה
if speed > allowed_speed:
    print("Driving above the speed limit!")
elif speed < allowed_speed:
   print("You are driving below the speed limit.")

else:
    print("You are driving exactly at the speed limit.")
