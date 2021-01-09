import sys
import datetime

def help():
    msg =  'epoch-converter help\n'
    msg += '\t Muestra la ayuda de la función\n'
    msg += 'epoch-converter epoch VALUE\n'
    msg += '\t Convierte VALUE (epoch timestamp) a formato fecha\n'
    msg += 'epoch-converter date VALUE\n'
    msg += '\t Convierte VALUE (fecha en formato MM/DD/YYYY-HH:MM:SS) a un epoch timestamp\n'
    return msg

def epoch2date(value):
    try:
        ts = datetime.datetime.fromtimestamp(int(value))
        return ts.strftime('%m/%d/%Y-%H:%M:%S')
    except:
        print('El valor debe ser un entero')
        exit(2)

def date2epoch(value):
    try:
        date, time = value.split('-')
        month,day,year = [int(i) for i in date.split('/')]
        h,m,s = [int(i) for i in time.split(':')]

        return int(datetime.datetime(year, month, day, h, m, s).timestamp())
    except ValueError as e:
        print(str(e))
        exit(2)

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print('Error no hay argumentos')
        exit(2)
    elif args[0] == 'help':
        print(help())
    elif len(args) < 2:
        print('Faltó el valor a convertir')
        exit(2)
    elif args[0] == 'epoch':
        print(epoch2date(args[1]))
    elif args[0] == 'date':
        print(date2epoch(args[1]))
    else:
        print('Operación no permitida')
        exit(2)

