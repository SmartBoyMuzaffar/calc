from art import *


tprint("Calculator")
print()
print()
print()
print("code writed by>> : Muzaffar Sharodiddinov")
print()
print()
a=int(input("1-son>> :"))
c=input("belgi '+ - * / ^ % ...' >> :")
b=int(input("2-son>> :"))

if c=='+':
	print(a+b)
elif c=='-':
	print(a-b)
elif c=='*':
	print(a*b)
elif c=='/':
	print(a/b)
elif c=='^':
	print(a**b)
else:
	print(a%b)
