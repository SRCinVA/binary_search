# to prove that binary search is faster than naive (one-at-a-time) search

def naive_search(l,target):
    for i in range(len(l)): #ie, every index
        if l[i] == target: # if that index spot in the list contains the target number ...
            return i        # return that index spot (easy enough)
    return -1               # if it's not there, return -1; we went through the entire list.


# you can take advantage of how the list is sorted
def binary_search(l, target):
    # example l == [1,3,5,10,12]
    midpoint = (len(l)) // 2 # divide by 2 and round it down
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,search)  # you recursively chop it in half and try it again
    else: # meaning, target > l[midpoint]
        return binary_search(l,search)


