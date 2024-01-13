n = int(input(" Lotfan Yek Adad Entekhab Konid:"))

a = 1  
b = 1  
i = 2  

if n == 0:
    print("Adad Bozorgtar Az 0 Entekhab Konid")

elif n == 1:
    print(a)

elif n == 2:
    print(a)
    print(b)

elif n >= 3:
    print(a)
    print(b)

    while i <=n :
        a , b = b , a+b
        i=i+1
        print(b)