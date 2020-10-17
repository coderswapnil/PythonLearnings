cityName='Nagpur'
stateName='MH'


userCity=input ('Give your city  name : ')
userState=input ('Give your State  name : ')

##and condition
if (cityName==userCity and stateName==userState): 
    print('in python == for string working and you are in and')
else : print ('In python == not working for string and ')

#or condition

if (cityName==userCity or stateName==userState):
    print('in python == for string working and you are in or')
else : print ('In python == not working for string or ')

##not condition

if not cityName=='Nagpur' :
    print ('Not is working ')
