# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        # check if there are empty lists, if so use first element of other list and delete first element from other list
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            del arrA[0]
        # if both lists have elements, compare first element of each list, set that element to merged[i] and delete that element from original
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            merged_arr[i] = arrB[0]
            del arrB[0]

    return merged_arr


# list1 = [1, 4, 6]
# list2 = [2, 3]
# print(merge(list1, list2))

# TO-DO: implement the Merge Sort function below USING RECURSION


list = [1, 4, 10, 6, 5, 3]


# def merge_sort(arr):
#     # TO-DO
#     if len(arr) > 1:
#         center = round(len(arr)/2)
#         arrA = arr[0:center]
#         arrB = arr[center:]
#         if len(arrA) == 1 and len(arrB) == 1:
#             arr = merge(arrA, arrB)
#         elif len(arrA) > 1 and len(arrB) == 1:
#             arr = merge(merge_sort(arrA), arrB)
#         elif len(arrA) == 1 and len(arrB) > 1:
#             arr = merge(merge_sort(arrB), arrA)
#         elif len(arrA) > 1 and len(arrB) > 1:
#             arr = merge(merge_sort(arrA), merge_sort(arrB))
#         return arr
#     else:
#         return arr

# def merge_sort(arr):
#     # TO-DO
#     center = round(len(arr)/2)
#     arrA = arr[0:center]
#     arrB = arr[center:]
#     if len(arr) <= 1:
#         return arr
#     return merge(merge_sort(arrA), merge_sort(arrB))

def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        center = round(len(arr)/2)
        arrA = arr[0:center]
        arrB = arr[center:]
        arr = merge(merge_sort(arrA), merge_sort(arrB))

    return arr


print(merge_sort(list))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
