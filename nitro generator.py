import random, string

print('Bienvenue dans le gen de >"Arizaki.exe#1504\n')
amount = int(input('Combien de nitros UNCHECK veux-tu générer ?: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Nitro uncheck.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[GEN BY  >"Arizaki.exe#1504] {code}')
    value += 1

print('\n') ; print(f'dis moi merci, tu viens de générer {value -1} nitros uncheck\n ') ; print('Les codes ont été sauvegardé dans fichier ce nomant Nitro uncheck.txt\n')
print('by >"Arizaki.exe#1504\n')

input()
exit()

