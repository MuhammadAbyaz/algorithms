def l_search(data: list, value: any):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return None


# Time Complexity
# f(n) = n
# f(n) = O(n)
