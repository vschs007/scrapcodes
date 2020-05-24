def swap_values(user_val1,user_val2):
    temp=user_val1
    user_val1=user_val2
    user_val2=temp
    return (user_val1,user_val2)

value1=int(input())
value2=int(input())
print(*swap_values(value1,value2),sep=' ')