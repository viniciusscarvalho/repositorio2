def funcao_segundo_grau(x,a,b,c):
        return a * x**2  + b * x + c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
x = float(input("Digite o valor de x: "))

if a==0:
    print("Erro a deve ser diferente de zero.")
else:
    y = funcao_segundo_grau(x,a,b,c)
    print(f"f({x}) = {y}")