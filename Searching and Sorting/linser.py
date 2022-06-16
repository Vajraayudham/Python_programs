def _linSerach(key,arr1):
    i,j=0,0
    for i in range(0,len(arr1)):
        if(key==arr1[i]):
            print('Key found at index :',i)

arr1=[1,2,3,4,5,6,7,8,9,10]
key=int(input('Enter key  search : '))
_linSerach(key,arr1)
