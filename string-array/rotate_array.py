'''
>>> n = 7
>>> k = 3
>>> arr = list(range(1, n+1))
>>> arr
[1, 2, 3, 4, 5, 6, 7]
>>> rotate(arr, k)
[5, 6, 7, 1, 2, 3, 4]
>>> rotate(arr, 8)
[]
'''
def rotate(array, k):
    if k > len(array):
        k = k % len(array)
    return array[k+1:] + array[:k+1]

if __name__ == '__main__':
    print(rotate(list(range(10), 5)))
