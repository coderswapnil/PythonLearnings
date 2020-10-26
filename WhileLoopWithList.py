#while loop with list

questionsFromChild=[]

queCount=0
while queCount<=3:
    que=input('Ok!time for Q and A game : ').strip().lower()
    questionsFromChild=questionsFromChild+[que]
    queCount=queCount+1
print(("All the questions from Child : {}").format(questionsFromChild))
