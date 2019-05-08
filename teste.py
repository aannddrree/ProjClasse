from calculadora import Calculadora

def imprimir():
    print("VALOR A: {}".format(calculo.getA()))
    print("VALOR B: {}".format(calculo.getB()))
    print(" * = {}".format(calculo.multiplicar()))
    print(" / = {}".format(calculo.dividir()))
    print(" - = {}".format(calculo.subtrair()))
    print(" + = {}".format(calculo.somar()))

#INSTANCIAR CLASSE CALCULADORA
calculo = Calculadora(1,2)

#IMPRIMIR DADOS
imprimir()

#ALTERAR INFORMAÇÕES
calculo.setA(4)
calculo.setB(5)

#IMPRIMIR DADOS
imprimir()