# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.
def shift(letter):
    if ord(letter) >=  ord ('a'):
        if ord(letter) <  ord ('z'):
            return chr(ord(letter)+1)
        elif ord(letter) ==  ord ('z') :
            return 'a'
        else:
            return letter
    else:
        return letter

def unshift(letter):
    if ord(letter) <=  ord ('z'):
        if ord(letter) >  ord ('a'):
            return chr(ord(letter)-1)
        elif ord(letter) ==  ord ('a') :
            return 'z'
        else:
            return letter
    else:
        return letter


def shift_n_letters(letter, n):
    if (n > 0):
        for i in range(0,n):
            letter = shift(letter) 
    else:
        for i in range(0,-n):
            letter = unshift(letter) 
    return letter    

def rotate(s,o):
    so = ""
    for i in range(0, len(s)):
        so=so+shift_n_letters(s[i],o)
    return so    

print rotate("a",1)
print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
