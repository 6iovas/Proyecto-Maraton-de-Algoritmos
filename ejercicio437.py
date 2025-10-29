// Proyecto de Informatica
// Ejercicio 437
Título del Ejercicio: Crear Cola (Queue) con Array
Análisis del Problema
? Descripción del Problema: Implementar una cola usando array con operaciones enqueue y dequeue.

? Entradas y Salidas:

? Entrada: Elementos a agregar o quitar.

? Salida: Estado de la cola.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir array y variables front y rear.

2. Implementar funciones enqueue y dequeue.

? Estructuras de Datos: Array y variables front y rear.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

class Cola{
    int arr[10], front, rear;
public:
    Cola(){front=0; rear=-1;}
    void enqueue(int x){
        if(rear<9) arr[++rear]=x;
        else cout << "Cola llena" << endl;
    }
    void dequeue(){
        if(front<=rear) front++;
        else cout << "Cola vacia" << endl;
    }
    void mostrar(){
        for(int i=front;i<=rear;i++) cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Cola c;
    c.enqueue(1); c.enqueue(2); c.enqueue(3);
    c.mostrar(); // 1 2 3
    c.dequeue();
    c.mostrar(); // 2 3
    return 0;
}

Pruebas
? Caso 1: enqueue 1,2,3 ? 1 2 3

? Caso 2: dequeue ? 2 3

? Caso 3: dequeue todas ? Cola vacía