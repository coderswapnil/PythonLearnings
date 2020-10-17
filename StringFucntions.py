message ='Happy 28th Birthday Jon'

#check is message is all alphabates

print(message.isalpha())

#check is numbers

print(message.isnumeric())

#is alphanumeric

print(message.isalnum())

name='SwapnilGadekar20000'

print(name.isalnum())

#calculate length

print(len(message))

#check particular alphabet in string

print(message.find('B')) ##index of B
print(message.find('b')) ## as b is not present it will return -1

#check complete word

print(message.find('Birthday'))

#trimming the spaces

temp='000000tile of the movie*     ****    '

print(temp.strip())

##trimming only left side particular character

print(temp.lstrip('0'))

#trimming righthand side particular characters

print(temp.rstrip('*'))

