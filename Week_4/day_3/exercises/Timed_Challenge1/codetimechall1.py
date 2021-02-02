x = int(input('Enter the Number:')) 
list_div = []
 
#find all the divisors of x
#sum them and check if it's equal to x
#if yes ->True if not False
for i in range(1, x):
  if x % i == 0:
    list_div.append(i)
sum_list = sum(list_div)
if sum_list == x:
  print(True)
else:
  print(False) 