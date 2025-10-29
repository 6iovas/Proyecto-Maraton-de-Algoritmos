// Proyecto de Informatica
// Ejercicio 315
Título del Ejercicio: Pila de Estructuras Empleado
Análisis del Problema
? Descripción del Problema: Crear pila que almacene estructuras Empleado con nombre y edad. Permitir push, pop y mostrar datos.

? Entradas y Salidas:

? Entrada: Datos del empleado.

? Salida: Mostrar pila de empleados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir struct Empleado.

2. Implementar pila con array y puntero tope.

3. Funciones para agregar, eliminar y mostrar.

? Estructuras de Datos: Array de estructuras.

? Funciones Principales: main(), push(), pop(), mostrar().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

struct Empleado {
    string nombre;
    int edad;
};

class PilaEmpleado {
    Empleado* arr;
    int tope, capacidad;
public:
    PilaEmpleado(int n) { arr = new Empleado[n]; capacidad=n; tope=-1; }
    void push(Empleado e) {
        if(tope>=capacidad-1) cout << "Pila llena\n";
        else arr[++tope] = e;
    }
    void pop() {
        if(tope<0) cout << "Pila vacia\n";
        else tope--;
    }
    void mostrar() {
        cout << "Pila de empleados:\n";
        for(int i=0;i<=tope;i++) cout << arr[i].nombre << ", " << arr[i].edad << endl;
    }
    ~PilaEmpleado() { delete[] arr; }
};

int main() {
    PilaEmpleado p(3);
    p.push({"Juan", 25});
    p.push({"Ana", 30});
    p.mostrar();
    p.pop();
    p.mostrar();
    return 0;
}

Pruebas
? Caso 1: Push Juan y Ana ? Mostrar ? Lista de empleados

? Caso 2: Pop ? Mostrar ? Solo Juan

? Caso 3: Push hasta capacidad ? Mensaje "Pila llena"