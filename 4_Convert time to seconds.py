print("Please enter the time: ")



x = int(input("hour:"))
y = int(input("minute:"))
z = int(input("second:"))


print("Time:" , x ,":", y ,":", z ,)
sec=int(x)*3600 + int(y)*60+ int(z)

print("Converted time is :" , sec ,"second")