from functools import reduce


numbers = [1, 2, 3]
result = map(lambda x: x * 2, numbers)
print(list(result))




nums = [4, 5, 6]
result = map(lambda x: x + 1, nums)
print(list(result))




nums = [1,2,3,4,5]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))




nums = [10,15,20]
result = filter(lambda x: x > 12, nums)
print(list(result))





nums = [1,1,1]
result = reduce(lambda x,y: x + y, nums)
print(result)




nums = [3,4]
print(list(map(lambda x: x*3, nums)))





nums = [2,4,6]
print(list(filter(lambda x: x>3, nums)))





nums = [5,5]
print(reduce(lambda x,y: x+y, nums))





print(list(map(lambda x: x+10, nums)))





nums = [9,10,11]
print(list(filter(lambda x: x>9, nums)))