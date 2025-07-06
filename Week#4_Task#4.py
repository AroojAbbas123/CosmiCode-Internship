
def count(string):
    
    frequency = {}  

    for char in string:
        if char in frequency:
            frequency[char] += 1 
        else:
            frequency[char] = 1   

    return frequency



text = input("Enter  a string: ")
result = count(text)
print(result)