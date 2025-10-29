// Proyecto de Informatica
// Ejercicio 435
Título del Ejercicio: Crear Pila (Stack) con Array
Análisis del Problema
? Descripción del Problema: Implementar una pila usando array con operaciones push, pop y mostrar.

? Entradas y Salidas:

? Entrada: Elementos a agregar o quitar.

? Salida: Estado de la pila.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir array y variable top.

2. Implementar funciones push y pop.

? Estructuras de Datos: Array y variable top.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

class Pila{
    int arr[10], top;
public:
    Pila(){top=-1;}
    void push(int x){
        if(top<9) arr[++top]=x;
        else cout << "Pila llena" << endl;
    }
    void pop(){
        if(top>=0) top--;
        else cout << "Pila vacia" << endl;
    }
    void mostrar(){
        for(int i=top;i>=0;i--) cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Pila p;
    p.push(1); p.push(2); p.push(3);
    p.mostrar(); // 3 2 1
    p.pop();
    p.mostrar(); // 2 1
    return 0;
}

Pruebas
? Caso 1: push 1,2,3 ? 3 2 1

? Caso 2: pop ? 2 1

? Caso 3: pop todas ? pila vacía