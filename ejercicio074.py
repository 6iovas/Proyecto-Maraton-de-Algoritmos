// Proyecto de Informatica
// Ejercicio 74
Título del Ejercicio: Ordenar Personas por Edad
Análisis del Problema
? Descripción del Problema: Dado un array de personas con nombre y edad, ordenar de menor a mayor según la edad.

? Entradas y Salidas:

? Entrada: Número de personas, nombres y edades.

? Salida: Lista de personas ordenadas por edad.

Diseño de la Solución
? Algoritmo Propuesto:

1. Leer número de personas y sus datos.

2. Usar std::sort con función lambda para ordenar por edad.

3. Mostrar lista ordenada.

? Estructuras de Datos: struct y std::vector.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Persona {
    string nombre;
    int edad;
};

int main() {
    int n;
    cout << "Ingrese número de personas: ";
    cin >> n;
    vector<Persona> personas(n);
    for(int i=0;i<n;i++) {
        cout << "Nombre: ";
        cin >> personas[i].nombre;
        cout << "Edad: ";
        cin >> personas[i].edad;
    }

    sort(personas.begin(), personas.end(), [](Persona a, Persona b){ return a.edad < b.edad; });

    cout << "Personas ordenadas por edad:\n";
    for(auto p : personas) cout << p.nombre << " - " << p.edad << endl;

    return 0;
}

Pruebas:
? Caso 1: Entrada: Ana 25, Juan 20, Luis 30 ? Salida: Juan 20, Ana 25, Luis 30
73. Ordenar un Vector de Enteros con Lambda