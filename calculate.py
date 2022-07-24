import sys

allowed_operations = ['+', '-', '/', '*','%']
if len(sys.argv) != 4 and len(sys.argv) !=2:
    print('Arg len should be 4 or dont space')
    sys.exit()

def calc(left_operand,operation,right_operand):
    
    if operation not in allowed_operations:
        print('Operation is not allowed')
        sys.exit()
    try:
        left_operand = int(left_operand)
        right_operand = int(right_operand)
    except ValueError:
        print('Left and Right operands must be int')
        sys.exit()

    if operation == '/' and right_operand == 0:
        print('Division by zero is not allowed')
        sys.exit()
    
    if operation == '%' and right_operand ==0:
        print('Division by zero is not allowed')
        sys.exit()

    match operation:
        case '*':
            print(left_operand * right_operand)
        case '+':
            print(left_operand + right_operand)
        case '/':
            print(left_operand / right_operand)
        case '-':
            print(left_operand - right_operand)
        case '%':
            print(left_operand % right_operand)
   

if len(sys.argv) == 4:
    try:
        left_operand = int(sys.argv[1])
        right_operand = int(sys.argv[3])
    except ValueError:
        print('Left and Right operands must be int')
        sys.exit()
        
    operation = sys.argv[2] 
    if operation not in allowed_operations:
       print('Operation is not allowed')
       sys.exit()

    
    calc(left_operand,operation,right_operand)
    

if len(sys.argv) ==2:
    for item in allowed_operations:
        result = sys.argv[1].split(item)
        if len(result)==2:
            operation = item
            break
    left_operand = result[0]
    right_operand = result[1]
    calc(left_operand,operation,right_operand)
    
    
        

    
    