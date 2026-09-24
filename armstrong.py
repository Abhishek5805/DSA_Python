num=int(input())

num_str=str(num)
n=len(num_str)
result=0
for digit_char in num_str:
    digit=int(digit_char)
    result+=digit**n

if result==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")