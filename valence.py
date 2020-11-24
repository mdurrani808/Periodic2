from mendeleev import element
import chemparse

tempElem = element("H")
tempMult = 0
totalValence = 0
counter = 0
inputThing = ""

while (inputThing != "0"):
    try:
        inputThing = input("Enter Formula:")
        formula = chemparse.parse_formula(inputThing)
        for k, v in formula.items():
            tempElem = element(k)
            tempMult = v
            totalValence = (tempElem.nvalence() * tempMult) + totalValence

        print(totalValence)
        totalValence = 0
    except:
        print("Error! Try Again.")
