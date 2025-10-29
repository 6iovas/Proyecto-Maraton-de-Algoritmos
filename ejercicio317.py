// Proyecto de Informatica
// Ejercicio 317
Título del Ejercicio: Cola de Prioridad Simple con Array
Análisis del Problema
? Descripción del Problema: Implementar cola de prioridad donde el menor valor tiene más prioridad.

? Entradas y Salidas:

? Entrada: Números a agregar.

? Salida: Mostrar cola ordenada por prioridad.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar array dinámico.

2. Insertar elementos en posición que mantenga orden creciente.

3. Eliminar elementos desde el frente.

4. Mostrar estado de la cola.

? Estructuras de Datos: Array dinámico.

? Funciones Principales: main(), insertar(), eliminar(), mostrar().

Código Fuente (C++)
#include <iostream>
using namespace std;

class ColaPrioridad {
    int* arr;
    int n;
public:
    ColaPrioridad(int size) { arr = new int[size]; n=0; }
    void insertar(int x) {
        int i=n-1;
        while(i>=0 && arr[i]>x) { arr[i+1]=arr[i]; i--; }
        arr[i+1]=x;
        n++;
    }
    void eliminar() { if(n>0) n--; }
    void mostrar() { for(int i=0;i<n;i++) cout << arr[i] << " "; cout << endl; }
    ~ColaPrioridad() { delete[] arr; }
};

int main() {
    ColaPrioridad c(5);
    c.insertar(30); c.insertar(10); c.insertar(20);
    c.mostrar(); // 10 20 30
    c.eliminar();
    c.mostrar(); // 10 20
    return 0;
}

Pruebas
? Caso 1: Insertar 30,10,20 ? 10 20 30

? Caso 2: Eliminar ? 10 20

? Caso 3: Insertar 5 ? 5 10 20