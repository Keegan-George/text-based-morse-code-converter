from morse_code import morse_code_map

user_input = input("Enter the phrase to be encoded in Morse Code:").upper().split()

morse_encrypted = "       ".join(
    [
        " ".join([morse_code_map.get(character, "") for character in word])
        for word in user_input
    ]
)

print(f"Your converted phrase in Morse Code is: {morse_encrypted}")
