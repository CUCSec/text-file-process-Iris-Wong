num=0
with open(r'C:\Users\Lenovo\Desktop\python作业\text-file-process-Iris-Wong\log_files\201811113031.log',encoding='utf8') as file:
    for i in file:
        list1=i.split('：')
        s1=list1[2]
        list2=s1.split(',')
        s2=list2[0]
        if s2=='201811113031':
            num+=1
print(num)