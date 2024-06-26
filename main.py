"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
#ORDEN
DEFAULT_ASC_ORDER = True



def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))

def count_items(my_list):
    return len(my_list)


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    order_lst = DEFAULT_ASC_ORDER

    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        order_lst = sys.argv[3].lower() == "asc" #order list
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        print("El tercer argumento ordena la lista")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    readedWords = count_items(word_list)
    print(f"El archivo o la lista por defecto contiene {readedWords} palabras")

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)
    
    print(f"El archivo o la lista por defecto contiene {readedWords} palabras luego de eliminar palabras duplicadas")

    print(sort_list(word_list, order_lst))
