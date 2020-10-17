#create disctionary filmes which will have movie name as key with age and number of tickets lefts as values
films ={
    "Sholey" :[18,3],
    "Chota Chetan" :[5,80],
    "Bhoot" : [18,9],
    "Three Ediots" :[5,20]
    }

while True :
    choice=input ("Enter the name of the cinema you wanted to watch : ").strip().title() #strip will trunkate spaces and title will capitalised first letter of every word

    if choice in films :
        print("Yes ,Film is showing in theaters")
        age = int(input('Enter your age ').strip())
        if age >= films[choice][0]:
            print('You can proceed to book tickets')
            number_of_tickets=int(input('How many tickets you want : ').strip())
            if number_of_tickets > films[choice][1]:
                print('sorry that many tickets are not available')
            else :
                output=("{} tickets are booked enjoy your movie ").format(number_of_tickets)
                print(output)
                films[choice][1]=films[choice][1]-number_of_tickets # updating number of tickets count by duducting booked tickets ,updating dictionary 
                

        else:
            print('You are quite young to watch this movie ')
    else :
        print ("Sorry, that film is not available")
