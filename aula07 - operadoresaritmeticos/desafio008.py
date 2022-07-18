metros = float(input('Digite o valor em metros: '))

cm = metros * 100
mm = metros * 1000

print('O valor de {} metro(s) é igual a {} cm e {} mm.'.format(metros, cm, mm))

######## Extra ########

km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.1
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('{} metros é igual: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(metros, km, hm, dam, dm, cm, mm))
