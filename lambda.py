checkFirstLetter= lambda string,letter: (string[0].lower()==letter.lower())#yahan lambda function check kar raha hai kay string ka first letter given letter say match kar raha hai ya nahi, .lower lowercase mein convert karnay kayliye use hua hai
data=["Ali","Ahmed","Faaz","Laeeq","Rehman","Iman"]# list of strings
def searchInList(list,start):#defination of function
    for item in list:#loop through list
        if(checkFirstLetter(item,start)):#lambda function ko karay search kya
            print(item)#agar true aya to print kardo item

searchInList(data,"A")#calling function