// Proyecto de Informatica
// Ejercicio 367
Título del Ejercicio: Eliminar Elemento de Lista Enlazada
Análisis del Problema
? Descripción del Problema: Eliminar un nodo con un valor dado en una lista enlazada simple.

? Entradas y Salidas:

? Entrada: Lista enlazada y valor a eliminar.

? Salida: Lista actualizada.

Diseño de la Solución
? Algoritmo Propuesto:

1. Revisar si el nodo cabeza contiene el valor.

2. Recorrer lista y actualizar enlaces para eliminar nodo.

3. Mostrar lista resultante.

? Estructuras de Datos: Lista enlazada.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

struct Nodo { int dato; Nodo* siguiente; };

Nodo* eliminar(Nodo* cabeza, int valor) {
    if(!cabeza) return nullptr;
    if(cabeza->dato == valor) {
        Nodo* temp = cabeza->siguiente;
        delete cabeza;
        return temp;
    }
    Nodo* actual = cabeza;
    while(actual->siguiente && actual->siguiente->dato != valor) actual = actual->siguiente;
    if(actual->siguiente) {
        Nodo* temp = actual->siguiente;
        actual->siguiente = temp->siguiente;
        delete temp;
    }
    return cabeza;
}

void mostrar(Nodo* cabeza) {
    while(cabeza) {
        cout << cabeza->dato << " ";
        cabeza = cabeza->siguiente;
    }
    cout << endl;
}

int main() {
    Nodo* lista = new Nodo{1,new Nodo{2,new Nodo{3,nullptr}}};
    lista = eliminar(lista,2);
    mostrar(lista); // 1 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3], eliminar 2 ? [1,3]

? Caso 2: [1,2,3], eliminar 4 ? [1,2,3]

? Caso 3: [1], eliminar 1 ? []
ercicio 36 (continuación)
Código Fuente (C++)
       for(int j=0;j<2;j++) cout << C[i][j] << " ";
        cout << endl;
    }
    return 0;
}

Pruebas
? Caso 1:
 A = [[1,2,3],[4,5,6]], B = [[7,8],[9,10],[11,12]] ? C = [[58,64],[139,154]]

? Caso 2:
 A = [[1]], B = [[2]] ? C = [[2]]

? Caso 3:
 A = [[1,0],[0,1]], B = [[5,6],[7,8]] ? C = [[5,6],[7,8]]