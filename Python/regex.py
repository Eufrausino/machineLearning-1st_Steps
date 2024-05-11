import re

frase = 'Olá, meu nome é Dorival Estevão, meu número é (67)98484-9017'
email = 'Claro! O e-mail da empresa é empresaEmpresarialEmpresaMesmo@genmail.com'
carro = "Catapimbas! Aquele carro bateu no meu e fugiu! A placa do meliante é RBD3R24"
carro2 = "Você viu o meu carro? A placa dele é FFS-1010, me avise caso o encontre"

print(re.search('\(\d{0,2}\)\d{4,5}\-\d{4}', frase))
print(re.search('\w+@\w+\.\w+', email))
print(re.search('\w+@\w+\.com', email))#Alternativa
print(re.search('\w{0,3}\d\w\d{0,2}', carro))
print(re.search('[A-Z]\w+-\d{4}',carro2))
print(re.search('[A-Za-z]{3}-\d{4}',carro2))#Alternativa que pega letras minúsculas

telefone = "(88)90019-5544 é o meu número"
print(re.match("\(\d{2}\)\d{5}-\d{4}", telefone))
print(re.match("\(\d{2}\)\d{5}-\d{4}", frase))#Match só pega se estiver no começo da string

frase2 = "Olá! Sou Clodoaldo, meu e-mail principal é clodogames@memail.com e meu telefone é (69)98989-0010. Meu e-mail secundário é clododo@email.com"
print(re.findall("\w+@\w+\.com", frase2))

emails = '''princessinha66@email.com
cad777@memail.com
mat@vicmail.com
lucy@email.com
lilyVt@memail.com
'''

print(re.findall("\w+\d*@\w+\.com", emails))
