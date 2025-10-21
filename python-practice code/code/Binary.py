pos = -1
def search(list, n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l + u)
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False            
list = [4, 7, 12, 45, 99, 102, 702, 10987, 56666]
n = 10  
if search(list, n):
    print("Found at", pos + 1)
else:
    print("Not Found")            
    