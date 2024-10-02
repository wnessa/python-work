class registration:
    def __init__(self,name,reg_no,course,year):
        self.name=name
        self.reg_no=reg_no
        self.course=course
        self.year=year

    def __str__(self):
        return(f"name:{self.name} reg_no:{self.reg_no} course:{self.course} year:{self.year}")

student1=registration("Moses mpagi","S23B13/109","Bsit","2023")
print(student1)    

student1=registration("Nessa Namatovu","S23B14/100","Dit","2022")
print(student1) 

student1=registration("Natongo Maria","S23B13/023","Law","2024")
print(student1)    

student1=registration("Mubiru Jame","S23B13/197","Bscs","2020")
print(student1)    
       
        