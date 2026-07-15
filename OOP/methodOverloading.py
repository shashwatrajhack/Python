class Area:
    def area(self,l=0,b=0):
        if(l>0 and b>0):
            print (l*b)
        elif (l>0 and b==0):
            print (l*l)
        
a = Area();
a.area(4,5)
a.area(3)
