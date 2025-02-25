# Water State Checker
# Define a  water_state function that:

# (1) gets a temperature parameter
# (2) returns the string "Solid" if the temperature is less than or equal to 0
# (3) returns "Liquid" if the temperature is greater than 0, but less than 100.
# (4) returns "Gas" if the temperature is greater than or equal to 100.


def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif temperature > 0 and temperature < 100:
        return "Liquid"
    else:
        return "Gas"