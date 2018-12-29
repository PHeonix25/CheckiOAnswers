class HousePassword():
    def checkio(data: str) -> bool:

        rules = [
                lambda x: any(c.isupper() for c in x),      # must have at least one uppercase
                lambda x: any(c.islower() for c in x),      # must have at least one lowercase
                lambda x: any(c.isdigit() for c in x),      # must have at least one digit
                lambda x: len(x) >= 10                      # must be at least 10 characters
                ]
    
        return bool(all(rule(data) for rule in rules))

    if __name__ == '__main__':
        #These "asserts" using only for self-checking and not necessary for auto-testing
        assert checkio('A1213pokl') == False, "1st example"
        assert checkio('bAse730onE4') == True, "2nd example"
        assert checkio('asasasasasasasaas') == False, "3rd example"
        assert checkio('QWERTYqwerty') == False, "4th example"
        assert checkio('123456123456') == False, "5th example"
        assert checkio('QwErTy911poqqqq') == True, "6th example"
        print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")