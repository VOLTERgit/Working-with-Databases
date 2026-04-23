nums = list(map(int, input("Enter numbers: ").split()))
nums = list(set(nums))
nums.sort()

print("Second smallest:", nums[1])