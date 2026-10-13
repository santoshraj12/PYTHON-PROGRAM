a=int(input("Enter the number:-"))
r=a%10
s=0
s+=r
a//=10
r=a%10
s+=r
a//=10
s+=a
print(s)