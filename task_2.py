

def double_zero(array):
   
    new_array = []
    for x in array:
        new_array.append(x)
        if x==0: new_array.append(0)
    print(array)
    print(new_array)

double_zero([1,0,2,3,0,4,5,0])