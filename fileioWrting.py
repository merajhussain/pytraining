myfile =  open(r"C:\py\newfile.txt","w+");

myfile.write("hello");

 


myfile.seek(0);
print(myfile.read());
myfile.close();


with open(r"c:\py\newfile.txt","w+") as f:
    f.write("new line added");
    
   
   
print(f.closed );