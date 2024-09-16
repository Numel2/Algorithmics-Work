from time import sleep
from random import choice

nums = [12, 3, 2, 4, 5, 6, 7, 8, 9, 10, 11, 1]
query = 12

target = 'apple'
sentence = ['apple', 'bruh', 'hello', 'world', 'monkey', 'donkey', 'aaron', 'clock', 'chair', 'piano', 'person',
            'happy']
array = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0


def linear_search():
    for num in range(len(nums)):
        if nums[num] == query:
            print('index is', num)
            return
    print('not in list')


def linear_search_string():
    for word in range(len(sentence)):
        if sentence[word].lower() == target:
            return print(f'index is {word}, took {word + 1} steps')
    print('not in list')


def linear_search_recursion(index):
    if len(sentence) == 0:
        print('not in list')
        return
    elif sentence[index] == target:
        print(f'index at {index}')
        return
    else:
        linear_search_recursion(index + 1)


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
            return print(f'query is at index {first_occurrence(middle)} and took {steps} steps')
    print('not in list')


def first_occurrence(middle):
    while True:
        if nums[middle] == nums[middle - 1]:
            middle -= 1
        else:
            return middle


def binary_search_recursive(lower, higher, array, target):
    if higher >= lower:
        mid = (lower + higher) // 2

        if array[mid] == target:
            return print(f'it is in index {mid}')
        elif array[mid] > target:
            binary_search_recursive(lower, higher - 1, array, target)
        elif array[mid] < target:
            binary_search_recursive(lower + 1, higher, array, target)


def binary_search_string():
    sorted_sentence = sorted(sentence)
    low = 0
    high = len(sorted_sentence) - 1
    steps = 0

    while low <= high:
        middle = (low + high) // 2
        middle_word = sorted_sentence[middle]
        steps += 1

        if middle_word > target:
            high = middle - 1
        elif middle_word < target:
            low = middle + 1
        elif middle_word == target:
            return print(f'target is at index {middle} and took {steps} steps')
    print('not in list')


def insertion_sort():
    x = nums[len(nums) - 1]
    print(x)
    while True:
        if x < nums[x - 1] and x != -1:
            a, b = nums.index(nums[x]), nums.index(nums[x - 1])
            nums[b], nums[a] = nums[a], nums[b]
            print(nums)
            x -= 1
        if x > nums[x - 1]:
            x -= 1
            print(nums)
        elif x == nums[0]:
            print(nums)
            return


hill1 = [1, 3, 4, 2, 1, 2, 1, 3, 2, 4, 5, 6, 4, 3, 2, 0]


def search_left(heights, i):
    while i > 0 and heights[i - 1] >= heights[i]:
        i = i - 1
    return i


def search_right(heights, i):
    while i < len(heights) - 1 and heights[i + 1] >= heights[i]:
        i = i + 1
    return i


def hill_climbing(heights, i):
    if i > 0 and heights[i - 1] > heights[i]:
        x = search_left(heights, i - 1)
        print(x)
    else:
        y = search_right(heights, i)
        print(y)


def exhaustive_search(heights):
    best_value = float('-inf')
    best_index = -1

    for i in range(len(heights)):
        if heights[i] > best_value:
            best_value = heights[i]
            best_index = i

    return print(best_index)


if __name__ == '__main__':
    exhaustive_search(hill1)
