"""Problem 01"""

def divisor(n):
    my_list = []
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            my_list.append(i)
    len_my_list = len(my_list)
    new_my_list = []
    for i in range(len_my_list):
        if my_list[i] in  new_my_list:
            pass
        else:
            new_my_list.append(my_list[i])

    sum = 0
    for i in new_my_list:
        sum = sum + i
    print(sum)


divisor(1000)