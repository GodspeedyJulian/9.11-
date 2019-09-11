UpperCaseLetters = 0
Digits = 0
UserID = input("Your User ID: ")
for i in range(len(UserID)):
    if 65<=ord(i)<=90:
        upercase += 1
    elif 0 <=int(i)<= 9:
        digit += 1
if upercase == 3 and digit == 4:
    print('valid user ID')
else:
    print('invalid user ID')
