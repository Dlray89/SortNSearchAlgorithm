'''
Construct the bubble sort algorithm!
'''


def bubble_sort(arr):
    #Traverse through each element
    for i in range(len(arr)):
        #loop to compare each element
        for j in range(len(arr) - i - 1):
            #If right is greate than the left element
            if arr[j] > arr[j + 1]:
                #swapped element if condition is true
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

data = [67, 79, 2, 5, 8, 10]
bubble_sort(data)
print(data)