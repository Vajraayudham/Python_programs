arr1=[1,2,3,4,5,6,7,8,9,10]
def binSer(arr1,key):
    l=0
    r=int(len(arr1)-1)
    while(l<=r):
        mid=(l+r)//2
        if(arr1[mid]==key):
            return mid
        elif(key<arr1[mid]):
            r=mid-1
        elif(key>arr1[mid]):
            l=mid+1
    return (key,' Not Found in Array.')

def _linSerach(key,arr1):
    i=0
    for i in range(0,len(arr1)):
        if(key==arr1[i]):
            print('Key found at index :',i)

print(arr1)
key=int(input('Enter Key to search :'))
print('Menu:\n\t1.Linear Search'
      '\n\t2.Binary Seach'
      '\n\t3.Show Array'
      '\n\t4.Exit')
ch=int(input('Enter Your Choice :'))
if(ch==1):
    _linSerach(key,arr1)    
elif(ch==2):
    print(key," Found At index ",binSer(arr1,key))
elif(ch==3):
    print(arr1)
elif(ch==4):
    exit()
