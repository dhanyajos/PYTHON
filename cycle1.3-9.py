#9.Sort dictionary in ascending and descending order. 





y={'aleena':4,'megha':2,'kavya':1,'chithra':3} 
l=list(y.items())  
l.sort()            
print("Ascending order: ",l) 
l=list(y.items())
l.sort(reverse=True) 
print("Descending order: ",l)
dict=dict(l) 
print("Dictionary:",dict)  

