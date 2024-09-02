from time import sleep

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
query = 6


def linear_search():
    for num in range(len(nums)):
        if nums[num] == query:
            print('index is', num)
            return
    print('not in list')


def binary_search():
    low = 0
    high = len(nums) - 1
    steps = 0

    while low <= high:
        middle = (low + high) // 2
        middle_num = nums[middle]

        steps += 1

        if middle_num > query:
            high = middle - 1
        elif middle_num < query:
            low = middle + 1
        elif middle_num == query:
            return print(f'query is at index {middle} and took {steps} steps')
    print('not in list')


if __name__ == '__main__':
    binary_search()
