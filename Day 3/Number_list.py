def Num_list():

    new_list = []

    for i in range (5):
        i = int(input("Enter the numbers: "))
        new_list.append(i)
        i+=1
    print(new_list)

    sum_list = sum(new_list)
    print(sum_list)
    max_list = max(new_list)
    print(max_list)
    min_list = min(new_list)
    print(min_list)
    count = len(new_list)
    avg = sum_list/ count
    print(avg)
    new_list.sort()
    print(new_list)

Num_list()
