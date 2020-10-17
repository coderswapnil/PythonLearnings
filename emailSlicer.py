##take user email addres via UI
userEmail=input('Give User email address : ')


##separate username
userName=userEmail[0:userEmail.index("@")]

#separate domain name
domainName=userEmail[(userEmail.index("@"))+1:]

#output message

output='username is {} and email created by {}'
output=output.format(userName,domainName)
#display output

print(output)
