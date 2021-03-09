def PyHelp():
    while True:
        from time import sleep
        print(f'\033[97;42m{"~" * 27}\n  SISTEMA DE AJUDA PyHelp  \n{"~" * 27}')
        cmd = str(input('\033[mFunção ou Biblioteca > ')).strip()
        if cmd == 'fim':
            print(f'\033[97;41m{"~" * 13}\n  ATÉ LOGO!  \n{"~" * 13}')
            break
        print(f'\033[97;44m{"~" * (len(cmd) + 36)}\n  Acessando o manual do comando "{cmd}"  \n{"~" * (len(cmd) + 36)}')
        sleep(0.5)
        print('\033[30;107m')
        help(cmd)


PyHelp()
