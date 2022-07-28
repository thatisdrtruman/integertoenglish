#Dictionaries
unitdict={1 : "one", 2 : "two", 3 : "three",
            4 : "four", 5 : "five", 6 : "six",
            7 : "seven", 8 : "eight", 9 : "nine"}

tendict={0: "ten", 1 : "eleven", 2 : "twelve", 3 : "thirteen",
        4 : "fourteen", 5 : "fifteen", 6 : "sixteen",
        7 : "seventeen", 8 : "eighteen", 9 : "nineteen"}

tydict={2 : "twenty", 3 : "thirty", 4 : "forty",
        5 : "fifty", 6 : "sixty", 7 : "seventy",
        8 : "eighty", 9 : "ninety"}

bigvalue=["trillion", "billion", "million", "thousand", ""]


def IntegerToEnglish(DigitNumber: int) -> str:
    def ValueErrorRaiser():
        """
        If called, will terminate the programe, due to invalid DigitNumber
        """
        raise ValueError("We can't accept this number, try another")
    
    def ListProduce(DigitNumber):
        number = list(str(DigitNumber))

        for i in range(0, 15-len(number)):
            number.insert(0, "0")
        return [number[i:i+3] for i in range(0,15,3)]
    
    def GrammarCleaner(word):

        wordlist = word.strip().split()

        if wordlist[-1] == "," or wordlist[-1] == "and":
            wordlist.pop(-1)

        if wordlist[0] == "," or wordlist[0] == "and":
            wordlist.pop(0)
            
        if "," in wordlist[-1]:
            wordlist[-1] = wordlist[-1][:-1]

        word = " ".join(wordlist)

        return word
    
    def WordConversion(
                hundred, tens,
                unit, multiplier):
        """
        Converts the hundred, ten and unit number into their respective numbers
        from the three dictionaries, including adding error
        and the multiplier and return to append to the word variable
        """
        subword = ""
        isty = False
        notzero = False

        if int(hundred) != 0:
            notzero = True
            subword += str(unitdict[int(hundred)]) + " hundred"
            if int(tens) != 0 or int(unit) != 0:
                subword += " and "

        if not multiplier:
            if (int(tens) != 0 or int(unit) != 0) and int(hundred) == 0:
                subword += "and "

        if int(tens) == 1:
            notzero = True
            subword += str(tendict[int(unit)])
            unit = 0 #To ensure if int(unit) not in unitdict to prevent duplicating unit, e.g. fifteen five" 

        if int(tens) in tydict:
            notzero = True
            subword += str(tydict[int(tens)])
            isty = True

        if int(unit) in unitdict:
            notzero = True
            if isty:
                subword += "-"
            subword += str(unitdict[int(unit)])

        if notzero:                
            subword += " " + str(multiplier) + ", "
        
        return subword
    
    word = "" #Initial empty string

    try:
        if not (isinstance(DigitNumber, int)):
            ValueErrorRaiser()
    except ValueError:
            ValueErrorRaiser()
    
    NumberInAList = ListProduce(DigitNumber)

    for numberblock in range(0, 5):
        NumberInAList[numberblock].append(bigvalue[numberblock])

    for i in range(0,5):
       word += WordConversion(
                NumberInAList[i][0],
                NumberInAList[i][1],
                NumberInAList[i][2],
                NumberInAList[i][3])
    word = GrammarCleaner(word)
    word = word.capitalize()
    print(word)
    return word



#unit test
assert IntegerToEnglish(3) == "Three"

#tens test
assert IntegerToEnglish(10) == "Ten"
assert IntegerToEnglish(30) == "Thirty"
assert IntegerToEnglish(37) == "Thirty-seven"

#hundreds test
assert IntegerToEnglish(500) == "Five hundred"
assert IntegerToEnglish(501) == "Five hundred and one"
assert IntegerToEnglish(515) == "Five hundred and fifteen"
assert IntegerToEnglish(541) == "Five hundred and forty-one"
assert IntegerToEnglish(540) == "Five hundred and forty"

#unit thousand test
assert IntegerToEnglish(4000) == "Four thousand"
assert IntegerToEnglish(4003) == "Four thousand, and three"
assert IntegerToEnglish(4010) == "Four thousand, and ten"
assert IntegerToEnglish(4030) == "Four thousand, and thirty"
assert IntegerToEnglish(4037) == "Four thousand, and thirty-seven"
assert IntegerToEnglish(4500) == "Four thousand, five hundred"
assert IntegerToEnglish(4501) == "Four thousand, five hundred and one"
assert IntegerToEnglish(4515) == "Four thousand, five hundred and fifteen"
assert IntegerToEnglish(4541) == "Four thousand, five hundred and forty-one"
assert IntegerToEnglish(4540) == "Four thousand, five hundred and forty"

#teen thousand test
assert IntegerToEnglish(14000) == "Fourteen thousand"
assert IntegerToEnglish(14003) == "Fourteen thousand, and three"
assert IntegerToEnglish(14010) == "Fourteen thousand, and ten"
assert IntegerToEnglish(14030) == "Fourteen thousand, and thirty"
assert IntegerToEnglish(14037) == "Fourteen thousand, and thirty-seven"
assert IntegerToEnglish(14500) == "Fourteen thousand, five hundred"
assert IntegerToEnglish(14501) == "Fourteen thousand, five hundred and one"
assert IntegerToEnglish(14515) == "Fourteen thousand, five hundred and fifteen"
assert IntegerToEnglish(14541) == "Fourteen thousand, five hundred and forty-one"
assert IntegerToEnglish(14540) == "Fourteen thousand, five hundred and forty"

#20-90 thousand test
assert IntegerToEnglish(40000) == "Forty thousand"
assert IntegerToEnglish(40003) == "Forty thousand, and three"
assert IntegerToEnglish(40010) == "Forty thousand, and ten"
assert IntegerToEnglish(40030) == "Forty thousand, and thirty"
assert IntegerToEnglish(40037) == "Forty thousand, and thirty-seven"
assert IntegerToEnglish(40500) == "Forty thousand, five hundred"
assert IntegerToEnglish(40501) == "Forty thousand, five hundred and one"
assert IntegerToEnglish(40515) == "Forty thousand, five hundred and fifteen"
assert IntegerToEnglish(40541) == "Forty thousand, five hundred and forty-one"
assert IntegerToEnglish(40540) == "Forty thousand, five hundred and forty"

#2x-9x thousand test
assert IntegerToEnglish(46000) == "Forty-six thousand"
assert IntegerToEnglish(46003) == "Forty-six thousand, and three"
assert IntegerToEnglish(46010) == "Forty-six thousand, and ten"
assert IntegerToEnglish(46030) == "Forty-six thousand, and thirty"
assert IntegerToEnglish(46037) == "Forty-six thousand, and thirty-seven"
assert IntegerToEnglish(46500) == "Forty-six thousand, five hundred"
assert IntegerToEnglish(46501) == "Forty-six thousand, five hundred and one"
assert IntegerToEnglish(46515) == "Forty-six thousand, five hundred and fifteen"
assert IntegerToEnglish(46541) == "Forty-six thousand, five hundred and forty-one"
assert IntegerToEnglish(46540) == "Forty-six thousand, five hundred and forty"

#hundred thousand test
assert IntegerToEnglish(400000) == "Four hundred thousand"
assert IntegerToEnglish(400003) == "Four hundred thousand, and three"
assert IntegerToEnglish(400010) == "Four hundred thousand, and ten"
assert IntegerToEnglish(400030) == "Four hundred thousand, and thirty"
assert IntegerToEnglish(400037) == "Four hundred thousand, and thirty-seven"
assert IntegerToEnglish(400500) == "Four hundred thousand, five hundred"
assert IntegerToEnglish(400501) == "Four hundred thousand, five hundred and one"
assert IntegerToEnglish(400515) == "Four hundred thousand, five hundred and fifteen"
assert IntegerToEnglish(400541) == "Four hundred thousand, five hundred and forty-one"
assert IntegerToEnglish(400540) == "Four hundred thousand, five hundred and forty"

#hundred and x thousand test
assert IntegerToEnglish(408000) == "Four hundred and eight thousand"
assert IntegerToEnglish(408003) == "Four hundred and eight thousand, and three"
assert IntegerToEnglish(408010) == "Four hundred and eight thousand, and ten"
assert IntegerToEnglish(408030) == "Four hundred and eight thousand, and thirty"
assert IntegerToEnglish(408037) == "Four hundred and eight thousand, and thirty-seven"
assert IntegerToEnglish(408500) == "Four hundred and eight thousand, five hundred"
assert IntegerToEnglish(408501) == "Four hundred and eight thousand, five hundred and one"
assert IntegerToEnglish(408515) == "Four hundred and eight thousand, five hundred and fifteen"
assert IntegerToEnglish(408541) == "Four hundred and eight thousand, five hundred and forty-one"
assert IntegerToEnglish(408540) == "Four hundred and eight thousand, five hundred and forty"

#hundred and teen thousand test
assert IntegerToEnglish(414000) == "Four hundred and fourteen thousand"
assert IntegerToEnglish(414003) == "Four hundred and fourteen thousand, and three"
assert IntegerToEnglish(414010) == "Four hundred and fourteen thousand, and ten"
assert IntegerToEnglish(414030) == "Four hundred and fourteen thousand, and thirty"
assert IntegerToEnglish(414037) == "Four hundred and fourteen thousand, and thirty-seven"
assert IntegerToEnglish(414500) == "Four hundred and fourteen thousand, five hundred"
assert IntegerToEnglish(414501) == "Four hundred and fourteen thousand, five hundred and one"
assert IntegerToEnglish(414515) == "Four hundred and fourteen thousand, five hundred and fifteen"
assert IntegerToEnglish(414541) == "Four hundred and fourteen thousand, five hundred and forty-one"
assert IntegerToEnglish(414540) == "Four hundred and fourteen thousand, five hundred and forty"

#hundred and ty thousand test
assert IntegerToEnglish(440000) == "Four hundred and forty thousand"
assert IntegerToEnglish(440003) == "Four hundred and forty thousand, and three"
assert IntegerToEnglish(440010) == "Four hundred and forty thousand, and ten"
assert IntegerToEnglish(440030) == "Four hundred and forty thousand, and thirty"
assert IntegerToEnglish(440037) == "Four hundred and forty thousand, and thirty-seven"
assert IntegerToEnglish(440500) == "Four hundred and forty thousand, five hundred"
assert IntegerToEnglish(440501) == "Four hundred and forty thousand, five hundred and one"
assert IntegerToEnglish(440515) == "Four hundred and forty thousand, five hundred and fifteen"
assert IntegerToEnglish(440541) == "Four hundred and forty thousand, five hundred and forty-one"
assert IntegerToEnglish(440540) == "Four hundred and forty thousand, five hundred and forty"

#hundred and 2x-9x thousand test
assert IntegerToEnglish(449000) == "Four hundred and forty-nine thousand"
assert IntegerToEnglish(449003) == "Four hundred and forty-nine thousand, and three"
assert IntegerToEnglish(449010) == "Four hundred and forty-nine thousand, and ten"
assert IntegerToEnglish(449030) == "Four hundred and forty-nine thousand, and thirty"
assert IntegerToEnglish(449037) == "Four hundred and forty-nine thousand, and thirty-seven"
assert IntegerToEnglish(449500) == "Four hundred and forty-nine thousand, five hundred"
assert IntegerToEnglish(449501) == "Four hundred and forty-nine thousand, five hundred and one"
assert IntegerToEnglish(449515) == "Four hundred and forty-nine thousand, five hundred and fifteen"
assert IntegerToEnglish(449541) == "Four hundred and forty-nine thousand, five hundred and forty-one"
assert IntegerToEnglish(449540) == "Four hundred and forty-nine thousand, five hundred and forty"

#Other tests
assert IntegerToEnglish(12703511033) == "Twelve billion, seven hundred and three million, five hundred and eleven thousand, and thirty-three"
assert IntegerToEnglish(12703511333) == "Twelve billion, seven hundred and three million, five hundred and eleven thousand, three hundred and thirty-three"

assert IntegerToEnglish(371292) == "Three hundred and seventy-one thousand, two hundred and ninety-two"
assert IntegerToEnglish(551000000000000) == "Five hundred and fifty-one trillion"

assert IntegerToEnglish(999999999999999) == "Nine hundred and ninety-nine trillion, nine hundred and ninety-nine billion, nine hundred and ninety-nine million, nine hundred and ninety-nine thousand, nine hundred and ninety-nine"
