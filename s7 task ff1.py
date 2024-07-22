def fabonacci(n):
   if n==1:      
     return 0
   if n==2:      
      return 1
   return fabonacci(n-1)+fabonacci(n-2)
print(fabonacci(7))