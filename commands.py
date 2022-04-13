from datetime import *
import os

def help():
  print('Displays the list of all the commands avaible')
  print('\n|------------------------------------------------------------------------------------------------------------|')
  print('| COMMAND                                      | DESCRIPTION                                                 |')
  print('|------------------------------------------------------------------------------------------------------------|')
  print('| time                                         | Displays the actual time and date                           |')
  print('| date                                         | Displays the actual time and date                           |')
  print('| datetime                                     | Displays the actual time and date                           |')
  print('| [SPACE]                                      | Clears the console                                          |')
  print('| cls                                          | Clears the console                                          |')
  print('| clear                                        | Clears the console                                          |')
  print('| ad <dir>                                     | Creates the  specified directory                            |')
  print('| add-dir <dir>                                | Creates the  specified directory                            |')
  print('| add-directory <dir>                          | Creates the  specified directory                            |')
  print('| gt <dir>                                     | Goes to the specified directory (absolute or relative path) |')
  print('| goto <dir>                                   | Goes to the specified directory (absolute or relative path) |')
  print('| rd <dir>                                     | Removes the specified directory (absolute or relative path) |')
  print('| remove-dir <dir>                             | Removes the specified directory (absolute or relative path) |')
  print('| remove-directory <dir>                       | Removes the specified directory (absolute or relative path) |')
  print('| le {dir}                                     | List the entries of the specified directory                 |')
  print('| list-entries {dir}                           | List the entries of the specified directory                 |')
  print('| ct [red] [green] [blue] [text]               | List the entries of the specified directory                 |')
  print('| colored-text [red] [green] [blue] [text]     | List the entries of the specified directory                 |')
  print('| -                                            | Exits the console                                           |')
  print('| exit                                         | Exits the console                                           |')
  print('|------------------------------------------------------------------------------------------------------------|')
  print('\n<> : Required argument')
  print('{} : Optionnal argument\n')


def time():
  today = datetime.now()
  time = today.strftime("%d/%m/%Y %H:%M:%S")
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

def unknown(cmd):
  print('The command ' + cmd + ' doesn\'t exist, please check your syntax')