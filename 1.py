# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

def Delete_symbols(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = 'раз абвер забвение зимбабве незабвен два забвенный незабвенен незабвенный самозабвенен самозабвение \
    зимбабвийский самозабвенный самозабвенность три'

print(my_text)
my_text = Delete_symbols(my_text)
print(my_text)