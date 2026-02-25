#Text Analysis Functions
def count_words(text):
    words=text.split()
    count=len(words)
    return count

def count_vowels(text):
    count=0
    for ch in text:
        if ch in "aeiouAEIOU":
            count=count+1
    return count
def count_consonants(text):
    count=0
    for ch in text:
        if ch not in "aeiouAEIOU":
            count=count+1
    return count

def reverse_text(text):
    return text[::-1]

def isPalindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
def remove_vowels(text):
    result=""
    for ch in text:
        if ch not in "aeiouAEIOU":
            result +=ch
    return result
def word_frequency(text):
    text.lower()
    words=text.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
def  longest_word(text):
    words=text.split()
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest

def analyse_text():
    while True:
        print("~~~~~~~~~MENU~~~~~~~~~~")
        print("1.Find number of words")
        print("2.Count no of vowels")
        print("3.count no of consonants")
        print("4.Reverse of string")
        print("5.Palindromme checking")
        print("6.Remove vowels in a string")
        print("7.Word Frequency")
        print("8.Longest word in sequence")
        
        print("9.Exit")

        choice=int(input("Enter a choice to proceed:"))
        if choice==1:
           text=input("Enter a text to proceed:")
           print(f"No of words in {text} is {count_words(text)}")
        
        
        elif choice==2:
            text=input("Enter a text to proceed:")
            print(f"No of vowels in {text} is {count_vowels(text)}")
           
        
       
        elif choice==3:
            text=input("Enter a text to proceed:")
            print(f"No of consonants in {text} is {count_consonants(text)}")
     
        elif choice==4:
            text=input("Enter a text to proceed:")
            print(f"Reversed {text} is {reverse_text(text)}")

        elif choice==5:

            text=input("Enter a text to proceed:")
            if isPalindrome(text):
                print("yes its palindrome")
            else:
                print("Not a palindrome")
            

        
        elif choice==6:
            text=input("Enter a text to proceed:")
            print(f"Removed vowels in a word: {remove_vowels(text)}")
            

      
        elif choice==7:
           text=input("Enter a text to proceed:")
           print(f"No of  frequent words in {text} is {word_frequency(text)}")
        

        #To check if its a perfect number or not
        elif choice==8:
           text=input("Enter a text to proceed:")
           print(f"Longest word in {text} is {longest_word(text)}")
              
        elif choice==9:
            return -1
        else:
            print("Invalid Input Try again")
    analyse_text()


