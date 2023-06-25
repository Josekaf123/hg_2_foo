#//eliminar los items 300 y 500  [100,200,300,400,500,600,700]


def fn_hack_4():
    lista = [100,200,300,400,500,600,700]
    lista.remove(300) 
    lista.remove(500) 
    print(lista)
    return lista

fn_hack_4()