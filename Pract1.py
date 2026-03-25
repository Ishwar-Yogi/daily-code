n = int(input("Enter a number: "))
temp = n
pd=0

while n>0:
    digit = n%10 
    pd = pd*10 + digit
    n = n//10

if pd == temp :
    print("Palindrome")
else:
    print("Not Palindrome")