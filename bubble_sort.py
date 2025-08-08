def bub_sort(arr):
    n = len(arr)

    for i in range(n):
        s = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                s = True
        if not s:
            break
            
    return arr

def sel_sort(arr):
    n = len(arr)

    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

sal = []

n = int(input('Enter the number of employees: '))

for i in range(0,n):
    emp = float(input(f"Enter employee number {i+1}'s Salary: "))
    sal.append(emp)

sal2 = sal.copy()

print(f'\nOriginal list {sal}\n\nSorted List Using Bubble Sort {bub_sort(sal2)}\n\nSorted List Using Selection Sort {sel_sort(sal)}')

for i in range(5):
    print(f"\nEmployee no. {i+1}'s Salary : {sal[n-i-1]}")