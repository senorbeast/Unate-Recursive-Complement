filename1 = input("File Name : ") 
 
file1 = open(filename1).readlines() 
 
file1_line = [] 
 
for lines in file1: 
 file1_line.append(lines) 
 
filename2 = input("File Name : ") 
file2 = open(filename2).readlines() 
 
file2_line = [] 
 
for lines in file2: 
 file2_line.append(lines) 
 
n = 0 
if len(file1) > len(file2): 
 print("Length Of File is ",filename1,"is greater than",filename2,len(file1),">",len(file2)) 
 for line in file1_line: 
  if line != file2_line[n]: 
   print("Not Match:","Line :",n + 1,filename1,":",line,"|",filename2,":",file2_line[n]) 
   n += 1 
  else: 
   n += 1 
 
 
elif len(file1) < len(file2): 
 n = 0 
 print("Length Of File is ",filename1,"is less than",filename2,len(file1),"<",len(file2)) 
 for line in file2_line: 
  if line != file1_line[n]: 
   print("Not Match:","Line :",n + 1,filename2,":",line,"|",filename1,":",file1_line[n]) 
   n += 1 
  else: 
   n += 1 
 
 
else: 
 print("Length Of File is ",filename1,"Equals",filename2,len(file1),"==",len(file2)) 
 n = 0 
 for line in file1_line: 
  if line != file2_line[n]: 
   print("Not Match:","Line :",n + 1,filename1,":",line,"|",filename2,":",file2_line[n]) 
   n += 1 
  else: 
   n += 1 