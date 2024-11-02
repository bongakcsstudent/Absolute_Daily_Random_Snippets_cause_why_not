# Daily (atmost Python shits): Decimal to Binary
user_input = int(input("Number here: "))  # Type conversion and input on the same line
bi_nu = ""  # Initialization

while user_input > 0:
    rem = user_input % 2
    bi_nu = str(rem) + bi_nu
    user_input = user_input // 2  #What tf is floor division i forgor


print("Binary:", bi_nu)

#Im refreshing my python brain so most of these would be done by our AI overlords
#Should I even pursue tech, given the job market idk 