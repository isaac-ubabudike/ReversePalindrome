def longestPalindrome(words):
    string_to_list = []
    for char in words:  # converts String to a String list
        string_to_list.append(char)
    string = ''
    for i in range(len(words)):  # Breaks up the String List into sections for analysis
        string = string + words[i]
        if len(string) > 1 and string == string[::-1]:
            print(string)


def remover(words):
    counter = 0
    while counter < len(words):
        if counter < 1:
            longestPalindrome(words)
        else:
            words = words.strip(words[0])
            longestPalindrome(words)
        counter += 1

        


# You could also try to account for words not included at the end by making each word get checked for palindrome
# Presence by reversing them and checking, because this longest palindrome checker only accounts for palindrome starting
# from the beginning
'''Example
def reverseLongestPalindrome(words):
    string_to_list = []
    for char in words:  # converts String to a String list
        string_to_list.append(char)
    string = ''
    for i in range(len(words)):  # Breaks up the String List into sections for analysis
        string = string + words[i]
        if len(string) > 1 and string == string[::-1]:
            print(string)

def remover_in_reverse(words):
    words = words[::-1]  # Over here you could see how we made the words in reverse that way we get the items lost 
    # Towards the end.
    counter = 0
    while counter < len(words):
        if counter < 1:
            longestPalindrome(words)
        else:
            words = words.strip(words[0])
            longestPalindrome(words)
        counter += 1'''

remover("anna")
