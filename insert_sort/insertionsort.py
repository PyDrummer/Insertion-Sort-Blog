list_1 = [8,4,23,42,16,15]

def insertionsort(an_array):
    for i in range(1, len(an_array)):

        mover = an_array[i]

        follower = i-1

        while follower >= 0 and mover < an_array[follower]:
            an_array[follower+1] = an_array[follower]
            follower -= 1
        an_array[follower+1] = mover
    return an_array


# if __name__ == '__main__':
#     insertionsort(list_1)
#     for i in range(len(list_1)):
#         print(list_1[i])