
#Palindrom words are the words which spell same from start and end.


def isPalindrom(str):
    if(len(str)<=1):
        return True
    new_str=''.join(char for char in str if char.isalnum())
    words_start=""
    words_end=""
    for word in new_str:
        words_start+=word
    for word in reversed(new_str):
        words_end+=word
    return words_start==words_end


string =str(input("Enter a string: "))
if(isPalindrom(string)):
    print("Yes! Given string is palindrom!")
else:
    print("No! Given string is not palindrom!")


