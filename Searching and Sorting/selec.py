def _selSor(arr1):
    for i in range(len(arr1)):
        key=i
        for j in range(i+1,len(arr1)):
            if(arr1[i]>arr1[j]):
                key=j
                arr1[i],arr1[key]=arr1[key],arr1[i]

arr1=[23,17,164,74,32,436,21,1,0,4]
print('Array Before Sorting :',arr1)
_selSor(arr1)
print('Array After Sort :',arr1)