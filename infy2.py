x=input()
y=input()

x=set(x)
y=set(y)

z=x.difference(y)
w=x.difference(z)
a=''
for i in w:
  a+=i
print(a)
