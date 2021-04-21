# to prove that binary search is faster than naive (one-at-a-time) search

def naive_search(l,target):
    for i in range(len(l)): #ie, every index
        if l[i] == target: # if that index spot in the list contains the target number ...
            return i        # return that index spot (easy enough)
    return -1               # if it's not there, return -1; we went through the entire list.

# you can take advantage of how the list is sorted
def binary_search(l, target, low=None, high=None):  # the lowest and highest indices we search
    # example l == [1,3,5,10,12]                    # note that low and high are enabled terms for lists.
    if low is None:
        low = 0  # ... so that it is the lowest possible index we could check
    if high is None:
        high = len(l) - 1  # ... here, obviously the highest possible index (that's why it's - 1)

    midpoint = (low + high) // 2 # add up lowest and highest indices and divide by 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, search, low, midpoint-1)  # you recursively chop it in half and try it again
    else: # meaning, target > l[midpoint]
        return binary_search(l,search, midpoint+1, high)


