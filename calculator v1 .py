from time import sleep
    
def main():
    print("-==" * 14)
    print("          BIG CASTAS CALCULADORA          ")
    print("-==" * 14)
    
    def soma():
        return num_1 + num_2
    def subtracao():
        return num_1 - num_2
    def divisao():
        return num_1 / num_2
    def multiplicacao():
        return num_1 * num_2
    def potenciacao():
        return num_1 ** num_2
    def raiz():
        return num_1 ** (1 / num_2)
    def sair():
        quit()
        

    while True:
        print("-" * 5)
        print("Bora lá!")
        print("-" * 5)
        sleep(1)
        num_1 = float(input("Insira o Primeiro valor: "))
        num_2 = float(input("Insira o Segundo valor: "))
        print("{} ? {} = \n".format(num_1, num_2))
        
        print("[ 1 ] Soma | + \n[ 2 ] Subtração | - \n[ 3 ] Divisão | / \n[ 4 ] Multiplicação | x \n[ 5 ] Potenciação | ¹ ² ³ \n[ 6 ] Raiz | ²V \n[ 0 ] Sair da Calculadora \n")
        
        processo = int(input("Escolha a operação: "))
        
        if processo == 1:
            
            print("{} + {} = {}".format(num_1, num_2, soma()))
        elif processo == 2:
            
            print("{} - {} = {}".format(num_1, num_2, subtracao()))
        elif processo == 3:
    
            print("{} / {} = {}".format(num_1, num_2, divisao())) 
        elif processo == 4:
            
            print("{} x {} = {}".format(num_1, num_2, multiplicacao()))   
        elif processo == 5:
            
            print("{}^{} = {}".format(num_1, num_2, potenciacao()))
        elif processo == 6:
            
            print("{}^^V {} = {}".format(num_2, num_1, raiz()))
        elif processo == 0:
            
            print("Tchau Tchauu!!!")
            sair()
        else:
            print("Insira um comando válido!!!")


    

if __name__ == "__main__":
    main()

    