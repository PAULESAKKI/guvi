a=int(input())
while(a>0):
  dig=a%10
  rem=dig%2
  a=a//10
  if(rem==0):
    print(dig)
    continue
