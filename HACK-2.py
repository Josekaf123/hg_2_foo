#//eliminar el primer item  [100,200,300,400,500,600,700]  result >  [200,300,400,500,600,700] 

def fn_hack_2():
    lista = [100,200,300,400,500,600,700]
    lista.pop(0)
    print(lista)
    return lista

fn_hack_2()