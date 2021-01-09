import sys
import datetime

def help():
    msg =  'epoch-converter help\n'
    msg += '\t Muestra la ayuda de la función\n'
    msg += 'epoch-converter epoch VALUE\n'
    msg += '\t Convierte VALUE (epoch timestamp) a formato fecha\n'
    msg += 'epoch-converter date VALUE\n'
    msg += '\t Convierte VALUE (fecha en formato MM/DD/YYYY-HH:MM:SS) a un epoch timestamp\n'
    return msg, 200

def epoch2date(value):
    try:
        ts = datetime.datetime.fromtimestamp(int(value))
        return ts.strftime('%m/%d/%Y-%H:%M:%S'), 200
    except:
        return 'The value must be an integer\n', 400

def date2epoch(value):
    try:
        date, time = value.split('-')
        month,day,year = [int(i) for i in date.split('/')]
        h,m,s = [int(i) for i in time.split(':')]

        ts = int(datetime.datetime(year, month, day, h, m, s).timestamp())
        return f'{ts}\n', 200
    except ValueError as e:
        return f'{str(e)}\n', 400

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    args = req.split()

    if not args:
        return 'There are no arguments\n', 400

    if args[0] == 'help':
        return help()

    if len(args) < 2:
        msg = 'Is ncessary provide the format and the value to convert\n'
        return msg, 400
    
    if args[0] == 'epoch':
        return epoch2date(args[1])
    elif args[0] == 'date':
        return date2epoch(args[1])
    else:
        return 'Format/operation not supported\n', 400
