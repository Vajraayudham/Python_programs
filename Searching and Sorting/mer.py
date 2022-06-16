def merSor(arr1):
    if len(arr1)>1:
        mid=len(arr1)//2
        l=arr1[:mid]
        r=arr1[mid:]
        merSor(l)
        merSor(r)
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i] < r[j]:
                arr1[k]=l[i]
                i+=1
            else:
                arr1[k]=r[j]
                j+=1
                k+=1
                while i<len(l):
                    arr1[k]=l[i]
                    i+=1
                    k+=1
                    while j<len(r):
                        arr1[k]=r[j]
                        j+=1
                        k+=1

arr1=[23,17,164,74,32,436,21,1,0,4]
print('Array Before Sorting :',arr1)
merSor(arr1)
print('Array After Sort :',arr1)