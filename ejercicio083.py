// Proyecto de Informatica
// Ejercicio 83
Título del Ejercicio: Distancias Mínimas con Floyd-Warshall
Análisis del Problema
? Descripción del Problema: Dado un grafo ponderado, encontrar todas las distancias mínimas entre cada par de nodos.

? Entradas y Salidas:

? Entrada: Número de nodos n, matriz de adyacencia con pesos.

? Salida: Matriz de distancias mínimas.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar matriz dist con pesos.

2. Aplicar Floyd-Warshall: dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j]).

3. Mostrar matriz final.

? Estructuras de Datos: Array 2D dist.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n;
    cout<<"Ingrese número de nodos: ";
    cin>>n;
    vector<vector<int>> dist(n,vector<int>(n));
    cout<<"Ingrese matriz de adyacencia (-1 si no hay arista):\n";
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            cin>>dist[i][j];
            if(dist[i][j]==-1) dist[i][j]=1e9;
        }

    for(int k=0;k<n;k++)
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);

    cout<<"Matriz de distancias mínimas:\n";
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(dist[i][j]>=1e9) cout<<"INF ";
            else cout<<dist[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}

Pruebas:
? Caso 1: Grafo 3x3 con pesos [0 1 4],[1 0 2],[4 2 0] ? Matriz final: [0 1 3],[1 0 2],[3 2 0]
82. Dijkstra para Camino Más Corto desde Nodo Origen