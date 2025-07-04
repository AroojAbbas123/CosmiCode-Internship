#In this task we are going to find the longest word in a sentence or string.

def longestWord(str):
    if len(str) <= 1:
        return str
    
    # Remove punctuation and split into words
    str_punc = "~!@#$%^&*()_+{}[]|\"';:<>,./?`"
    cleaned_str = ''.join([char for char in str if char not in str_punc])
    words = cleaned_str.split()  
    
    if not words:  
        return ""
    
    longest = words[0]
    for i in words[1:]:
        if len(i) > len(longest):
            longest = i
    
    return f'"{longest}"'


string=str(input("Enter a string: "))
print(f"Longest word in string is {longestWord(string)}")                     