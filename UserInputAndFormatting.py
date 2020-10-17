#take name input
name =input('What is your name ?')
print(name)

#take age input
age=input ('What is yout age?')
print(age)

#take hobbies
hobbies=[]
hobbies=input('What are your hobies?')
print(hobbies)

#format all the info

finalOut='Your name is {} at the age of {} your hobbies are {}'
finalOut=finalOut.format(name,age,hobbies)

#display output
print(finalOut)
