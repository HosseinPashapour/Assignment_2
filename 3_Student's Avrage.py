input("Enter the name of student?  ")
print("Enter the score student")

sum = 0
score_number = 0

while 1 == 1:
    score = (input("score:"))

    if score =="exit":
        print("End")
        break

    else:
        print("Thanx.")
        score = float(score)
        sum += score
        score_number = score_number+1

avg=sum/score_number
print("The avrage:" , avg)