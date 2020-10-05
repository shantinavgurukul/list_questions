marks=[[78,76,94,86,88],[91,71,98,65],[95,45,78],[87,67,49,68,88]]
i=0
while(i<len(marks)):
    marks_of_list=marks[i]
    length=len(marks_of_list)
    j=0
    sum=0
    average=0
    while(j< len(marks_of_list)):
        sum=sum+marks_of_list[j]
        average=sum//length
        j=j+1
    i=i+1
    print(average)