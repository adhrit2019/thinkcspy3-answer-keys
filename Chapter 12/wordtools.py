# Question 8

from unit_tester import test
import string
import random

def cleanword(s):
    """ Returns a clean word i.e. a word without puctuations. """
    
    res = ""
    
    for char in s:
        if char not in string.punctuation:
            res += char
        
    return res


def has_dashdash(s):
    """ Returns True if s has '--' in it and False if not. """
    
    return "--" in s


def extract_words(s):
    """ Extracts words from s. """
  
    s = s.split() 
    res = []
    
    for word in range(len(s)):
        if not has_dashdash(s[word]):
            s[word] = cleanword(s[word].lower())
        else:
            s[word] = s[word].split("--")
            
        if type(s[word]) == list:
            for words in s[word]:
                res.append(words)
        else:
            res.append(s[word])
                   
    return res


def wordcount(w, sl):
    """ Returns the number of occurences of w in sl. """
    
    num = 0
    
    for word in sl:
        if w == word:
            num += 1
            
    return num


def wordset(sl):
    """ Returns a list as a set of the words in sl. """
    
    set_sl = []
    
    for word in sl:
        if word not in set_sl:
            set_sl.append(word)
        
    return set_sl


def longestword(sl):
    """ Returns the length of the longest word in sl. """
    
    ml = 0
    for word in sl:
        if len(word) > ml:
            ml = len(word)
            
    return ml
      
    
if __name__ == "__main__":
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")
    
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    
    test(extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") == ['she','tried','to','curtsey','as','she','spoke','fancy'])

    test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)
    
    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["now", "is", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "is", "am"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["or", "a", "am", "is", "are", "be", "but"])
    
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)