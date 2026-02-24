#String Manipulator

#Taking Input from the user
Original_Sentence=input("Enter Sentence:")

#Making a function because its a special case 
def total_characters_without_spaces(text):
    return len(text.replace(" ","")) #Here it will replace " " with "" that means it will ignore blank spaces


def total_words(text):
    words=text.split() #Split function is used for 
    count=len(words)

    return count



    words=text.split()
    
    return words



print("Total characters with spaces:",len(Original_Sentence))#len() used for counting characters in a string
print("Total characters without spaces :",total_characters_without_spaces(Original_Sentence))
print("Total Words in the word :",total_words(Original_Sentence))
print("Original Sentence in UPPERCASE :" ,Original_Sentence.upper())#.upper() is a converter which converts all alphabets to uppercase
print("Original Sentence in lowercase:",Original_Sentence.lower())#lower() is a converter which converts all alphabets to lowercase
print("Title Case :",Original_Sentence)
print("First Word is :",Original_Sentence.split()[0])
print("Last Word is :",Original_Sentence.split()[-1])
print("Reversed String is :",Original_Sentence[::-1])#[::-1] starts printing from the last character




