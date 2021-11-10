# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
# 1) Store d elements in a temp array
#    temp[] = [1, 2]
# 2) Shift rest of the arr[]
#    arr[] = [3, 4, 5, 6, 7, 6, 7]
# 3) Store back the d elements
#    arr[] = [3, 4, 5, 6, 7, 1, 2]


# Function to left rotate arr[] of size n by d*/
def left_rotate(arr, d, n):
    for i in range(d):
        temp = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = temp


# utility function to print an array */
def print_array(arr, size):
    for i in range(size):
        print(arr[i], end=" ")


_arr = [1, 2, 3, 4, 5, 6, 7]
left_rotate(_arr, 2, 7)
print_array(_arr, 7)
