
def max_sub(a):
    temp_sum = a[0]
    max_sum = temp_sum
    for item in a[1:]:
        temp_sum = max(temp_sum + item, item)
        max_sum = max(temp_sum, max_sum)
    return max_sum

arr = [-3, -4, -5]
sum = max_sub(arr)
print(sum)