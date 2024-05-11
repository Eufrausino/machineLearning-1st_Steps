palavra = "CasAco"
print(palavra.upper(), palavra.lower(), palavra.capitalize())

meiaPalavra = palavra[0:len(palavra)//2]
print(meiaPalavra)

ultimas_3_Letras = palavra[3:]
primeiras_3_Letras = palavra[:3]
reversedManual = palavra[len(palavra)::-1]

print(ultimas_3_Letras, primeiras_3_Letras, reversedManual)

c = palavra.replace('o','i')#precisa da variável para salvar o replace
print(c)

print(c.find('a'))
print(c.find('b'))

palavra2 = "   J A q u e ta "
f = palavra2.strip()
print(palavra2)
print(f)