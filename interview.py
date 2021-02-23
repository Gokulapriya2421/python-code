class Father:
    def __init__(self,name,occupation,salary,mobile_number):
        self.name=name
        self.occupation=occupation
        self.salary=salary
        self.mobile_number=mobile_number
        
class Son(Father):
        def __init__(self,name_of_son,occupation_of_son,salary_of_son,mobile_number_of_son,degree_of_son):
            self.name=name_of_son
            self.occupation=occupation_of_son
            self.salary=salary_of_son
            self.mobile_no=mobile_number_of_son
            self.degree= degree_of_son
            
def details(name):
    global occupation
    occupation=input("enter occupation").lower()
    global salary
    salary=eval(input("enter salary"))
    global mobile_number
    mobile_no=int(input("enter mobile number"))
    
    if name=="Father":
        global details_of_father
        details_of_father=Father(name,occupation,salary,mobile_no)
        return details_of_father
        
    else:
        global degree
        degree=input("enter degree")
        global details_of_son
        details_of_son=Son(name,occupation,salary,mobile_no,degree)
        return details_of_son
        
    return details_of_father, details_of_son

name=input("enter name:")
details(name)
print(details_of_son.degree)        
    