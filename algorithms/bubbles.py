nums = [3, 9, 8, 1]

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

nums = [3, 9, 8, 1]
true = True
while true:
    true = False
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            true = True
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)