from typing import List, Tuple

#tworzę w osobnej funkcji kopię listy żeby naprawić problem
def quicksort(unsorted: List[int]) -> List[int]:
    return quicksort_working_on_copy(unsorted[:])

def quicksort_working_on_copy(I: List[int], start = 0, stop = None) -> List[int]:  
    # I = unsorted[:] Nie wiem czemu ale pracując z tym rozwiązaniem pojawiają się błędy
    if stop == None:
        stop = len(I) - 1

    if start < stop:
        pivot = I[start + (stop - start) // 2]
        
        i = start
        j = stop

        while i <= j:

            #szukam i oraz j
            while I[i] < pivot:
                i += 1
            while I[j] > pivot:
                j -= 1   

            #porównuję
            if i <= j:
                I[j], I[i] = I[i], I[j]
                i += 1
                j -= 1
                
        quicksort_working_on_copy(I, start, j)
        quicksort_working_on_copy(I, i, stop)
    return I


def bubblesort(unsorted: List) -> Tuple[List, int]:
    I = unsorted[:]
    n = len(unsorted)
    counter = 0

    while n > 1 :

        for i in range(1, n):
            if I[i-1] > I[i]:
                I[i-1], I[i] = I[i], I[i-1]
                counter += 1
        n -= 1
    return I, counter

