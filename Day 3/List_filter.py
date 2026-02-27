def list_filter():

    num_list = []
    for i in range(10):
        num = int(input(f"Enter your number {i+1} to create a list: "))
        num_list.append(num)
        i = i+1
        print(num_list)
    
    even_list = [n for n in num_list if n%2 == 0]
    odd_list = [n for n in num_list if n%2 != 0]
    max_list = [n for n in num_list if n>50]

    print(f"the original list is {num_list}")
    print(f"the even number list is {even_list}")
    print(f"The numbers greater than 50 are: {max_list}")
    print(f"The odd number list is: {odd_list}")

list_filter()