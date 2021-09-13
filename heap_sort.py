import sys
from time import perf_counter_ns

swap_count = 0
compare_count = 0


def main():
    start = perf_counter_ns()

    arr = sys.argv
    arr.pop(0)
    mode = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = int(arr[i])
    arr.pop()
    Heapsort(arr, mode)
    
    end = perf_counter_ns()
    time = end - start

    print("HeapSort:\nExecution time: ", time, " nanoseconds\nComparisons: ", compare_count, "\nSwaps: ", swap_count, "\n", arr)    

def Heapsort(list, mode):
    
    def Down(root, size):
        left_elem = root* 2 + 1
        right_elem = left_elem + 1
        local_max = root
        global compare_count

        if left_elem < size:
            if (mode == "asc" and list[int(local_max)] < list[int(left_elem)]) or (mode == "desc" and list[int(local_max)] > list[int(left_elem)]):
                local_max = left_elem
            compare_count = compare_count + 1
        if right_elem < size:
            if (mode =="asc" and list[int(local_max)] < list[int(right_elem)]) or (mode == "desc" and list[int(local_max)] > list[int(right_elem)]):
                local_max = right_elem
            compare_count = compare_count + 1
        if local_max == root:
            return

        Swap(local_max, root)
        Down(local_max, size)

    def Swap(lowered_elem, index_last_elem):
        x = list[int(lowered_elem)]
        list[int(lowered_elem)] = list[int(index_last_elem)]
        list[int(index_last_elem)] = x
        global swap_count 
        swap_count = swap_count + 1
    
    index_last_elem = len(list) - 1  
    x = len(list)/2 - 1

    while x >= 0:
        Down(x, len(list)) 
        x = x - 1

    while index_last_elem >= 0:
        Down(0, index_last_elem + 1)
        Swap(0, index_last_elem)
        index_last_elem = index_last_elem - 1

    return list

if __name__ == "__main__":
    main()
