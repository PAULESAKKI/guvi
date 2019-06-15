d= input()
m=0
for i in range(len(d)):
  if(d[i].isdigit() or d[i].isalpha() or d[i]==""):
    continue
  else:
    m=m+1
print(m)
