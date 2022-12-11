import sys
sys.path.insert(1, "/Users/Svetlana/PythonLearning/Caesar Encryptor/application")
import caesar_encryptor as ce

    


ce.set_alphabet()
print('encrypt char tests:')
print(ce.en_de_crypt_char('ш', 'а', 1, 'рус') == 'б')
print(ce.en_de_crypt_char('д', 'а', 1, 'рус') == 'я')
print(ce.en_de_crypt_char('ш', 'a', 1, 'eng') == 'b')
print(ce.en_de_crypt_char('ш', 'A', 1, 'eng') == 'B')

print('encrypt string tests:')
print(ce.create_new_string('ABBA', 'ш', 1, 'eng') == 'BCCB')
print(ce.create_new_string('ABBA, b', 'ш', 1, 'eng') == 'BCCB, c')

print('when ROT is unknown')
for ROT in range(26):
    print(ce.create_new_string('Hawnj pk swhg xabkna ukq nqj.', 'д', ROT, 'eng'), sep='')
