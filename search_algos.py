from time import sleep

nums = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
query = 2
target = 'apple'
sentence = ['apple', 'bruh', 'hello', 'world', 'monkey', 'donkey', 'aaron', 'clock', 'chair', 'piano', 'person',
            'happy']
array = [1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]


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
    sorted(sentence)
    low = 0
    high = len(sentence) - 1
    steps = 0

    while low <= high:
        middle = (low + high) // 2

        if sentence[middle] == target:
            return print(f'it is at index {middle} took {steps} steps')
        elif ord(sentence[middle][0]) < ord(target[0]):
            steps += 1
            low = middle + 1
        elif ord(sentence[middle][0]) > ord(target[0]):
            high = middle - 1
            steps += 1


if __name__ == '__main__':
    binary_search_string()
