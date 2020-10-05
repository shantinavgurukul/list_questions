a=[-2,0,-9,11,45]
b=[]
i=0
while i<len(a):
    j=i
    while j<len(a):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    b.append(a[i])
    i+=1
print(b)    




# ar = ['s','h','a','n','t','i','j','i']
# i=0
# s=[]
# while(i<len(ar)-1):
#     j=i
#     while(j<len(ar)):
#         if ar[i] > ar[j]:
#             ar[i], ar[j] = ar[j], ar[i]
#         j=j+1
#     s.append(ar[i])
#     i=i+1
# print(ar[i])
        