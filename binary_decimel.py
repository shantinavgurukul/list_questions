
# binary_number = [1,1,0,1,0]
# length = len(binary_number)
# a = 1
# sum=0
# i=0
# while(i<=length):
#     sum= sum+2**i*(binary_number[length-a])
#     i=i+1
#     a = a+1
# print(sum)


n=[[1,3,4,5,6],[1,8,9,10,11]]
i=0
while(i<len(n)):
    j=0
    while(j<len(n[i])):
        print(n[i][j])
        j=j+1
    i=i+1