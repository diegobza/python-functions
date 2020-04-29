from pessoal import functions


def main():
    print(functions.is_cpf('055.885.524-58'))
    print(functions.is_cpf('055,885.524/58'))
    print(functions.is_cpf('05588552458'))
    print(functions.is_cpf('5588552458'))


if __name__ == '__main__':
    main()
