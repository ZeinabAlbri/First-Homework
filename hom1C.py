l=['Network','Math','Programming','Physics','Music']
flag=False
print("items that starts with 'P' letter :")
for i in range(len(l)):
    if l[i].startswith('P'):
        print(l[i],end=' , ')
        flag=True
if not flag:
    print('not found')
    
