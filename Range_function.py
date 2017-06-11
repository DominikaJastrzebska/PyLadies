def range_function(*args):
    if len(args) == 1:
        begin = 0
        end = args[0]
        step = 1
    elif len(args) == 2:
        begin = 0
        end = args[0]
        step = args[1]
    else:
        begin = args[0]
        end = args[1]
        step = args[2]

    range_list = []
    while begin < end:
        range_list.append(begin)
        begin+=step
    return range_list

print(range_function(5))
        
    
