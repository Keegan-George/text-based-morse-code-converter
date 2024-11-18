from morse_code import morse_code_map

user_input = input("Enter the phrase to be encoded in Morse code:").upper()

encrypted = [morse_code_map[character] for word in user_input for character in word]

print(f"Your converted phrase in morse code is: {''.join(encrypted)}")
