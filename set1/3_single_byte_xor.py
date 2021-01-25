#!/usr/bin/python3

'''

Cryptopals Challenge - Set 1 - Challenge 3: Single XOR

Author: Adam Klyne
Date: 23-Jan-21


'''

def calc_score(message):
    letter_freq = {
        'a': 8.4966, 'b': 2.0720, 'c': 2.5388, 'd': 3.3844,
        'e': 1.1607, 'f': 1.8121, 'g': 2.47053, 'h': 3.0034,
        'i': 7.5448, 'j': 0.1965, 'k': 1.1016, 'l': 5.4893,
        'm': 3.0129, 'n': 6.6544, 'o': 7.1635, 'p': 3.1671,
        'q': 0.1962, 'r': 7.5809, 's': 5.7351, 't': 6.9509,
        'u': 3.6308, 'v': 1.0074, 'w': 1.2899, 'x': 0.2902,
        'y': 1.7779, 'z': 0.2722
    }

    output = 0
    
    for byte in message:
      
        output+=letter_freq.get(byte, 0)
      
    #for i in range(len(xor_message)):
        

    return output





def single_xor(byte_msg, key):
    output = b''
    for b in byte_msg:
        output += bytes([b^key])
    return output




def main():


    input_hex = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    
    top_char = 0
    top_score = 0
    top_message = ''

    for i in range(32, 127):
        message = single_xor(input_hex, i)
        score = calc_score(message.decode())
        if score > top_score:
            top_score = score
            top_char = i
            top_message = message
    
    print('The most likely key is ASCII character: {}\n with a score of: {}\nThe plaintext is: {}'.format(chr(top_char), top_score, top_message))

    

if __name__ == '__main__':
    main()
