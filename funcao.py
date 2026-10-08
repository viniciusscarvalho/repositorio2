def cria_funcao_afim(a,b):
    def f(x):
        return a * x + b
    return f
f = cria_funcao_afim(2,-3)
print(f(2))
print(f(3))
print(f(4))