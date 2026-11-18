from formula import Math
answer = 0
formerequation = 0
while True:
    # input()
    # equation = "3|4 * (2 + 6)|"
    x = 5
    equation = input("Equation:")
    if equation == "=":
        newequation = Math(formerequation, x, answer)
    else:
        newequation = Math(equation, x, answer)

    print(f"{newequation.answer}")
    if equation != "=":
        formerequation = equation
    answer = newequation.answer


# # z = 10
# # x = f"Hello {z}"
# # z = 11
# # print(x)

# for value2 in code[2::]:
#     print(f"-------------------{value2}")

# value = [1, 2]
# print(type(value))