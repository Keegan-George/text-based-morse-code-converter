"""
A text-based Morse code converter that prompts the user to enter a phrase and then returns a new string in 
Morse, as per the International Morse code.
"""

from morse_code import morse_code_map


def morse_encoder(phrase: str) -> str:
    return "       ".join(
        [
            " ".join([morse_code_map.get(character, "") for character in word])
            for word in phrase
        ]
    )


user_input = input("Enter the phrase to be encoded in Morse Code:").upper().split()

print(f"Your converted phrase in Morse Code is: {morse_encoder(user_input)}")
