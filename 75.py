aa=str(input())
b=list(aa)
s=len(aa)
p=""
if s%2==0:
  b[int(s/2)]="*"
  b[int(s/2-1)]="*"
else:
   b[int(s/2)]="*"
p=p.join(b)
print(p)
