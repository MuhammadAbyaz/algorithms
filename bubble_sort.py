def b_sort(data: list):
    for i in range(len(data)-1):
        k = 0
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                k = 1
        if k == 0:
            return data
    return data


# Time Complexity
# f(n) = (n-2)(n-2)
# O(f(n)) = O(n^2)
