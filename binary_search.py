# to prove that binary search is faster than naive (one-at-a-time) search

def naive_search(l,target):
    for i in range(len(l)): #ie, every index
        if l[i] == target: # if that index spot in the list contains the target number ...
            return i        # return that index spot (easy enough)
    return -1               # if it's not there, return -1; we went through the entire list.

# def binary_search
