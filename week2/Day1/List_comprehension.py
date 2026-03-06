def list_comp():

    number = [n for n in range(100)]
    square = [s**2 for s in number]
    even = [e for e in number if e%2 ==0]
    five = [f for f in number if f%5 == 0]
    odd_square = [o**2 for o in number if o%2 !=0]
    str_num = str(number)
    range_num = [r for r in range(20,50)]
    print(range_num)

list_comp()