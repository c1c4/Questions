num_list = []
str_num_list = []
dict_nums = {}
fib_list = []
reverse_list = []

def create_list():
    for number in range(10):
        num_list.append(number)

    print(num_list)

def convert_num_into_str():
    for number in num_list:
        str_num_list.append(str(number))
    
    print(str_num_list)

def create_dict():
    for idx, value in enumerate(num_list):
        key = str_num_list[idx]
        dict_nums[key] = value

    print(dict_nums)

def create_fib_list():
    for number in num_list:
        def calculate_fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                return calculate_fib(n - 1) + calculate_fib(n - 2)
        
        fib_list.append(calculate_fib(number))
    
    print(fib_list)


def sort_desc_fib_list():
    global reverse_list
    reverse_list = fib_list[::-1]
    print(reverse_list)


def filter_less_than_fifteen():
    less_than_fifteen_list = [number for number in reverse_list if number < 15]
    print(less_than_fifteen_list)


def create_fib_list_optimized():
    create_fib_list_optimized = []
    for number in num_list:
        def calculate_fib(n, cached = {0: 0, 1: 1}):
            if n in cached:
                return cached[n]
            else:
                cached[n] = calculate_fib(n - 1, cached) + calculate_fib(n - 2, cached)
                return cached[n]
        
        create_fib_list_optimized.append(calculate_fib(number))
    
    print(create_fib_list_optimized)

# This is another alternative to optimize the fibonacci question
# Instead call a recursive method is used a list of two elements because we need
# to know the last two elements and we want to discover next element
# so while our N is less than our counter try to find out what's is the next fibonacci sequence
def create_fib_list_optimized2():
    create_fib_list_optimized = []
    for number in num_list:
        def calculate_fib(n):
            simple_list = [0,1]
            counter = 3

            while counter <= n:
                next_fib = (n - 1) + (n - 2)
                simple_list[0] = simple_list[1]
                simple_list[1] = next_fib
                counter += 1    

            return simple_list[1] if simple_list[0] > 2 else simple_list[0]
        create_fib_list_optimized.append(calculate_fib(number))
        
    print(create_fib_list_optimized)


create_list()
convert_num_into_str()
create_dict()
create_fib_list()
sort_desc_fib_list()
filter_less_than_fifteen()
create_fib_list_optimized()
create_fib_list_optimized2()