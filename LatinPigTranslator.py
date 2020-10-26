#pig latin translator

# take sentence input from user
# convert that into list of words
#loop over words and check the letters
#if word starts with vovel then add 'yay' at the end and if it starts with consonent then travel till first vovel and append that to end and add 'ay
#egg->eggyay glove-oveglay
#jojn the list workds and frame the sentence 

userInput=input('Please provide input for translation :').strip().lower()
userInputList=userInput.split()

newWordsList=[]
for word in userInputList:
    if word[0] in 'aeiou':
        latinWord=word+'yay'
        newWordsList.append(latinWord)
    else:
        letterPosition=0
        for letter in word:
            if letter not in 'aeiou':
                letterPosition=letterPosition+1
            else:
                break
        
        consonentPart=word[:letterPosition]
        vovelPart=word[letterPosition:]
        finalWord=vovelPart+consonentPart+'ay'
        newWordsList.append(finalWord)
#frame sensentce from list
translated_statement=" ".join(newWordsList)
print(translated_statement)
        
            
        
        
        
        
