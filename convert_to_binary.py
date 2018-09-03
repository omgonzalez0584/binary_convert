

def convert_to_bin(num): #FUNCION CONVIERTE UN DECIMAL A BINARIO
    num_bin = []
    while num != 1:
        num_bin.append(num%2)
        num = num / 2
    num_bin.append(num)
    return(num_bin)

def print_binary(num_bin): #IMPRIME LOS NUMEROS BINARIOS
    temp = []
    num_bin.reverse()
    for i in num_bin:
        temp.append(str(i))
    a = " ".join(temp)
    print(a)

def convert_to_dec(binary): #CONVIERTE BINARIO A DECIMAL
    list_temp = []
    for i in binary:
        list_temp.append(int(i))
    list_temp.reverse()
    sum = 0
    j = 0
    for i in list_temp:
        sum = sum + (i * pow(2,j))
        j = j + 1
    return (sum)

def sumar_binarios(bin1,bin2): #SUMA 2 NUMEROS BINARIOS
    num1 = convert_to_dec(bin1)
    num2 = convert_to_dec(bin2)
    suma = num1 + num2
    lista_flag = convert_to_bin(suma)
    print_binary(lista_flag)

def main(): #FUNCION MAIN 
    while True:
        print("1.Convertir de  binario a decimal ")
        print("2.Convertir decimal a binario ")
        print("3.Sumar dos numeros binarios ")
        print("4.Para Salir ")
        opc =raw_input("Digite una opcion: ")

        if opc=='4':
            print("Adios...")
            break

        elif opc == '1':
            num = int(input("Digite el numero: "))
            num_bin = convert_to_bin(num)
            print_binary(num_bin)

        elif opc == '2':
             binary =raw_input("Digite el numero Binario: ")
             decimal = convert_to_dec(binary)
             print(decimal)

        else:
            bin1 = raw_input("Digite el primer binario: ")
            bin2 = raw_input("Digite el segundo binario: ")
            sumar_binarios(bin1,bin2)

if __name__ =='__main__':
  main()
