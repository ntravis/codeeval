"""
MORSE CODE
CHALLENGE DESCRIPTION: You have received a text encoded with Morse code and want to decode it.
INPUT SAMPLE: Your program should accept as its first argument a path to a filename. Input example is the following:
.- ...- ..--- .-- .... .. . -.-. -..-  ....- .....
-... .... ...--
Each letter is separated by space char, each word is separated by 2 space chars.
OUTPUT SAMPLE: Print out decoded words. E.g.
AV2WHIECX 45
BH3
"""
import sys
test_cases = open(sys.argv[1], 'r')
morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
         '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
         '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
         '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
         '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}
for test in test_cases:
    words = test.split("  ")
    overall = []
    for word in words:
        letters = word.split(" ")
        word = ""
        for letter in letters:
            word += str(morse.get(letter.strip()))
        overall.append(word)
    print ' '.join(overall)

test_cases.close()
