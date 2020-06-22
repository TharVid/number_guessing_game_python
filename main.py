import random
win_number= random.randint(1,10)
print(win_number)
count =1
for i in range(10):
    user_number=int(input("Enter Number Betwwen 1-10: "))
    if user_number==win_number:
        print(f"You Won in {count} times!")
        break
    elif user_number < win_number:
        print("Too Low")
        count+=1
        continue
    elif user_number > win_number:
        print("Too High")
        count+=1
        continue

