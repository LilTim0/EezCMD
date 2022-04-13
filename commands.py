from datetime import *
import os
import platform
from traceback import print_tb

def help(arg):
  if arg == '':
    arg = '1'

  print('Displays the list of all the commands avaible')
  print('\n|------------------------------------------------------------------------------------------------------------------|')
  print('| COMMAND                                            | DESCRIPTION                                                 |')
  print('|------------------------------------------------------------------------------------------------------------------|')
  if arg == '1':
    print('| time                                               | Displays the actual time and date                           |')
    print('| date                                               | Displays the actual time and date                           |')
    print('| datetime                                           | Displays the actual time and date                           |')
    print('| SPACE                                              | Clears the console                                          |')
    print('| cls                                                | Clears the console                                          |')
    print('| clear                                              | Clears the console                                          |')
    print('| ad <dir>                                           | Creates the  specified directory                            |')
    print('| add-dir <dir>                                      | Creates the  specified directory                            |')
    print('| add-directory <dir>                                | Creates the  specified directory                            |')
    print('| gt <dir>                                           | Goes to the specified directory (absolute or relative path) |')
    print('| goto <dir>                                         | Goes to the specified directory (absolute or relative path) |')
    print('| rd <dir>                                           | Removes the specified directory (absolute or relative path) |')
    print('| remove-dir <dir>                                   | Removes the specified directory (absolute or relative path) |')
    print('| remove-directory <dir>                             | Removes the specified directory (absolute or relative path) |')
    print('| le {dir}                                           | List the entries of the specified directory                 |')
    print('| list-entries {dir}                                 | List the entries of the specified directory                 |')
    print('| ct [red] [green] [blue] [text]                     | List the entries of the specified directory                 |')
    print('| colored-text [red] [green] [blue] [text]           | List the entries of the specified directory                 |')
    print('| fo [file] [mode]                                   | Makes several different operations on the specified file    |')
    print('| file-operation [file] [mode]                       | Makes several different operations on the specified file    |')
  elif arg == '2':
    print('| foa [file] [file2/text] [mode]                     | Makes several different operations on the specified files   |')
    print('| file-operation-advanced [file] [file2/text] [mode] | Makes several different operations on the specified files   |')
  print('|------------------------------------------------------------------------------------------------------------------|')
  print('\n[] : Required argument')
  print('{} : Optionnal argument                                                                                       Page ' + arg + '\n')


def time():
  today = datetime.now()
  time = today.strftime("%Y/%m/%d %H:%M:%S")
  print(time)           
  
def clear():
  os.system('cls')
  
def ad(dir):
  path = os.path.realpath(os.getcwd())
  if os.path.exists(os.path.join(path, dir)):
    print('Creation failed, this directory already exists')
  
  else:
    os.makedirs(dir)
  
def gt(dir):
  path = os.path.realpath(os.getcwd())
  
  if not os.path.exists(os.path.join(path, dir)):
    print('You can\'t open this directory, it doesn\'t exist');
  else:
    os.chdir(os.path.join(path, dir))
    
def rd(dir):
  path = os.path.realpath(os.getcwd())
  if not os.path.exists(os.path.join(path, dir)):
    print('You can\'t remove a directory who doesn\'t exist')
  
  else:
    if len(os.listdir(os.path.join(path, dir)) ) != 0:
      print('You can\'t remove a directory if it is not empty')
    else:
      os.rmdir(dir)
      
def le():
  path = os.path.realpath(os.getcwd())
  le = os.listdir(path)
  for i in range(len(le)):
    print(le[i])
  print()

def lea(dir):
  path = os.path.realpath(os.getcwd())
  if not os.path.exists(os.path.join(path, dir)):
    print('You can\'t list the entries of a directory who doesn\'t exist')
  
  else:
    le = os.listdir(os.path.join(path, dir))
    for i in range(len(le)):
      print(le[i])
    print()
  
def color(colors):
  os.system('color ' + colors)

def ct(r, g, b, text):
  print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))

def si(arg):
  if arg == '*':
    syst = platform.uname()
    print('Operating System :\n' + syst[0])
    print('\nName             :\n' + syst[1])
    print('\nVersion          :\n' + syst[2])
    print('\nVersion (detail) :\n' + syst[3])
    print('\nArchitecture     :\n' + syst[4])
    print('\nProcessor        :\n' + syst[5])

  elif arg == 'arc':
    print('Architecture :\n' + platform.machin())
  
  elif arg == 'version':
    print('Version :\n' + platform.version())

  elif arg == 'osd':
    print('Operating System (detail) :\n' + platform.platform())

  elif arg == 'os':
    print('Operating System :\n' + platform.system())

  elif arg == 'processor':
    print('Processor :\n' + platform.processor())

  elif arg == 'ldrives':
    ldrives = ''
    drives = [ chr(x) + ':\\' for x in range(65,91) if os.path.exists(chr(x) + ':')]
    for i in drives:
      ldrives += i + ' '
    print('Logical drives :\n' + ldrives)

  elif arg == '?':
    print('Arguments :')
    print('-*         -> Displays all the system informations')
    print('-arc       -> Displays the architecture informations')
    print('-version   -> Displays the operating system version')
    print('-osd       -> Displays the operating system detail informations')
    print('-os        -> Displays the operating system informations')
    print('-processor -> Displays the processor informations')
    print('-ldrives   -> Displays all the accessible logical drives')

  else:
    print('The argument ' + arg +' doesn\'t exist, please check your syntax')

def fo(file, mode):
  text = ''
  if mode == 'r':
    if not os.path.exists(file):
      print('You can\'t read a file who does not exist')
    else:
      with open(file, mode) as rf:
        lines = rf.readlines()
        for i in lines:
          text += i;
        if text == '':
          text = 'The file ' + file + ' is empty'
  
  elif mode == 'a':
    if not os.path.exists(file):
      print('You can\'t append something to a file who does not exist')
    else:
      with open(file, 'r') as rf:
        lines = rf.readlines()
        for i in lines:
          text += i
      with open(file, 'w') as xf:
        temp = text
        text = input('> ' + temp)
        xf.write(temp + text)
        text = ''
        
        
  elif mode == 'w':
    if not os.path.exists(file):
      mode = 'x'
    with open(file, mode) as xf:
      text = input('> ')
      xf.write(text)
      text = ''

  elif mode == 'c':
    with open(file, 'x') as xf:
      xf.write('')

  elif mode == 'rm':
    if not os.path.exists(file):
      text = 'You can\'t remove a file who does not exists'
    else:
      os.remove(file)

  elif mode == '?':
    print('Modes :')
    print('-r  -> Reads the content of the specified file')
    print('-w  -> Write some content in the specified file')
    print('-a  -> Append some content to the specified file')
    print('-c  -> Create the specified file')
    print('-rm -> Removes the specified file')

  return text

def foa (file, sfile, mode):
  if mode == 'ct':
    text = ''
    with open(sfile, 'r') as rf:
      content = rf.readlines()
      for i in content:
        text += i

    if not os.path.exists(file):
      with open(file, 'x') as xf:
        xf.write('')
    with open(file, 'w') as wf:
      wf.write(text)

  elif mode == 'cat':
    text = ''
    basis = ''
    with open(file, 'r') as rf:
      content = rf.readlines()
      for i in content:
        basis += i

    if not os.path.exists(sfile):
      print('You can\'t append something to a file who does not exist')
    else :
      with open(sfile, 'r') as rf:
        content = rf.readlines()
        for i in content:
          text += i

    with open(file, 'w') as wf:
      temp = basis + text 
      wf.write(temp)

  elif mode == 'sif':
    cont = ''
    with open(file, 'r') as rf:
      content = rf.readlines()
      for i in content:
        cont += i

    findStr = cont.replace(sfile, '')
    find = False
    for i in findStr:
      if i == '':
        find = True

    if find == True:
      print(sfile + ' has been found in ' + file)
    else:
       print(sfile + ' has not been found in ' + file)

  else:
    print('The argument ' + mode + ' is unknown, please check your syntax')

def unknown(cmd):
  print('The command ' + cmd + ' doesn\'t exist, please check your syntax')
