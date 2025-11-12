# Define the input string
input_string = "Hello World"

# Print original string
print("Original String:", input_string)

# Perform AND operation with 127 on each character
and_result = ""
print("\nAND Operation with 127:")
for char in input_string:
    # Convert character to ASCII using ord(), perform bitwise AND with 127, and convert back to character
    and_char = chr(ord(char) & 127) #72 & 127 =72 H
    and_result += and_char
    print(f"{char} ({ord(char)}) & 127 = {ord(and_char)} -> '{and_char}'")

# Perform XOR operation with 127 on each character A'B+AB'
xor_result = ""
print("\nXOR Operation with 127:")
for char in input_string:
    # Convert character to ASCII using ord(), perform bitwise XOR with 127, and convert back to character
    xor_char = chr(ord(char) ^ 127)
    xor_result += xor_char
    print(f"{char} ({ord(char)}) ^ 127 = {ord(xor_char)} -> '{xor_char}'")

# Final transformed strings
print("\nResultant String after AND with 127:", and_result)
print("Resultant String after XOR with 127:", xor_result)
