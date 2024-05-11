capitais = {'RJ' : 'Rio de Janeiro', 'SP' : 'São Paulo',
            'MG' : 'Belo Horizonte', 'ES' : 'Vitória'}
print(capitais)

print(capitais['RJ'])
capitais['BA'] = 'Salvador'
print(capitais)

del(capitais)['SP']
print(capitais)
print(capitais.keys())
print(capitais.values())
print(capitais.items())

capitais2 = {'AM' : 'Manaus', 'RR' : 'Boa Vista'}
capitais.update(capitais2)
print(capitais)