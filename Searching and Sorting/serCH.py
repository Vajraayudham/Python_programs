def _bubbSor(arr1):
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if(arr1[j]<arr1[i]):
                temp=arr1[j]
                arr1[j]=arr1[i]
                arr1[i]=temp

def _selSor(arr1):
    for i in range(len(arr1)):
        key=i
        for j in range(i+1,len(arr1)):
            if(arr1[i]>arr1[j]):
                key=j
                arr1[i],arr1[key]=arr1[key],arr1[i]
def _insSor(arr1):
    for i in range(1,len(arr1)):
        key=arr1[i]
        j=i-1
        while(j>=0 and key<arr1[j]):
            arr1[j+1]=arr1[j]
            j-=1
        arr1[j+1]=key

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(0, n1):
		L[i] = arr[l + i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]
	i = 0	 
	j = 0	 
	k = l	 
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

arr1=[12, 11, 13, 5, 6, 7, 123, 0, 1, 3]
print(arr1)
n=len(arr1)
while(1):
    print('Menu:\n\t1.Bubble Sort'
      '\n\t2.Selection Sort'
      '\n\t3.Insertion Sort'
      '\n\t4.Merge Sort'
      '\n\t5.Shell Sort'
      '\n\t6.Show Array'
      '\n\t7.Exit')
    match ch:=int(input('Enter Your Choice:')):
        case 1:
            _bubbSor(arr1)
            print('Array After Sort :',arr1)
        case 2: 
            _selSor(arr1)
            print('Array After Sort :',arr1)
        case 3: 
            _insSor(arr1)
            print('Array After Sort :',arr1)
        case 4:
            mergeSort(arr1, 0, n-1)
            print('Array After Sort :',arr1)
        case 5:
            shellSort(arr1,n)
            print('Array After Sort :',arr1)
        case 6: print(arr1)
        case 7: exit()
        case _:
            print('Wrong Choice')      

