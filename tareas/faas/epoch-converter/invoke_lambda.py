#!/usr/local/opt/python@3.8/bin/python3.8
# -*- coding: utf-8 -*-

import boto3
import sys
import json

if __name__ == '__main__':
    args = sys.argv[1:]

    session = boto3.Session(profile_name='miavisa', region_name='us-east-1')
    client = session.client('lambda')

    payload = ' '.join(args)
    bin_res = client.invoke(FunctionName='epoch-converter',
                            Payload=f'"{payload}"')['Payload'].read()
    str_res = bin_res.decode("utf-8")
    res = json.decoder.JSONDecoder().decode(str_res)
    code = res['statusCode']
    msg = res['body']
    if code == 200:
        print(msg)
    else:
        print(f'Server returned unexpected status code: {code} - {msg}')
    