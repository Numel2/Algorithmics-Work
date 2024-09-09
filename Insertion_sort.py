from time import sleep

nums = [6, 2, 3, 4, 5, 7, 1]


def insertion_sort():
    total = len(nums)
    steps = 1
    while True:
        x = nums[total - steps]
        print(x)
        if x < nums[x - 1] and x != -1:
            a, b = nums.index(nums[x]), nums.index(nums[x - 1])
            nums[b], nums[a] = nums[a], nums[b]
            print(nums, 'x is smaller')
            steps += 1
            return
        elif x > nums[total - steps]:
            print(nums, 'x is bigger')
            steps += 1
            return
        elif x == nums[0]:
            print(nums, 'bruh')
            return


insertion_sort()