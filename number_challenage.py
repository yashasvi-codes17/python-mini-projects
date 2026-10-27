print("----------number challenage----------")
fix_number=25
attempts=0
while True:
    num=int(input("please enter the number bw 1 and 50"))
    if num<1 or num>50:
        print("pleasr enter the number btw 1 and 50")
        continue
    attempts=attempts+1
    if num==fix_number:
        print("\ncongratulations....")
        print(f"you found the number in {attempts} attempts...")
    elif num<fix_number:
        print("too low!!")
    else:
        print("too high!!")
    print("game over!")                
