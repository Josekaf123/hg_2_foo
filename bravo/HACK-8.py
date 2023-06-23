# //agregar tú alias al final [100,200,300,400,500,600,700]  result >  [100,200,300,400,500,600,700,foo]

def fn_hack_8():
    lista = [100,200,300,400,500,600,700]
    lista[-1] = "foo"
    print(lista) 
    return lista

fn_hack_8()
