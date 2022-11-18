# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def informacoes_menu():
    print('Operações disponiveis ')
    print('+ Adição')
    print('/ Divisão ')
    print('- Subtração')
    print('** potencia')
    print('* Multiplicação')
    print('r  raiz quadrada')
    print('% Percentagem')
    print('= ')

def eNumero ( valor ) :
    if not valor.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():
        return False
    try:
        float(valor)
    except ValueError:
        return False
    return True


def pedir_numero():
    print('Insira um numero ')
    numero = input()
    return numero

def pedir_op(numero):
    print('Insira uma operacao')
    operacao = input()

    if operacao == '**' or operacao == '+' or operacao == '-' or operacao == 'r' or operacao == '%'or operacao == '/'or operacao == '*' or operacao == '=':
        return operacao

    print('Não existe esta operação')
    return pedir_op(numero)




def potencia(numero):
    base = int(numero)
    print('Insira o expoente')
    expo = input()
    if(eNumero(expo)) :
        potenciaResult = 1
        for count in range(int(expo)):
            potenciaResult *= base
            count += 1
    
        return potenciaResult
    else:
        print("Este expoente não é valido")
        return potencia(numero)
        

def raiz(numero):

    if numero > 0:
        return math.sqrt(numero)
    else:
        print('Nao pode ter numeros negativos')
        return 0

def op_diferente(operacao) :
    if (operacao =='r' or operacao =='**'):
        print("Precisa de escolhe outra operação ")
        return pedir_op(operacao)

def percentagem(numero):
    print("percentagem de valor:")
    perc = float(numero)
    value = float(input('Insira o valor : '))
    result = (value * perc) / 100
    print(f'{perc} % de {value} é = {result}')




def resultado(conta) :
    if(len(conta)>1):
       print(eval(conta[0:len(conta)-1]))
    print('Resultado: '+ conta)







def pedir_conta():
    # Use a breakpoint in the code line below to debug your script.
    informacoes_menu()
    operacao = ' '
    conta = ''
    while operacao != '=':
            numero=pedir_numero()
            if(eNumero(numero)):
                operacao = pedir_op(numero)

                if operacao == '**':
                    numero = potencia(numero)
                    operacao = op_diferente(operacao)

                    print(conta)

                if operacao == 'r':
                    numero=raiz(float(numero))
                    if (numero == 0):
                        numero= pedir_numero()
                    operacao = op_diferente(operacao)

                    print(conta)

                conta = conta + str(numero) + str(operacao)


                print(conta)

                if operacao == '%':
                    percentagem(numero)
                    break
            else:
                print('Não é um numero')

            if(operacao != '%'):
                resultado(conta)
    # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pedir_conta()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
