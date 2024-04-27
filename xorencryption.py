import math

characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]


def XOR(bit1,bit2):
    if bit1 == bit2:
      return '0'
    else:
      return '1'





def XORonByte(byte, key):
    emsg = ""


    for i in range(len(byte)):
        emsg += XOR(byte[i], key[i])


    return emsg






def XORonLetter(letter, keyLetter):
    letterbin = encode(letter)
    keyLetterbin = encode(keyLetter)


    eLetter = XORonByte(letterbin, keyLetterbin)

    return decode(eLetter)


print(XORonLetter("d", "r"))

def XORonSentence(sentence, key):

    Esentence= ""
    genKey = generateKey(sentence, key)

    for i in range(len(sentence)):
        Esentence += XORonLetter(sentence[i], genKey[i])
    return Esentence



def generateKey(message, key):
    if len(message) == len(key):
        return key

    elif len(message) < len(key):
    
        return key[0:len(message)]

    else:
        genkey =""
        rep = math.floor(len(message)/len(key))

        remain = len(message) % len(key)
        for i in range(rep):
            genkey += key

        genkey += key[ 0:remain]  
        
        return genkey


msg = input("Enter a Message")
key = input("Enter a Key:")


print("Your Encrypted Message is ", XORonSentence(msg, key))