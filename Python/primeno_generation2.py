import numpy as np

final1=[]
r=10**4

fournp1_file=open('4n+1.txt','w')
threenp1_file=open('3n+1.txt','w')

# def append_new_line(file_name, text_to_append):
#     with open(file_name, "a+") as file_object:
#         file_object.seek(0)
#         data = file_object.read(100)
#         if len(data) > 0:
#             file_object.write("\n")

#         file_object.write(text_to_append)

for i in range(1,r):
    # 4n+1
    if (4*i+1)<=r:
        z1=4*i+1
        # append_new_line('4n+1.txt',str(z1))
        fournp1_file.write(str(z1))

    # 3n+1
    if (3*i+1)<=r:
        z2=3*i+1
        # append_new_line('3n+1.txt',str(z2))
        threenp1_file.write(str(z2))

with open('4n+1.txt', 'r') as file1:
    with open('file.txt', 'r') as file2:
        same = set(file1).intersection(file2)

with open('some_output_filex.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
with open('3n+1.txt', 'r') as file1:
    with open('file.txt', 'r') as file2:
        same = set(file1).intersection(file2)

 

with open('some_output_filey.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)


y1=np.loadtxt('some_output_filex.txt')
y1.sort()
y2=np.loadtxt('some_output_filey.txt')
y2.sort()
for i in range(len(y1)):
    if y1[i]==y2[i]:
        final1.append(y1[i])
        

#print(final1)
print(len(final1))

with open("file_finaldemo.txt", "w") as f:
    for s in final1:
        f.write(str(s) +"\n")
