a=int(input())
s=0
temp=a
while(temp>0):
  dig=temp%10
  s=s+dig**3
  temp=temp//10
if(a==s):
  print("it is an amstrong")
else:
  print("not")
