import numpy as np
nparray=np.array([1,4,2])
print(nparray)
nparray=np.array([2,2,4])
print(nparray)
print(type(nparray))
print(nparray.dtype)
nparray=np.array([5,3,4],dtype=float)
print(nparray)
nparray=np.array([[1,2,3],[4,5,6]])
print(nparray)
l=[[5,9,3],[1,8,6]]
a=[]
for e in l:
	for elem in e:
		a.append(elem)
nparray=np.array(a)
print(nparray)
print(type(nparray))


arr=np.arange(3,20,2)
print(arr)
arr=np.arange(3,20)
print(arr)
arr=np.arange(6)
print(arr)


arr=np.zeros(7)
print(arr)
arr=np.zeros((5,6))
print(arr)

arr=np.zeros((5,6),dtype=np.int64)
print(arr)

arr=np.ones(5)
print(arr)
arr=np.ones((4,5))
print(arr)
arr=np.ones((4,5),dtype=np.int64)
print(arr)


arr=np.full(3,9)
print(arr)
arr=np.full((4,5),9)
print(arr)

print(arr.shape)

arr=np.linspace(20,60,5,dtype=np.int32)
print(arr)
arr,step=np.linspace(20,60,5,retstep=True)
print(arr)
print(step)

s=[True,False]
b=np.random.choice(s,size=5)
print(b)
b=np.random.choice(s,size=(3,4))
print(b)

b=np.ones(5,dtype=bool)
print(b)
b=np.zeros(5,dtype=bool)
print(b)

l=[5,0,9,7,0,4]
b=np.array(l,dtype=bool)
print(b)

l=[4,'','hello',9,0]
b=np.array(l,dtype=bool)
print(b)


arr=np.array([9,8,9,7])
r=np.where(arr>7,['h','k','i','i'],['o','i','u','o'])
print(r)

r=np.where(arr>8)&(arr<10)
print(r)

print(r[0])

arr=np.arry([11,99,15,18,15,99])
r=np.where(arr==15)
print(r)
print(r[0])
print(r[0][0])

r=np.where(arr==1000)
print(r)
print(r[0])

arr=np.array([[11,12,13],[14,15,16],[12,14,15]])
