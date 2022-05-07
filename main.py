# x = 1
# y = 1
# z = 2
# n = 3

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(sum([x, y, z]) != n)

    my_list = [[x, y, z] for x in range(n) for y in range(n) for z in range(n) if sum([x, y, z]) != n]
    print(my_list)