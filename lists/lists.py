my_unique_list = []

my_leftovers = []

def add_item(value):
    if value not in my_unique_list:
        my_unique_list.append(value) 
        return True
    else:
        my_leftovers.append(value)
        return False

print(my_unique_list)

add_item('test')
add_item('test')
add_item('york')
add_item('york')
add_item('york')

print('unique', my_unique_list)
print('leftovers', my_leftovers)
