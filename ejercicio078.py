// Proyecto de Informatica
// Ejercicio 78
Título del Ejercicio: Ordenar Cadenas Alfabéticamente
Análisis del Problema
? Descripción del Problema: Ordenar un array de cadenas alfabéticamente.

? Entradas y Salidas:

? Entrada: Array de strings.

? Salida: Array ordenado alfabéticamente.

Diseño de la Solución
? Algoritmo Propuesto:

1. Leer número de cadenas y cadenas.

2. Usar std::sort.

3. Mostrar resultado.

? Estructuras de Datos: std::vector<string>.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cout<<"Ingrese número de cadenas: ";
    cin>>n;
    vector<string> v(n);
    cout<<"Ingrese cadenas:\n";
    for(int i=0;i<n;i++) cin>>v[i];

    sort(v.begin(),v.end());

    cout<<"Cadenas ordenadas:\n";
    for(auto s:v) cout<<s<<endl;

    return 0;
}

Pruebas:
? Caso 1: {"banana","manzana","pera"} ? Salida: banana manzana pera
77. Contar Caminos Distintos de Origen a Destino en un DAG usando DP