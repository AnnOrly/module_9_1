def apply_all_func(int_list, *functions):
    resalts = {}
    for func in functions:
        resalts[func.__name__] = func(int_list)
    return resalts

def add(int_list):
    int_list.add()
    return

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))