alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
original_text = input("Type your message: ").lower()
shift_number = int(input("Enter shift number: "))

def encrypt(original_text,shift_number):
    encrypted_word = ""
    for index in original_text:
        if index.isalpha():
            index_alphabet = alphabet.index(index)
            if index_alphabet+shift_number >= len(alphabet):
                index_alphabet = index_alphabet+shift_number - len(alphabet)
                encrypted_letter = alphabet[index_alphabet]
                encrypted_word = encrypted_word + encrypted_letter
            else:
                encrypted_letter = alphabet[index_alphabet+shift_number]
                encrypted_word= encrypted_word + encrypted_letter
        else:
            encrypted_word = encrypted_word + index

    print(f"The encrypted_word is: {encrypted_word}")
    return encrypted_word


def decrypt(original_text,shift_number):
    decrypted_word = ""
    for index in original_text:
        if index.isalpha():
            index_alphabet = alphabet.index(index)-shift_number
            decrypted_letter = alphabet[index_alphabet]
            decrypted_word = decrypted_word + decrypted_letter
        else:
            decrypted_word = decrypted_word + index

    print(f"Decrypted word: {decrypted_word}")


def ceaser(original_text,shift_number,decode_or_encode):
    if decode_or_encode == "encode":
        return encrypt(original_text,shift_number)
    elif decode_or_encode == "decode":
        decrypt(original_text,shift_number)


encrypted_word = encrypt(original_text,shift_number)
decrypt(encrypted_word,shift_number)
enc_word = ceaser(original_text,3,"encode")
ceaser(enc_word,3,"decode")