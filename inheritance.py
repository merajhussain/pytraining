class parent(object):
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def doubleMembers(self):
        m1 = m1 *2 
        m2 = m2 *2 
        
        
class child(parent):
    def __init__(self,m1,m2,m3):
        parent.__init__(self,m1,m2)
        self.m3=m3;
    def printType(self):
        print(type(self.m1))
        print(type(self.m2))
        print(type(self.m3))
        
		
 
 
cobj = child(1,2.0,'2');

print(cobj);
cobj.printType()