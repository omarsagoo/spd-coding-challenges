# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def num_step_counter(num):
    steps = 0
    while num != 0:
        if num & 1:
            num -= 1
        elif num & 1 == 0:
            num = num // 2
        steps += 1
    return steps
        
print(num_step_counter(14))