import math


class Math:

    def __init__(self, formula, valuex=0, prioranswer=0):
        '''
        ----
        Purpose
        ----
        Takes a formula as a string and returns an answer as a float.

        ----
        Values
        ----

        formula - Must be a string in the form of an equation. eg. (5 + 6) * 4

        valuex = 0 - (Optional) Must be an integer or float. May be preceded by a negative sign

        -----
        Abilities
        -----
        Add
        Multiply
        Divide
        Subtract

        Parentheses
        Exponents

        Sin()
        Cos()
        Tan()

        Absolute Values

        Determine the difference between a subtraction symbol and a negative number

        Accept spaces between values or no spaces between values and anything between

        ----
        Examples of Equations
        ----

        -(3 + 1)

        5x or x5

        sin(1 + 6)

        sin(tan(cos(sin(5))))

        |4 - 7|

        (1 + 2)^2

        ----
        What Does Not Yet Work
        ----

        (2) + |2|

        Things to Note:
        |2| + (3) Works
        (3) + |2| Does Not

        '''

        divide_by_zero = " "

        # would turn into a + a
        def testforletter(character):
            nan = 1
            for goahead in numbers:
                if character == goahead:
                    nan = 0

            return nan

        def addition(a, b):
            # print(f"a = {a}, b = {b}")
            if a == "NaN" or b == "NaN":
                return "NaN"
            else:
                return a + b

        def multiplication(a, b):
            # print(f"a = {a}, b = {b}")
            if a == "NaN" or b == "NaN" or isinstance(a, complex) or isinstance(b, complex):
                return "NaN"
            elif a == "-":
                return b * -1
            elif b == "-":
                return a * -1
            else:
                return a * b

        def subtraction(a, b):
            if a == "NaN" or b == "NaN":
                return "NaN"
            else:
                return a - b

        def division(a, b):

            try:
                if a == "NaN" or b == "NaN":
                    return "NaN"
                else:
                    return a / b
            except ZeroDivisionError:

                return "NaN"

        def exponent(a, b):
            # print(f"a = {a}, b = {b}")
            try:
                return a ** b
            except(OverflowError):
                return "NaN"

        def sct(thing, thing_after):
            # print(f"DEBUG Thing = {thing}, thingafter = {thing_after}")
            if isinstance(thing_after, complex):
                return "NaN"
            thing_after = float(thing_after)
            if thing == "sin":
                value = math.sin(thing_after)
            elif thing == "cos":
                value = math.cos(thing_after)
            elif thing == "tan":
                value = math.tan(thing_after)
            # print(f"Value={value}")
            return value
        def roots(roottype, equation):
            value = equation ** (1/roottype)
            return value

        # def parenthasis(a):
        #     a.split("(")
        #     a.split(")")
        #     parenthasis(a[1])

        def numberchecker(charcode):
            charcode = str(charcode)
            if character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or \
                    character == "6" or character == "7" or character == "8" or character == "9" or character == "0:":
                return True
            else:
                return False

        def speak(newlist):

            current_code = -1
            newcode = 1
            cont = True
            while cont:
                newcode += 1

                current_code += 1
                for characters in newlist:
                    # print(f"code = {characters}")
                    # print(f"character = {characters}")
                    # print(f"currentcode = {current_code}")
                    # print(newform)
                    if characters == "^":
                        current_code = newlist.index(characters)
                        if characters == "^":
                            answer = exponent(newlist[current_code - 1], newlist[current_code + 1])
                            if answer == "NaN":
                                return "NaN"
                            del (newlist[current_code + 1])
                            del (newlist[current_code - 1])
                            current_code -= 1
                            newlist[current_code] = answer
                            current_code += 1
                    if newcode > 10:
                        cont = False
            current_code = -1
            newcode = 1
            cont = True
            while cont:
                newcode += 1

                current_code += 1
                for characters in newlist:
                    # print(f"code = {characters}")
                    # print(f"character = {characters}")
                    # print(f"currentcode = {current_code}")
                    # print(newlist)
                    if characters == "/" or characters == "*":
                        current_code = newlist.index(characters)
                        if characters == "/":
                            answer = division(newlist[current_code - 1], newlist[current_code + 1])
                            if answer == "NaN":
                                return "NaN"
                            else:
                                del (newlist[current_code + 1])
                                del (newlist[current_code - 1])
                                current_code -= 1
                                newlist[current_code] = answer
                                current_code += 1
                        elif characters == "*":
                            # print(f"currentcode = {current_code}")
                            # print(newform)
                            answer = multiplication(newlist[current_code - 1], newlist[current_code + 1])
                            if answer == "NaN":
                                return "NaN"
                            del (newlist[current_code + 1])
                            del (newlist[current_code - 1])
                            current_code -= 1
                            newlist[current_code] = answer
                            current_code += 1
                    if newcode > 10:
                        cont = False
            newcode = 1
            cont = True
            while cont:
                # print("HERE")
                newcode += 1
                for characters in newlist:
                    if characters == "-" or characters == "+":
                        current_code = newlist.index(characters)
                        if characters == "-":
                            answer = subtraction(newlist[current_code - 1], newlist[current_code + 1])
                            if answer == "NaN":
                                return "NaN"
                            del (newlist[current_code + 1])
                            del (newlist[current_code - 1])
                            current_code -= 1
                            # print(f"DEBUG Newlist: {newlist}")
                            # print(f"DEBUG Currentcode: {current_code}")

                            newlist[current_code] = answer
                            current_code += 1
                        elif characters == "+":
                            answer = addition(newlist[current_code - 1], newlist[current_code + 1])
                            if answer == "NaN":
                                return "NaN"
                            # print(current_code)
                            # print(newform)
                            del (newlist[current_code + 1])
                            del (newlist[current_code - 1])
                            current_code -= 1
                            newlist[current_code] = answer
                            current_code += 1
                if newcode > 10:
                    cont = False

                if len(newform) == 1:
                    cont = False

            return newlist

        def parenthesis(code, startingpoint, abcount):
            # print(f"Code is {code}")
            # print(f"Extra Info: Startingpoint = {startingpoint}, abcount = {abcount}")
            try:

                snippet = []
                # print(f"Snippet is {snippet}")
                pcounta = 0
                abcounta = 0
                endpoint = len(code)
                for value8 in code:
                    if value8 == ")":
                        pcounta = 1
                    elif value8 == ">":
                        abcounta = 1

                    if pcounta == 1:
                        endpoint = code.index(")")
                    if abcounta == 1:
                        endpointab = code.index(">")
                if abcounta == 0:
                    abcount = 0
                # print(f"endpoint is at place {endpoint}")
                if abcount > 0:
                    # print("It World here")
                    # print(f"( = Endpoint: {endpoint}, < = EndpointAB:{endpointab}")
                    if endpointab < endpoint:
                        # print("GOT HERE")
                        startingpointab = endpointab
                        cont = True
                        while cont:
                            startingpointab -= 1
                            if code[startingpointab] == "<":
                                # print(f"startpoint is place {startingpoint}")
                                cont = False
                        testpointab = startingpointab + 1
                        for value2 in code[startingpointab + 1:endpointab]:
                            snippet.append(value2)
                        # print(f"Failed Here")
                        for value2 in code[startingpointab + 1:endpointab + 1]:
                            del (code[testpointab - 1])
                        # print(f"Snippet is {snippet}")
                        snippettest = speak(snippet)
                        # print(f"Speaktest = {snippettest}")
                        # code[testpointab] = snippet[0]
                        # print(f"code = {code}")
                        # print(f"Failed Here")
                    elif endpoint < endpointab:
                        mysnippet = []
                        startingpointp = endpoint
                        cont = True
                        while cont:
                            startingpointp -= 1
                            if code[startingpointp] == "(":
                                # print(f"startpointPar is place {startingpointp}")
                                cont = False
                        for value2 in code[startingpointp + 1: endpoint]:
                            # print(f"Value2 = {value2}")
                            mysnippet.append(value2)
                        # print(f"Mysnippet = {mysnippet}")
                        speaksnippet = speak(mysnippet)
                        # print(f"Speaker says {mysnippet}")
                        code[startingpointp + 1] = mysnippet[0]

                        for value2 in code[startingpointp:endpoint + 1]:
                            del (code[startingpointp])
                        code.insert(startingpointp, speaksnippet[0])




                        snippet = mysnippet
                        # print(f"Code is {code}")


                else:

                    startingpoint = endpoint
                    cont = True
                    while cont:
                        # print("HERE")
                        startingpoint -= 1
                        if code[startingpoint] == "(":
                            # print(f"startpoint is place {startingpoint}")
                            cont = False
                    testpoint = startingpoint + 1
                    for value2 in code[startingpoint + 1:endpoint]:
                        # print(f"-------------------{value2}")
                        snippet.append(value2)

                    for value2 in code[startingpoint + 1:endpoint + 1]:
                        del (code[testpoint])
                # print(f"Snippet = {snippet}")
                if snippet[0] == "tan" or snippet[0] == "sin" or snippet[0] == "cos":
                    snippet[0] = sct(snippet[0], snippet[1])
                    del snippet[1]

                if abcount > 0:
                    info = speak(snippet)
                    if info == "NaN":
                        snippet[0] = 0
                        code[startingpointab] = abs(snippet[0])
                    else:
                        code[startingpointab] = abs(snippet[0])
                else:
                    info = speak(snippet)
                    if info == "NaN":
                        snippet[0] = 0
                    else:
                        code[startingpoint] = snippet[0]
                        # print(f"Snippet is {snippet}")
                # print(code)

                return code
                # goal is to find the last startpoint based on the first endpoint
            except:
                # print("This Failed")
                return code

        x = 2

        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        letters = ["x", "y", "z"]
        symbols = ["*", "/", "+", "-"]
        usable_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
        form = []
        numbercode = ""
        newform = []
        codes = []
        # 0 = Number, 1 = Parenthases, 2=Exponent, 3=Multiplication, 4=Divison, 5=Addition, 6=Subtraction

        for character in formula:
            # print(character)
            form.append(character)

        # print(f"Form is {form}")
        # print(form)
        number = -1
        pcount = 0
        abcount = 0
        location = 0
        cont = True
        while cont:
            # print("HERE")
            if form[location] == "x" and location != 0:
                try:
                    if form[location - 1] != "(" and form[location + 1] != ")":
                        form.insert(location + 1, ")")
                        form.insert(location, "(")
                        location += 1
                        # print("HI")
                except:
                    form.insert(location + 1, ")")
                    form.insert(location, "(")
                    location += 1
                    # print("weeee")
            elif form[location] == "x" and location == 0:
                form.insert(0, "(")
                form.insert(2, ")")
                location += 1
                # print("YO")

            location += 1
            if location > len(form) - 1:
                cont = False

        # print(f"Form is {form}")
        totalabsvalues = 0
        for character in form:
            if character == "|":
                totalabsvalues += 1
        location = 0
        abscode = 0
        abcount = 0
        for character in form:

            number += 1
            side_number = number + 1
            # print(f"SideNuma = {side_number}")
            nogo = testforletter(character)
            if character == " ":
                numbercode = "ignore"
            if nogo == 0:
                numbercode += character
            if character == "(":
                pcount += 1
            if character == "|":
                abcount += 2
                currentlocation = location
                waitingoncode = 0
                if abscode == 0:
                    form[number] = "<"
                for value2 in form[location:len(form)]:
                    if location == currentlocation + 1 and value2 == "|":
                        waitingoncode = 1
                    elif value2 == "(":
                        abscode += 1
                    elif value2 == ")":
                        abscode -= 1
                    elif abscode == 0 and value2 == "|" and waitingoncode == 1:
                        waitingoncode = 0
                    elif abscode == 0 and value2 == "|" and waitingoncode == 0:
                        form[location] = ">"
                    location += 1
                location = currentlocation
            while nogo == 0:

                # print(f"Form={form}" )
                # print(f"SideNum = {side_number}")
                if len(form) == side_number:
                    # print(f"HERE _ {numbercode}")
                    nogo = 1
                elif testforletter(form[side_number]) == 1:
                    nogo = 1
                elif testforletter(form[side_number]) == 0:

                    numbercode += form[side_number]
                    del (form[side_number])


            if character == "t" and form[number + 1] == "a" and form[number + 2] == "n":
                del form[number + 2]
                del form[number + 1]
                form[number] = "tan"
                # print(form)
            if character == "c" and form[number + 1] == "o" and form[number + 2] == "s":
                del form[number + 2]
                del form[number + 1]
                form[number] = "cos"
                # print(form)
            if character == "s" and form[number + 1] == "i" and form[number + 2] == "n":
                del form[number + 2]
                del form[number + 1]
                form[number] = "sin"
            if character == "p" and form[number + 1] == "i":
                del form[number + 1]
                form[number] = math.pi
            if character == "a" and form[number + 1] == "n" and form[number + 2] == "s":
                del form[number + 2]
                del form[number + 1]
                # print(f"Prior Answer = {prioranswer}")
                form[number] = float(prioranswer)
            if character == "r" and form[number + 1] == "t":
                del form[number + 1]
                form[number] = "rt"
            # print(form)
            # print(f"numbercode = {numbercode}")

            try:
                newform.append(float(numbercode))
            except:
                if numbercode == "ignore":
                    pass
                else:
                    newform.append(form[number])
            numbercode = ""
            location += 1
        # print(newform)
        abcount /= 2
        pcount += abcount
        codelist = []
        lettercode = 0
        newnumberp = -1
        pnumber = -1
        pholder = []
        pstasis = []
        number = 0
        for value6 in newform:
            if value6 == "x":
                newform[number] = valuex
                # print(newform[number - 1])
                if type(newform[number - 1]) == float and number != 0:
                    # print("YES")
                    newform.insert(number, "*")
                    number -= 1
            number += 1
        number = 0
        for value7 in newform:
            # print("It Got HERE")
            # print(newform)
            try:
                if number != len(newform) - 1 and value7 == ")" and newform[number + 1] == "(":
                    # print("Here")
                    newform.insert(number + 1, "*")
            except:
                pass
            try:
                # print("Check HERE")
                # print(f"Newform[number] = {newform[number]}, value7 = {value7}")
                if number != len(newform) - 1 and value7 == ")" and int(newform[number + 1]):
                    # print("Here")
                    newform.insert(number + 1, "*")

            except:
                pass
            try:
                if number == 0 and value7 == "-" and newform[number + 1] == "(":
                    # print("wee")
                    newform[number] = -1
                    newform.insert(number + 1, "*")
                    number += 1
                # This will turn:  - (3) into -1 * (3)
                #
                elif number != len(newform) - 1 and value7 == "-" and newform[number + 1] == "(" and \
                        newform[number - 1] != ")" and (type(newform[number - 1]) != float):
                    newform[number] = -1
                    newform.insert(number + 1, "*")
                    # print("woo")

                    number += 1
                # tests for whether or not the character before is a number. In this case, it will change the minus
                # sign to: + -1 *         This is so if a variable follows it can be adjusted easily.
                elif number != len(newform) - 1 and value7 == "-" and number != 0 and (type(newform[number - 1]) == float or
                                                                       type(newform[number - 1]) == int):
                    newform.insert(number + 1, "*")
                    newform.insert(number + 1, -1)
                    newform[number] = "+"
                    # number += 2
                    # print("Here")
                # print(newform)
            except:
                pass
            # if value7 == ")" and number != len(newform) - 1:
            #     print(number)
            #     print(value7)
            #
            #     print(newform)
            #     print(newform[number])
            #     if testforletter(newform[number + 1]):
            #         newform.insert(number + 1, "*")
            number += 1
            # print(f"Newform = {newform}")
        # print(f"New Form is {newform}")
        # print(f"Newform 3: {newform}")
        numbersave = 0

        # Replaces all negative
        for value4 in newform:
            if (value4 == "-" and type(newform[numbersave - 1]) != float or value4 == "-" and numbersave == 0) and \
                    value4 == "-" and newform[numbersave - 1] != ")":
                newform[numbersave] = -1
                newform.insert(numbersave + 1, "*")
            numbersave += 1

        numbersave = 0
        # print(f"NEW FORM = {newform}")
        testcode = newform
        # print(f"Newform 2: {newform}")
        if pcount > 0:
            for value5 in newform:
                length = len(newform)
                try:
                    if (type(value5) == float) and numbersave != len(newform) - 1 and \
                            (newform[numbersave + 1] == "(" or newform[numbersave + 1] == "<"):
                        # if value5 == "(" and numbersave != 0 and type(newform[numbersave - 1] == float):
                        newform.insert(numbersave + 1, "*")
                        # print(f"Newform = {newform}")
                    #     print(numbersave)
                    # numbersave += 1
                    # print(f"Newform 2a: {newform}")
                    if (type(value5) == float) and type(newform[numbersave + 1]) == float and numbersave != len(
                            newform) - 1:
                        newform.insert(numbersave + 1, "*")
                    numbersave += 1
                    # print(f"Newform 2b: {newform}")
                except:
                    # print(f"It failed. Newform = {newform}")
                    pass

            # print("HELLO THERE")
            for value3 in range(0, int(pcount + abcount / 2)):
                newform = parenthesis(newform, 0, abcount)

        newnumber = -1
        # print(f"Newform 1: {newform}")
        for char in newform:
            newnumber += 1
            # while True:
                # if newform[newnumber + 1] == "sin" or newform[newnumber + 1] == "cos" or newform[newnumber + 1] == "tan":

            if char == "sin" or char == "cos" or char == "tan":
                # print(f"Newform = {newform}")
                newvalue = sct(char, newform[newnumber + 1])
                del newform[newnumber + 1]
                newform[newnumber] = newvalue
                if newnumber != 0 and type(newform[newnumber - 1] == float):
                    newform.insert(newnumber, "*")
            if char == "rt":
                if type(newform[newnumber - 1]) != float and type(newform[newnumber - 1]) != int:
                    newvalue = roots(roottype=2, equation=newform[newnumber + 1])
                    del newform[newnumber + 1]
                    newform[newnumber] = newvalue
            try:
                if (type(char) == int or type(char) == float) and newform[newnumber + 1] == "rt":
                    try:
                        newvalue = roots(roottype=newform[newnumber], equation=newform[newnumber + 2])
                    except(ZeroDivisionError):
                        pass
                    del newform[newnumber + 1]
                    del newform[newnumber + 1]
                    newform[newnumber] = newvalue
            except:
                pass

        # print(newform)
        # print("It Got HERE")
        newform = speak(newform)
        # print(divide_by_zero)
        if newform == "NaN" or isinstance(x, complex):
            self.answer = "NaN"

        # speak(newform)
        else:

            self.answer = newform[0]
