#!/usr/bin/python3

def key_xor(msg_byte, key_byte):
    # XOR each character of the message byte with the rolling key
    return bytes([a ^ b for a, _b in zip(msg_byte, key_byte)])

 

def repeat_n(key, n):
    # create rolling key same length as byte_msg
   return (key * ((n//len(key))+1))+key[:n%len(key)]



def main():
    plaintext = 'Burning \'em, if you ain\'t quick and nimble\
                 I go crazy when I hear a cymbal'

    byte_msg = plaintext.encode('utf-8')
    ciphertext = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272\
                  a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

    key ='ICE' 

    byte_key = key.encode('utf-8')

    return_cypher = key_xor(byte_msg, repeat_n(byte_key, len(byte_msg)))
    print(return_cypher.hex())



if __name__=='__main__':
    main()
