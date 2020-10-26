##For loop 
#Dictionary containing student names
students={
    'male' : ['Salman','Amir','Govinda','Ranveer','Badshah'],
    'female' :['Sushma','Jaya','Daya','Leela']
    }

for singleKey in students:
    for name in students[singleKey]:
        if 'd' in name.lower():
            print (('This Student name {} has "d" in his/her firstname').format(name))
            break # come out of the name loop
        elif "$" in name:
            pass
            print("this is the pass block it can be used just to show noting will happen if condition met loop will continue its operation")
        else:
            continue #continue the loop ietrations
    break #come out of the outer loop
            
