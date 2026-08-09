def move_zeroes_one_liner(nums):
   
    return [x for x in nums if x != 0] + [0] * nums.count(0)

# Example
numbers = [0, 1, 0, 3, 12]
print(move_zeroes_one_liner(numbers))

