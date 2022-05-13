from datetime import date
from re import M

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]


hotelLakewood = 3


hotelBridgewood = 4


hotelRidgewood = 5
zlakefi=0
bridgfi =0
ridgefi = 0
zlakenormal =0 
bridgnormal=0
ridgenormal=0
print('############################################################################################')
print('############################################################################################')
print('##    ___   ___   ___   ___   ___  __   __    _       _  _    ___    _____   ___   _      ##')
print('##   | _ \ | __| / __| | __| | _ \ \ \ / /   /_\     | || |  / _ \  |_   _| | __| | |     ##')
print('##   |   / | _|  \__ \ | _|  |   /  \ V /   / _ \    | __ | | (_) |   | |   | _|  | |__   ##')
print('##   |_|_\ |___| |___/ |___| |_|_\   \_/   /_/ \_\   |_||_|  \___/    |_|   |___| |____   ##')
print('############################################################################################')
print('############################################################################################')



i = int(input('Quantos dias dejesa fazer um reserva:  '))
while (i>0):

    print('--------------------Digite a data da reserva--------------------------------')
    y= int(input('Digite o ano:  '))
    m=int(input('Digite o mês:  '))
    d = int(input('Digite o dia:  '))
    data = date(y, m, d)
    print('Data: ',data)
    indice_da_semana = data.weekday()
    
    dia_da_semana = DIAS[indice_da_semana]
    print('Dia: ',dia_da_semana)
    print('--------------------------------------------------------------------------------')
    numero_do_dia_da_semana = data.isoweekday()
    
    i=i-1

    if numero_do_dia_da_semana >5:
     #fim de semana fidelidade   
        zlakefi = zlakefi + 80
        bridgfi = bridgfi + 50
        ridgefi = ridgefi + 40
    # fim de semana normal    
        zlakenormal = zlakenormal + 90
        bridgnormal = bridgnormal + 60
        ridgenormal = ridgenormal + 150
       






    else:
# dia de semana com fidelidade        
        zlakefi = zlakefi + 80
        bridgfi = bridgfi + 110
        ridgefi = ridgefi + 100
#dia de semana normal
        zlakenormal = zlakenormal + 110
        bridgnormal = bridgnormal + 160
        ridgenormal = ridgenormal + 220


        
    
    

list1= [zlakefi, bridgfi, ridgefi]
list2= [zlakenormal,bridgnormal, ridgenormal]

print('---------------------------------------------------------------------------------')
print('Qual sua categoria de cliente?')
tipo_do_cliente = int(input('Digite 1 - Reward ou 2 - regular : '))
print('---------------------------------------------------------------------------------')
print('-------######-----o hotel-----######---------------------------------------------')

if tipo_do_cliente == 1:

    if zlakefi == bridgfi and zlakefi < ridgefi:
        print('Os hoteis LAKEWOOD E BRIDGEWOOD possuem o mesmo preço de R$',zlakefi, 'mas recomendamos o BRIDGEWOOD, pois possui a melhor classificação do serviço.')
    
    if zlakefi == ridgefi and bridgfi > ridgefi:
        print('Os hoteis LAKEWOOD E BRIDGEWOOD possuem o mesmo preço de R$',zlakefi, 'mas recomendamos o RIDGEWOOD, pois possui a melhor classificação do serviço.')
      
    if ridgefi == bridgfi and zlakefi>bridgfi:
        print('Os hoteis LAKEWOOD E BRIDGEWOOD possuem o mesmo preço de R$',ridgefi, 'mas recomendamos o RIDGEWOOD, pois possui a melhor classificação do serviço.')
    
    else:
        if min(list1) == zlakenormal:
            print('O hotel mais barato Lakewoow ',min(list1))
        elif min(list1) == bridgnormal:
            print('O hotel mais barato Bridgewood ',min(list1))
        else: 
            print('O hotel mais barato Ridgewood ',min(list1))
    
else:
    if zlakenormal == bridgnormal and zlakefi < ridgefi:
        print('Os hoteis LAKEWOOD E BRIDGEWOOD possuem o mesmo preço de R$',zlakenormal, ',mas recomendamos o BRIDGEWOOD, pois possui a melhor classificação do serviço.')

    if zlakenormal == ridgenormal and bridgfi > ridgefi:
        print('Os hoteis LAKEWOOD E BRIDGEWOOD possuem o mesmo preço de R$',zlakenormal, 'mas recomendamos o RIDGEWOOD, pois possui a melhor classificação do serviço.')
    
    if ridgenormal == bridgnormal and zlakefi>bridgfi:
        print('Os hoteis LAKEWOOD E BRIDGEWOOD possuem o mesmo preço de R$',ridgenormal, 'mas recomendamos o RIDGEWOOD, pois possui a melhor classificação do serviço.')
    else:
        if min(list2) == zlakenormal:
            print('O hotel mais barato Lakewoow ',min(list2))
        elif min(list2) == bridgnormal:
            print('O hotel mais barato Bridgewood ',min(list2))
        else:
            print('O hotel mais barato Ridgewood ',min(list2))

