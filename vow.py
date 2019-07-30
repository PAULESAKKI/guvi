a=str(input())
b=len(a)
for i in range(b):
  if(a[i]=='a' or a[i]=='e' or a[i]=='i'or  a[i]=='o'or a[i]=='u'):
    print("yes")
    break
  if(a[i]!='a' or a[i]!='e' or a[i]!='i'or  a[i]!='o'or a[i]!='u'):
    print("no")
    break


