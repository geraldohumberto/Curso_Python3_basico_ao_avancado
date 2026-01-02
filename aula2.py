# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="-", end='\r\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')


# Mostrando modelo com Hastag e o comportamento de fim de linha
print(12, 34, 1011, sep="-", end='##')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

# Mostrando modelo com Hastag e o comportamento de fim de linha
print(12, 34, 1011, sep="-", end='##\n')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

# Mostrando modelo com Hastag e o comportamento de fim de linha
print(12, 34, 1011, sep="-", end='\n##')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')