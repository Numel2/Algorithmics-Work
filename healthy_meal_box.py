from random import choice


def simulation():
    num = ['1', '2', '3', '4', '5']
    times = 0
    num_list = []
    while len(num_list) < 5:
        num_list.append(choice(num))
        num_list = list(dict.fromkeys(num_list))
        times += 1
    if len(num_list) == 5:
        print(num_list)
        print(f'It took {times} boxes')


if __name__ == '__main__':
    for i in range(10):
        simulation()
