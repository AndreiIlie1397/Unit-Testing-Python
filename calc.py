num1 = input("Enter first number ")
num2 = input("Enter second number ")
op = input ("Enter operator or third number ")
list = []

def add (x,y):
    return x + y

def sub (x,y):
    return x - y

def multi (x,y):
    return x * y

def div (x,y):
    return x / y

def mod(x, y):
    if x % y == 0:
        return True
    else:
        return False
def equal(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return True

def calculation(x,y,z):
    answer = x + y + z + "="
    return answer

def split(input_list):
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]

def merge_sorted_lists(list_left, list_right):

    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left

    index_left = index_right = 0
    list_merged = []
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            list_merged.append(list_right[index_right])
            index_right += 1

        if index_right == len(list_right):
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            list_merged += list_right[index_right:]
            break

    return list_merged

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        return merge_sorted_lists(merge_sort(left), merge_sort(right))

if op == "+":
    print(calculation(num1,op,num2), add(float(num1),float(num2)))
elif op == "-":
    print(calculation(num1,op,num2), sub(float(num1),float(num2)))
elif op == "*":
    print(calculation(num1,op,num2), multi(float(num1), float(num2)))
elif op == "/":
    print(calculation(num1,op,num2), div(float(num1), float(num2)))
elif op == "%":
    print(mod(float(num1), float(num2)))
elif op == "?":
    print(equal(float(num1), float(num2)))
else:
    list.append(float(num1))
    list.append(float(num2))
    list.append(float(op))
    print("Sorted numbers: ", merge_sort(list))

