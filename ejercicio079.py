// Proyecto de Informatica
// Ejercicio 79
Título del Ejercicio: Contar Caminos en un DAG
Análisis del Problema
? Descripción del Problema: Dado un grafo acíclico dirigido (DAG), contar cuántos caminos distintos existen desde un nodo origen a un nodo destino.

? Entradas y Salidas:

? Entrada: Número de nodos n, número de aristas m, lista de aristas, nodo origen y destino.

? Salida: Número total de caminos distintos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear lista de adyacencia para el DAG.

2. Inicializar vector dp con -1 para memoización.

3. Usar función recursiva con memoización: dp[u] = sum(dp[v]) para cada vecino v.

4. Mostrar dp[origen].

? Estructuras de Datos: vector<vector<int>>, vector<int> para DP.

? Funciones Principales: main y función countPaths.

Código Fuente (C++):
#include <iostream>
#include <vector>
using namespace std;

int n,destino;
vector<vector<int>> adj;
vector<int> dp;

int countPaths(int u){
    if(u==destino) return 1;
    if(dp[u]!=-1) return dp[u];
    int total=0;
    for(int v: adj[u]) total += countPaths(v);
    return dp[u]=total;
}

int main(){
    int m,origen;
    cout<<"Ingrese número de nodos y aristas: ";
    cin>>n>>m;
    adj.assign(n,vector<int>());
    dp.assign(n,-1);
    cout<<"Ingrese aristas (u v):\n";
    for(int i=0;i<m;i++){
        int u,v; cin>>u>>v;
        adj[u].push_back(v);
    }
    cout<<"Ingrese nodo origen y destino: ";
    cin>>origen>>destino;

    int total=countPaths(origen);
    cout<<"Número de caminos distintos: "<<total<<endl;
    return 0;
}

Pruebas:
? Caso 1: DAG 0->1,0->2,1->3,2->3, origen=0, destino=3 ? Salida: 2
78. Subset Sum (Suma de Subconjuntos)