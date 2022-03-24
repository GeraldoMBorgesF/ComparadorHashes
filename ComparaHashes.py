import hashlib

print('#'*60)
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

#objeto hash que determina qual algoritmo de hash, p.ex. "sha1" ou "ripemd"
hash1 = hashlib.new('ripemd160')

#Verificar documentação https://docs.python.org biblioteca hashlib 'rb": r = read e b = binario
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'Oarquivo: {arquivo1} é diferente do arquivo {arquivo2}')

else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo {arquivo2}')

print('#'*60)

#a função hexdigest coloca o hash em hexadecimal
print('Hash de a.txt : {}'.format(hash1.hexdigest()))
print('Hash de b.txt : {}'.format(hash2.hexdigest()))
print('#'*60)