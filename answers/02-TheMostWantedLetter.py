import string

class TheMostWantedLetter():

    def checkio(text: str) -> str:
        text = text.lower()
    
        d = dict()
        for c in text:
            if not c.isalpha(): continue # Skip non-alpha
            d[c] = d.get(c,0) + 1
    
        sortedValues = [(d[k], k) for k in sorted(d, key=d.get, reverse=True)]
    
        topLetters = [x[1] for x in sortedValues if x[0] == sortedValues[0][0]]
        
        letter = sorted(topLetters)[0]
    
        #return letter
    
        # or 
        return max(string.ascii_lowercase, key=text.count)

    if __name__ == '__main__':
        print("Example:")
        print(checkio("Hello World!"))

        #These "asserts" using only for self-checking and not necessary for auto-testing
        assert checkio("Hello World!") == "l", "Hello test"
        assert checkio("How do you do?") == "o", "O is most wanted"
        assert checkio("One") == "e", "All letter only once."
        assert checkio("Oops!") == "o", "Don't forget about lower case."
        assert checkio("AAaooo!!!!") == "a", "Only letters."
        assert checkio("abe") == "a", "The First."
        print("Start the long test")
        assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
        print("The local tests are done.")
        assert checkio("Lorem ipsum dolor sit amet") == "m", "Lorem Ipsum"
