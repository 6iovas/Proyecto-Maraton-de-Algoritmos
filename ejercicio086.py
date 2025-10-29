// Proyecto de Informatica
// Ejercicio 86
Título del Ejercicio: Números Únicos con std::set
Análisis del Problema
? Descripción del Problema: Insertar números en un std::set para mantenerlos únicos y ordenados automáticamente.

? Entradas y Salidas:

? Entrada: Número de elementos y los números.

? Salida: Números únicos ordenados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Leer tamaño n y los números.

2. Insertar en std::set.

3. Mostrar contenido del set.

? Estructuras de Datos: std::set.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <set>
using namespace std;

int main(){
    int n; cout<<"Ingrese número de elementos: "; cin>>n;
    set<int> s;
    cout<<"Ingrese elementos:\n";
    for(int i=0;i<n;i++){
        int x; cin>>x;
        s.insert(x);
    }

    cout<<"Números únicos y ordenados: ";
    for(int x:s) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [5 3 5 2] ? Salida: 2 3 5

85. Insertar y eliminar elementos de std::set