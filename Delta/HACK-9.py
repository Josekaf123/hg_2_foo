# //agregar tú alias al inicio  [100,200,300,400,500,600,700]

def fn_hack_9():
    lista = [100,200,300,400,500,600,700]
    lista[0] = "foo"
    print(lista) 
    return lista

fn_hack_9()