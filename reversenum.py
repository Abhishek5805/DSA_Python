num=(input("Enter a number: "))


if len(num)==4 and num.isdigit():
    rev_num=num[::-1]
    print(rev_num)

else:
    print("Please enter a valid 4-digit number.")

if rev_num==num[::-1]:
    print("yes, reversed number is true")