# Match-Case with Bitwise Operator
# This one is similar to a previous exercise, but it uses the bitwise OR (|) operator in addition.  In the coding area, we have defined a country variable.  Below that line, write a match-case block that:

# (1) checks the value of the country variable, and

# (2) prints out Hello if the value of country is "USA" or "United States",

# (3) prints out Ciao if the value of country is "Italy",

# (4) prints out Hallo if the value of country is "Germany".


country = "USA"

match country:
    case "USA" | "United States":
        print("Hello")
    case "Italy":
        print("Ciao")
    case "Germany":
        print("Hallo")
    case _:
        print("Whatever")