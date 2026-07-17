nums = list(map(int,input("Enter numbers : " ).split(",") ))
x = int(input("Enter x :  "))
i=0
while i<len(nums):
   if(nums[i]==x):
        print("found at idx ", i)
        break
   else: 
       print("cannot find")
       i +=1