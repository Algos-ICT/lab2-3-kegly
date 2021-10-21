def merge(left, right): #слияние двух подмассивов
    global count
    res = []
    l, r = 0, 0 # количество уже записанных чисел в конечный массив
    while (l < len(left)) and (r < len(right)): # в конечный массив записываем по возрастанию числа из двух частей
        if(left[l] <=right[r]):
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
            count+= (len(left)-l)

    while (l < len(left)):
        res.append(left[l])
        l += 1
    while (r < len(right)):
        res.append(right[r])
        r += 1
    return res

def merge_sort(A):
    if(len(A) <= 1):
        return A
    middle = len(A) // 2
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left, right)


global count #количество инверсий
count=0

f=open('input.txt')
a= list(map(int, f.readline().split()))
a=merge_sort(a)
f2=open('output.txt', 'w')
f2.write(str(count))