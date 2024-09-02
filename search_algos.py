from time import sleep

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
query = 6


def linear_search():
    for num in range(len(nums)):
        if nums[num] == query:
            print('index is', num)
            return
    print('not in list')


if __name__ == '__main__':
    linear_search()
