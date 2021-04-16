print(" "*8 +"@" +" "*3+"@")
print(" "*15 +"@")
print(" "*5 +"@")
print(" "*5 +"@")
print(" "*5 +"@")
print(" "*5 +"@" +" "*23+"@"+" "*5 +"@" +" "*1 +"@"+" "*5 +"@")
print(" "*5 +"@" +" "*31 +"@" +" "*5 +"@")
print(" "*5 +"@" +" "*20 +"@" +" "*10 +"@" +" "*5 +"@")
print(" "*5 +"@" +" "*31 +"@" +" "*5 +"@")
print(" "*5 +"@" +" "*10 +"@"+" "*15 +"@" +" "*10 +"@"*6)
print(" "*8 +"@" +" "*3+"@")
print()
print()
print()
print("code writed by>> : Muzaffar Sharodiddinov")
print()
print()
a=int(input("1-son>> :"))
c=input("belgi >> :")
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
