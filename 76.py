a2=int(input())
if(a2>1):
   for i in range (2,a2):
      if(a2%i==0):
       print("yes")
       break
   else:
      print("no")
