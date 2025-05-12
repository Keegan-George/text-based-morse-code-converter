"""
A text-based Morse code converter that prompts the user to enter a phrase and then returns a new string, Morses encoded,
as per the International Morse Code.
"""

from morse_code_map import morse_code_map

SPACES_BETWEEN_WORDS = " " * 7

def morse_encoder(phrase: list[str]) -> str:
    """Convert a list of strings into their Morse Code equivalent"""

    return SPACES_BETWEEN_WORDS.join(
        " ".join(morse_code_map.get(character, "") for character in word)
        for word in phrase
    )


user_input = input("Enter the phrase to be encoded in Morse Code: ").upper().split()

print(f"Your converted phrase in Morse Code is: {morse_encoder(user_input)}")
