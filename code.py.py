import os, sys, re
# ['qdqwd.as','mail.ru','ya.ru']
tpl = "^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$"
# регулярное выражение, означает что имя должно иметь ограничение на длину и состоять из разрешенных символов.

def usage():
  print("Ping3 - программа пингует три имени хостов.")
  print(" требуется три аргумента командной строки,")
  print(" имена хостов вводятся в командной строке вручную.")
  print("")

def regname(s):      #проверка допустимости доменного имени с помощью регулярного выражения
  global tpl
  if re.match(tpl, s) is not None:
    return True
    # Соответствует
  else:
    return False
    # Не соответствует

def pings():
  global host
  ret1 = os.system("ping -n 1 " + host[0])
  ret2 = os.system("ping -n 1 " + host[1])
  ret3 = os.system("ping -n 1 " + host[2])
  print("::Doing pings:::::::::::::")
  print("")
  print("False " if ret1 else "True  " ,host[0])
  print("False " if ret2 else "True  ", host[1])
  print("False " if ret3 else "True  ", host[2])

i = 1            #номер итерации
host = []        #список пустой


if len(sys.argv) != 4:
  if(len(sys.argv) != 1):
    print("Количество аргументов неверно. Пожалуйста, введите вручную.")
    #usage()
  usage()        #вывод объяснения, как работает программа
  while i < 4:     #цикл ввода=================
    print("Input host "+str(i)+": ", end="")
    line = input()
    if regname(line): 
        print(line+" cоответствует допустимому имени")
        host.append(line)
        i=i+1
    else:
        print(" не соответствует, введите снова")
else: 
  host.append(sys.argv[1])
  host.append(sys.argv[2])
  host.append(sys.argv[3])

print("")

pings()
