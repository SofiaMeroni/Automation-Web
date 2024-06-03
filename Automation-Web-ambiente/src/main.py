from src.paginas.api import todaslasbromas
from src.utils.crearbase import cerrarconexionbase, bromaguardada, obtener_bromas

def main():
    num_bromas = 20
    bromas = todaslasbromas(num_bromas)

    # Guardar las bromas en la base de datos
    for broma in bromas:
        bromaguardada(broma)
    
    # Obtener las bromas de la base de datos
    bromas_bd = obtener_bromas()
    
    if bromas_bd:
        print("Bromas de Chuck Norris:")
        for i, broma in enumerate(bromas_bd, start=1):
            print(f"{i}. {broma[1]}")
    else:
        print("Error en obtener las bromas")

if __name__ == '__main__':
    main()
    cerrarconexionbase() 
    #cambio
