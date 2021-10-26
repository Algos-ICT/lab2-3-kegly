
def Find_Maximum_Subarray(A,low,high):
    if high== low:
        return (low, high, A[low])
    else:
        mid = (low+high)//2
        leftlow, lefthigh, leftsum= Find_Maximum_Subarray(A, low, mid)
        rightlow, righthigh, rightsum= Find_Maximum_Subarray(A, mid+1, high)
        crosslow, crosshigh, crosssum = Find_Max_Crossing_Subarray(A, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return (leftlow, lefthigh, leftsum)
        elif rightsum>= righthigh and rightsum>= crosssum :
            return (rightlow, righthigh, rightsum)
        else:
            return (crosslow, crosshigh, crosssum)


def Find_Max_Crossing_Subarray(A, low, mid, high):
    leftsum= float('-inf')
    sum=0
    maxleft=0
    maxright=0
    for i in range(mid, low, -1):
        sum=sum+ A[i]
        if sum>leftsum:
            leftsum= sum
            maxleft=i
    rightsum=float('-inf')
    sum=0
    for j in range (mid+1, high):
        sum=sum+A[j]
        if sum> rightsum:
            rightsum =sum
            maxright=j
    return (maxleft, maxright, leftsum+rightsum)



A=[1,4,5]
print(Find_Maximum_Subarray(A, 0, 2))

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
