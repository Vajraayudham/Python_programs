def _insSor(arr1):
    for i in range(1,len(arr1)):
        key=arr1[i]
        j=i-1
        while(j>=0 and key<arr1[j]):
            arr1[j+1]=arr1[j]
            j-=1
        arr1[j+1]=key
        
arr1=[23,17,164,74,32,436,21,1,0,4]
print('Array Before Sorting :',arr1)
_insSor(arr1)
print('Array After Sort :',arr1)