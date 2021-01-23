#1/usr/bin/python3

'''

Cryptopals Challenge - Set 1 - Challenge 2: Fixed XOR

Author: Adam Klyne
Date: 23-Jan-21


'''

#
# Solution found at https://laconicwolf.com/2018/05/19/cryptopals-challenge-2-fixed-xor-in-python/
#

def bitwise_xor_bytes(a, b):
    result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

#
# Method for ensuring 8-bit binary conversion
#

def add_bits(a):
    if len(a)!=8:
        for i in range(8-len(a)):
            a ='0'+ a
    return a

#
# My method for manually computing the XOR of two input hex strings
#

def man_xor(a, b):
    output=''
    string_bin = ''
    key_bin = ''
    for i in range(0,len(a),2):
        string_bin = add_bits(format(int(a[i] + a[i+1],16), 'b'))
        key_bin = add_bits(format(int(b[i] + b[i+1], 16), 'b'))
        output += str(hex(int(string_bin,2)^int(key_bin,2))[2:])
    return output

#
# Main method to run code
#

def main():
    input_string = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    key = bytes.fromhex('686974207468652062756c6c277320657965')
    bin_string = '1c0111001f010100061a024b53535009181c'
    bin_key = '686974207468652062756c6c277320657965'
    expected_output = "746865206b696420646f6e277420706c6179"
    
    print(man_xor(bin_string, bin_key))
    print(bitwise_xor_bytes(input_string,key).hex())

if __name__ == '__main__':
    main()
    

