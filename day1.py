# Given A list of numbers find if two numbers(pair) exists such that sum of Numbers is equal to N
# For example List = [5,-2,10,4,6,3,-6,15,1], N = 11 Answer would be 5,6 and other's

# O(n^2) Time Complexity || O(1) space Complexity
def func1(list_num, target_num):
    for i in range(0, len(list_num)):
        first_num = list_num[i]
        for j in range(i + 1, len(list_num)):
            second_num = list_num[j]
            if first_num + second_num == target_num:
                print('(' + str(first_num) + ', ' + str(second_num) + ')')
                return first_num, second_num
    print("No Common Pair's Found")
    return []


# O(n) Time Complexity || O(n) space Complexity
def func2(list_num, target_num):
    dict_of_num = {}
    for i in list_num:
        if target_num - i in dict_of_num:
            print('(' + str(target_num-i) + ', ' + str(i) + ')')
            return target_num-i, i
        else:
            dict_of_num[i] = True
    print("No Common Pair's Found")
    return []

# O(nlog(n)) Time Complexity || O(1) space Complexity
def func3(list_num, target_num):
    list_num.sort()
    left_ptr = 0
    right_ptr = len(list_num) - 1
    while True:
        if list_num[left_ptr] + list_num[right_ptr] == target_num:
            print('(' + str(list_num[left_ptr]) + ', ' + str(list_num[right_ptr]) + ')')
            return list_num[left_ptr], list_num[right_ptr]

        elif list_num[left_ptr] + list_num[right_ptr] > target_num:
            right_ptr -= 1

        elif list_num[left_ptr] + list_num[right_ptr] < target_num:
            left_ptr += 1
    print("No Common Pair's Found")
    return []

#### Testing the Functions ###
list_num1 = [1,3,4,6,2,-1,5,6,14]
list_num2 = [1,9,6,2,-1,5,6,1,-9,15]
func3(list_num1,133)