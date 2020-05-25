import time
from random import randint
def insertion_sort(arr):#codes from the lecture
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur
def selection_sort(arr):#see explanation in the writeup
    for k in range(len(arr)):
        j = k
        minindex = j
        while j < len(arr):
                if arr[j] < arr[minindex]:
                    minindex = j
                j = j + 1
        a = arr[minindex]
        arr[minindex] = arr[k]
        arr[k] = a
    return arr
def insertion_sort_timing(arr):#The two timing functions are written to simplify timings for each sorting algorithms. Each runs the sorting function and the timing codes. Then, they return the time difference between start and end of the process.
    start = time.process_time()
    insertion_sort(arr)
    end = time.process_time()
    return end-start
def selection_sort_timing(arr):
    start = time.process_time()
    selection_sort(arr)
    end = time.process_time()
    return end-start


if __name__ == '__main__':

    arr1 = [i for i in range(1000)]#array1 to array 5 are increasing arrays for timing of insertion sort
    arr2 = [i for i in range(2500)]
    arr3 = [i for i in range(5000)]
    arr4 = [i for i in range(7500)]
    arr5 = [i for i in range(10000)]
    print('Increasing Array of length 1000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr1)))#Results returned from timing functions are formatted and printed. Same for all printing codes below.
    print('Increasing Array of length 2500 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr2)))
    print('Increasing Array of length 5000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr3)))
    print('Increasing Array of length 7500 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr4)))
    print('Increasing Array of length 10000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr5)))
    arr6 = [i for i in range(1000)]#arr6 to arr10 are increasing arrays for timing of selection sort.
    arr7 = [i for i in range(2500)]
    arr8 = [i for i in range(5000)]
    arr9 = [i for i in range(7500)]
    arr10 = [i for i in range(10000)]
    print('Increasing Array of length 1000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr6)))
    print('Increasing Array of length 2500 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr7)))
    print('Increasing Array of length 5000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr8)))
    print('Increasing Array of length 7500 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr9)))
    print('Increasing Array of length 10000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr10)))
    arr11 = [i for i in range(999,-1,-1)]#arr11 to arr15 are decreasing arrays for timing of insertion sort.
    arr12 = [i for i in range(2499,-1,-1)]
    arr13 = [i for i in range(4999,-1,-1)]
    arr14 = [i for i in range(7499,-1,-1)]
    arr15 = [i for i in range(9999,-1,-1)]
    print('Decreasing Array of length 1000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr11)))
    print('Decreasing Array of length 2500 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr12)))
    print('Decreasing Array of length 5000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr13)))
    print('Decreasing Array of length 7500 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr14)))
    print('Decreasing Array of length 10000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr15)))
    arr16 = [i for i in range(999,-1,-1)]#arr16 to arr20 are decreasing arrays for timing of selection sort.
    arr17 = [i for i in range(2499,-1,-1)]
    arr18 = [i for i in range(4999,-1,-1)]
    arr19 = [i for i in range(7499,-1,-1)]
    arr20 = [i for i in range(9999,-1,-1)]
    print('Decreasing Array of length 1000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr16)))
    print('Decreasing Array of length 2500 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr17)))
    print('Decreasing Array of length 5000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr18)))
    print('Decreasing Array of length 7500 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr19)))
    print('Decreasing Array of length 10000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr20)))

    arr21 = [None for i in range(1000)]#arr21 to arr25 are random arrays for insertion sort timing. Empty arrays are created before being populated with random integers.
    for i in range(1000):
        arr21[i] = randint(0,1000000)
    arr22 = [None for i in range(2500)]
    for i in range(2500):
        arr22[i] = randint(0,1000000)
    arr23 = [None for i in range(5000)]
    for i in range(5000):
        arr23[i] = randint(0,1000000)
    arr24 = [None for i in range(7500)]
    for i in range(7500):
        arr24[i] = randint(0,1000000)
    arr25 = [None for i in range(10000)]
    for i in range(10000):
        arr25[i] = randint(0,1000000)
    arr26 = [None for i in range(1000)]#Creating array with same elements as arrays#21 to #25 by populating empty arrays with elements from arr21 to arr25.
    for i in range(1000):
        arr26[i] = arr21[i]
    arr27 = [None for i in range(2500)]
    for i in range(2500):
        arr27[i] = arr22[i]
    arr28 = [None for i in range(5000)]
    for i in range(5000):
        arr28[i] = arr23[i]
    arr29 = [None for i in range(7500)]
    for i in range(7500):
        arr29[i] = arr24[i]
    arr30 = [None for i in range(10000)]
    for i in range(10000):
        arr30[i] = arr25[i]
    print('Random Array of length 1000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr21)))
    print('Random Array of length 2500 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr22)))
    print('Random Array of length 5000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr23)))
    print('Random Array of length 7500 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr24)))
    print('Random Array of length 10000 Insertion timing: ' + '{:.6f}'.format(insertion_sort_timing(arr25)))
    print('Random Array of length 1000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr26)))
    print('Random Array of length 2500 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr27)))
    print('Random Array of length 5000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr28)))
    print('Random Array of length 7500 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr29)))
    print('Random Array of length 10000 Selection timing: ' + '{:.6f}'.format(selection_sort_timing(arr30)))
