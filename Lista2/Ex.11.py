#11. Faça um algoritmo para calcular, considerando que o usuário informe a idade (inteira), as seguintes informações sobre o usuário:
#a. Número de semestres;
#b. Número de meses;
#c. Número de semanas;
#d. Número de dias;
#e. Número de horas;
#f. Número de minutos;
#g. Número de segundos;
#No final deseja-se visualizar todos os cálculos realizados e também se o usuário é infantil, adolescente, jovem ou adulto. A tabela abaixo demonstra as idades que defini essas categorias: Até 12 Infantil, 13 a 16 Adolescente, 17 a 20 Jovem, 21 a 50 Adulto e acima de 50 Idoso

#Resposta:
idade = int(input('Digite sua idade:'))

semestres = idade * 12 / 6
meses = idade * 12
semanas = idade * 52
dias = idade * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print('\nVocê tem', idade, 'anos,', semestres, 'semestres,', meses, 'meses,', semanas, 'semanas,', dias, 'dias,', horas, 'horas,',minutos,'minutos e',segundos,'segundos')

if idade <= 12:
  print('\nInfantil')
else:
 if idade >= 13 and idade <= 16:
  print('\nAdolescente')
 else:
  if idade >= 17 and idade <= 20:
   print('\nJovem')
  else:
   if idade >= 21 and idade <= 50:
    print('\nAdulto')
   else:
     print('\nIdoso')