# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def calc_freq(str, l):
    i = 0
    c = 0
    while i < len(str):
        if str[i] == l:
            c = c + 1
        i = i + 1
    return c * 1.0 / len(str)
    
    
def freq_analysis(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    freq_arr = []
    i = 0
    while i < len(alphabet):
        l = alphabet[i]
        freq = calc_freq(message,l)
        freq_arr.append(freq)
        i = i + 1
    return freq_arr



#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
