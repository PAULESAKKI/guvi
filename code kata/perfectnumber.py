a=int(input())
s=0
for i in range(1,a):
  if(a%i==0):
    s=s+i
if(a==s):
  print("it is a perfect number")
else:
  print("not")
