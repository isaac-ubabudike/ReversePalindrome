class Solution:
    def longestPalindrome(self, words):
        words = words
        self.word_to_list(words)

    # Coverts the given String to a String List
    def word_to_list(self, words):
        string_to_list = []
        for char in words:
            string_to_list.append(char)
        self.Breaker(string_to_list)
        return string_to_list

    # Breaks up the String List into sections for analysis
    def Breaker(self, words):
        string = ''
        for i in range(len(words)):
            string = string + words[i]
            self.compare(string)
        return string

    def compare(self, new_string):
        new_string_list = []
        if len(new_string) <= 1:
            pass
        else:
            if new_string == new_string[::-1]:
                print(new_string)
            else:
                pass





