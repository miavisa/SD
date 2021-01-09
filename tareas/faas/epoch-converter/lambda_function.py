import json
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
        return 'The value must be an integer', 400

def date2epoch(value):
    try:
        date, time = value.split('-')
        month,day,year = [int(i) for i in date.split('/')]
        h,m,s = [int(i) for i in time.split(':')]

        ts = int(datetime.datetime(year, month, day, h, m, s).timestamp())
        return f'{ts}', 200
    except ValueError as e:
        return str(e), 400
        
def handle_output(res):
    msg, code = res
    return {
        'statusCode': code,
        'body': msg
    }


def lambda_handler(event, context):

    args = event.split()
    print(args)

    if not args:
        return handle_output(('There are no arguments', 400))

    if args[0] == 'help':
        return handle_output(help())

    if len(args) < 2:
        msg = 'Is ncessary provide the format and the value to convert'
        return handle_output((msg, 400))
    
    if args[0] == 'epoch':
        return handle_output(epoch2date(args[1]))
    elif args[0] == 'date':
        return handle_output(date2epoch(args[1]))
    else:
        return handle_output(('Format/operation not supported', 400))

