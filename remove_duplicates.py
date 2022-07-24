
def remove_duplicates(array):
    print(array)
    sort_array = sorted(array)
    new_array = []
    for x in sort_array:
        if x not in new_array:
            new_array.append(x)
    print(new_array)

remove_duplicates([1,1,2])

remove_duplicates([0,0,1,1,1,2,2,3,3,4])

remove_duplicates([1,1,1,1,1,1,1,1])