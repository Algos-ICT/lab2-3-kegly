
def merge(left, right): #слияние двух подмассивов
    res = []
    l, r = 0, 0 # количество уже записанных чисел в конечный массив
    while (l < len(left)) and (r < len(right)): # в конечный массив записываем по возрастанию числа из двух частей
        if(left[l] < right[r]):
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
#если останутся элементы только одной какой-то части :
    while (l < len(left)):
        res.append(left[l])
        l += 1
    while (r < len(right)):
        res.append(right[r])
        r += 1
    return res

def merge_sort(A):
    if(len(A) <= 1): #если массив одноэлементный то уже делить нечего
        return A
    middle = len(A) // 2 # иначе делим на две части :
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    return merge(left, right) #сливаем части

f=open('input.txt')
a= list(map(int, f.readline().split()))
a=merge_sort(a)
count=0 #количество значений среднего элемента в отсортированном массиве
for i in range(len(a)):
    if a[i]==a[len(a)//2]:
        count+=1
f2=open('output.txt', 'w')
if count> len(a)//2 :
	f2.write('1')
else:
	f2.write('0')
	f2.write('0')