def add(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum
        
def subtract(nums):
    sum = nums[0]
    sum -= nums[1]
    return sum
    
def multiply(nums):
    sum = nums[0]
    sum *= nums[1]
    return sum
    
def division(nums):
    sum = nums[0]
    sum /= nums[1]
    return sum

print('1. Sum \n2. Subtract \n3. Multiply \n4. Divide')
op = int(input('What operation do you want to do? '))
nums = (float(input('\nType the first number: ')), float(input('\nType the second number: ')))
if op == 1:
    result = add(nums)
elif op == 2:
    result = subtract(nums)
elif op == 3:
    result = multiply(nums)
elif op == 4:
    result = division(nums)
    
print(result)