import json
#import the pattern matching library
from difflib import get_close_matches

# created a data varaible to laod the json data 
data = json.load(open("data.json"))

#define a funtion translate the word
def translate(word):
    #convert to lower case
    word = word.lower()
    #boolean condition to check if word exist
    if word in data:
       
        #excute if word exist
        return data[word]
       
        #chek with the pattern matchig lib to get the word
    elif len(get_close_matches(word,data.keys())) > 0:
         
        reply = input("did you mean %s instead? Enter Y if Yes, N if No -> " % get_close_matches(word,data.keys())[0])
        
        if reply.lower() == "y":
           
            return data[get_close_matches(word,data.keys())[0]]
        
        elif reply.lower() == "n":

            return "please check the word"

        else:

            return "we didnt understand your query"
        #if word doesnt exist
    else:
        #excutes if word doesn't exist
        return "This word doesn't exist"

#ask for the input 
word = input("Enter Word:-> ")

result = translate(word)

if type(result) == list :

    for item in result:
        print(item)

else:
    
    print(result)