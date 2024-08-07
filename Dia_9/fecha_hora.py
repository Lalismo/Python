from datetime import datetime, date

fecha = datetime(2025,5,15,22,10,15,2500)

fecha = fecha.replace(month=12)
print(fecha)

#Calcular fechas
nacimiento = date(1995, 3, 5)
defuncion =  date(2095, 6, 19)

vida = defuncion - nacimiento
print(vida)
print('----------')

despierta =  datetime(2022, 10, 5, 7,30)
duerme = datetime(2022,10,5,23,45)

vigilia = duerme - despierta
print(vigilia)