def _bubbSer(arr1):
    for i in range(len(arr1)):
    for j in range(i+1,len(arr1)):
        if(arr1[j]<arr1[i]):
            temp=arr1[j]
            arr1[j]=arr1[i]
            arr1[i]=temp

arr1=[23,17,164,74,32,436,21,1,0,4]
print('Array Before Sorting :',arr1)
print('\nArray After Sorting :',arr1)