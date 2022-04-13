from ast import arg
from commands import *
import os
  
loop = True;

title = 'EezCMD BETA'
version = ' v.22.04.13'
today = datetime.now()
utime = today.strftime("%H:%M:%S - %Y/%m/%d")

os.system('cls')
os.system('title ' + title)
os.system('color 07')

print(title + version + ' - (c) Lil_Tim')
print('All rights reserved')
print('Session started at : ' + utime)

while True:
  path = os.getcwd()
  print()
  cmd = input( 'EEZ > ' + path + ' > ')
  print()

  if cmd == 'help':
    help()

  elif cmd == 'time' or cmd == 'date' or cmd == 'datetime':
    time()
  elif cmd == ' ' or cmd == 'clear' or cmd == 'cls':
    clear()

  elif cmd.startswith('ad') or cmd == cmd.startswith('add-directory') or cmd.startswith('add-dir'):
    if cmd.startswith('ad'):
      st = 'ad '
    elif cmd.startswith('add-directory'):
      st = 'add-directory '
    else:
      st = 'add-dir'
    dir = cmd.replace(st, '')
    ad(dir)

  elif cmd.startswith('gt') or cmd.startswith('goto'):
    if cmd.startswith('gt'):
      st = 'gt '
    else:
      st = 'goto '
    dir = cmd.replace(st, '')
    gt(dir)

  elif cmd.startswith('rd') or cmd.startswith('remove-dir') or cmd.startswith('remove-directory'):
    if cmd.startswith('rd'):
      st = 'rd '
    elif cmd.startswith('remove-dir'):
      st = 'remove-dir '
    else:
      st = 'remove-directory '
    dir = cmd.replace(st, '')
    rd(dir)

  elif cmd == 'le' or cmd == 'list-entries':
    le()

  elif cmd.startswith('le') or cmd.startswith('list-entries'):
    if cmd.startswith('le'):
      st = 'le '
    else:
      st = 'list-entries '
    dir = cmd.replace(st, '')
    lea(dir)

  elif cmd == 'color':
    os.system('color 07')

  elif cmd.startswith('color'):
    ucolor = cmd.replace('color ','')
    color(ucolor)

  elif cmd.startswith('ct') or cmd.startswith('colored-text'):
    if cmd.startswith('ct'):
      st = 'ct '
    else:
      st = 'colored-text '
    args = cmd.replace(st, '')

    args = args.split()
    if len(args) < 4:
      print('This command takes  4 arguments and you only have put '+str(len(args))+' arguments')
    else:
      for i in range(4, len(args)):
        args[3] += ' ' + args[i]
      ct(args[0], args[1], args[2], args[3])


  elif cmd.startswith('si') or cmd.startswith('sys-info') or cmd.startswith('system-informations'):
    if cmd.startswith('si'):
      st = 'si '
    elif cmd.startswith('sys-info'):
      st = 'sys-info '
    else:
      st = 'system-informations '
    arg = cmd.replace(st, '')
    arg = arg.replace('-', '')
    si(arg)

  elif cmd == 'exit' or cmd == '-':
    os.system('cls')
    break

  elif cmd == '':
    print('->')
  else:
    unknown(cmd)
