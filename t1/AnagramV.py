
from collections import Counter
import sys

def is_anagrams(s, t,  min_length = 1, max_length = 5000):

    # Empty String Checks
    if not s or not t:
        return(False, 'one or both strings cannot be empty')

    # Convert to lowercase and filter out non-alphabetical characters
    s = ''.join(c for c in s.lower() if c.isalpha())
    t = ''.join(c for c in t.lower() if c.isalpha())

    # Check if the lengths of the filtered strings are within the specified range
    if not (min_length <= len(s) <= max_length) or not (min_length <= len(t) <= max_length):
        return (False)

    # Check if the lengths of the filtered strings are the same
    if len(s) != len(t):
        return (False, 'Length of both words must be the same')
    elif len(s) == len(t):
        return(True, 'Length of both words are the same')

    # Create counter objects for both strings
    counter_s = Counter(s)
    counter_t = Counter(t)

    # Check if the Counter objects are equal
    if counter_s == counter_t:
        return(True, 'String are anagram')
    else:
        missing_in_t = counter_s - counter_t
        missing_in_s = counter_t - counter_s
        if missing_in_t:
            return (False, 'All char in String s not fount in string t')
        elif missing_in_s:
            return (False, 'All char in String t not found in s')
        else:
            return (False, 'String are not anagram')

def main():
    print("Anagram Checker\n" + "="*15)
    s = input("Enter the first word: ").strip()
    t = input("Enter the second word: ").strip()

    result, message = is_anagrams(s,t)
    
    if result:
        print(f"\033[92m{message}\033[0m") 
    else:
        print(f"\033[91m{message}\033[0m") 
if __name__ == "__main__":
    main()     

# Test Cases"
s = "listen"
t = "silent"
s = ""
t = "latent"
s = "basiparachromatin"
t =  "marsipobranchiata"


    # =========== Code Documentation ===========
    # First an empty string check must be done first to check for valid input before the length of the string are check. This ensure result consistency and accuracy. If one or both strings are empty, the code output False, 'one or both strings cannot be empty'. If length are not the same, the code return false, 'length must be equal'.

    # The len check is O(1) operation that check whether the two STEINGS are of the same length which is a requirement for anagram. If the length are the same, the counter counts the frequency of each element to verify same elements in the two words, ensuring corectness and optimization.  
    
    # when the output  is sucessful, it idicates that, the length of both words are same and you can find same elements in each words. However, if the output is false, it indicates either the length of words are not the same, or there are empty strings or both words have different elements even though the length of both words could be the same

    # Line 20 ensures the length of both words are the same and line 30 counts the frequency of each element in both words. The length and counter function works togther on the input data, both length and counter should be true in other to give a sucessful result, once one parameter is false, the output result will also be false

    # It is not possible for both strings with same elements and length to result in false output; this does not comply with the if statement in line 20 and line 30. The UI can be improved by making the code accepts and input and giving the user an idea of the expected words

    # Lines 12 and 13 convert all characters of the string into lower case, ensuring that the string is comparison insensitive

    # The advantage of counter block is to optimized for counting hashable items, which makes it efficient for this task. It also automates the process, reducing the chance of errors and making the code more compact.

    # The disadvatage in this regard is that, the counter method is not optimal for small input or simple checks. Also if the input string is not purely alphabetical, additional logic might required to handle the case correctly. This method is also case sensitive, hence additional block of code needs to be added in order make it case insensitive.

    # I chose the couter method in order to handle longer strings effectively improving accuracy and efficiency. 

    # Both counter and manual time complexity runs in O(n) time where n is the length of string. The Counter method is generally more concise and easier to read, while the manual method gives you more control over the counting process

    #  The counter method  depends on how you handle elements. In the case of checking for strings only while ignoring non alphabetical characters such as spaces and puctuation, the counter method will not provide expected results because it will consider all non alphabetical characters in comparison. But if non alphabetical characters are meant to be included, the the counter method works perfectly. To need to ignore these non alphabetical characters, preprocessing the strings before using Counter is necessary.

    # Now there is a block of code to handle case sensistive and non alphabetical characters in line 63, if they are diffrent frequency but the same length, they would be considered as anagrams

    # Some anagrams are in sentence form which might have spaces or punctuation in them. Hence implemeting the filter block is essential for handling all types of anagrams, improving accuracy

    # Some Anagrams may include phrases, sentences or puctuation inside words. Not sure numbers could be anagrams

    # Anagrams are words or phrases that are formed by rearranging the letters of another word or phrase, they cannot contain numbers

    # The counter block enhances the verification by efficiently counting the frequency of each character in both strings and directly checking whether both strings have identical character counts to confirm that they are anagrams

    # Anagrams are considered to be words or phrases that are formed by rearranging the letters of another word or phrase, they must contain alphabetical characters

    # The filtering block affect the overall logic by ensuring that only alphabetic characters are considered when checking if two strings are anagrams. This adds robustness to the code by ignoring spaces, punctuation, numbers, and other non-alphabetic characters, which could otherwise interfere with the anagram check.

    # I expect the function to convert characters to lower cases, check the length of input strings, check the frequency of characters of the input string and return correct result

    # counter(s) is compared to counter(t) whether they have the same characters ignoring non alphabetical characters

    # The implementation of character comparison in the code involves using the Counter objects from the collections module to compare the frequency of each character in the two strings. First the string are converted into lower case and filter non alphabetical elements which is relevant for checking anagrams. The Counter objects are created for both strings at line 26 and 27. The character comparison is done by directly comparing the two Counter objects using the equality operator == at line 30. Based on the comparison, the function returns a tuple containing a boolean and a message at line 31.

    # The Counter method counts the frequency of each character in a string and stores the result in a dictionary-like structure where the keys are the characters and the values are their counts. In order to use the Counter object, you first need to import it from the collections module

    # Yes, line 9 return a boolean value and a statment when one or both string are empty
    
    # The empty string validation ensures that the function does not attempt to process invalid input and the importation of the counter from collections in this cose enhances code readability, efficiency, versatality and count elements automatically
    
    # The check length looks like checking if len(s) is not equal to len(t). If the two length are not the same, the return statement is : False, length of both Strings must be the same

    # The Counter block is case sensitive and will count spaces and punctuation separately if not filtered. Hence the need to convert lower case and filter non alphabetical characters  ensures consistency and acuracy in counting the characters. 

    # The counter method is a built-in functionality that allows for automatic counting . In manual counting, you will need to write additional code to initialize counts and increment them manually which is time consuming. The counter allows for simplified code, uses direct comparison (==), has improved readability and maintainabilty.

    # Although the requirement of the output should be boolean, it is important to describe the type of output message in order to guide the user understanding

    # The filter block at line 12 and 13 automatically filters non alpabetical characters making it valid for the counter to check only character frequency

    # The min_length and max_length specify range of characters must be between 1 and 5000, any value above 5000 or below 1 will not be allowed to enter the counter block code

    # Manual approach requires initializing count and increment them manually while counter method user direct comparison (==)

    # \033[92m  is the ANSI escape code for green text and \033[91m is the ANSI escape code for red text (bright red)
