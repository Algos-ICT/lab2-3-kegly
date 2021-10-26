import random

def binary_search(x, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
	    center = (left+right) // 2
    if arr[center]<x:
	    left = center+1
    elif arr[center]>x:
	    right = center-1
    else:
	    return center
    return -1

def find_elements_in_array(find_in, find_what):
	f = open('output.txt', 'w')
	for i in range(len(find_what)):
	    f.write(' ' + str(binary_search(find_what[i], find_in)))
	f.close()

a = [random.randint(1, 10 ** 9) for i in range(100000)]
f = open('input.txt', 'w')
f.write(str('100000\n'))
for i in a:
	f.write(str(i) + ' ')
	f.write('\n')
b = [random.randint(1, 10 ** 9) for i in range(100000)]

f.write(str('100000\n'))
for i in b:
    f.write(str(i) + ' ')
f.close()




f = open('input.txt', 'r')
n = f.readline()
a = list(map(int, (f.readline().split())))
a.sort()
k = f.readline()
b = list(map(int, (f.readline().split())))
f.close()

find_elements_in_array(a, b)