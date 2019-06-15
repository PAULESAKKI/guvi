t = int(input())
 
f= 0
s = 1
print(f, ",", s, end=", ")
 
for i in range(2, t):
	next = f + s
	print(next, end=", ")
 
	f = s
	s = next
