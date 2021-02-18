#!/usr/bin/python3

'''

Cryptopals Challenge - Set 1 - Challenge 1: Convert hex to base64

Author: Adam Klyne
Date: 23-Jan-21

'''
#
# import classes
#
 
import base64

#
# main method to run the code
#

def main():
   
    input_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_output = bytes('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t', 'utf-8')

    output = base64.b64encode(bytes.fromhex(input_hex))

    if output==expected_output:
        print('Success')
    else:
        print('Try again\n')

if __name__ == '__main__':
    main()