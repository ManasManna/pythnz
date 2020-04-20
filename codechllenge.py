preorder=[]
lst=[]
finallist=[]
n = int(input("Enter number of elements : ")) 
print("Enter the predefined order of list")
for i in range(0,n):
    order=int(input())
    preorder.append(order)

print("Enter the elements of the list")
for i in range(0,n):
    elem=str(input())
    lst.append(elem)
   
for i in range(0,n):
    if predorder[i]==len(lst[i]):
        u=lst[i]
        v=u.upper()
        finallist.insert(preorder[i],v)
    else :
        u=lst[i]
        v=u.lower()
        finallist.insert(preorder[i],v)      
print(finallist)       
        