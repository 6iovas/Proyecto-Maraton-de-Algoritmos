// Proyecto de Informatica
// Ejercicio 84
Título del Ejercicio: Camino Más Corto con Dijkstra
Análisis del Problema
? Descripción del Problema: Encontrar la distancia mínima desde un nodo origen a todos los demás en grafo ponderado.

? Entradas y Salidas:

? Entrada: Número de nodos, aristas, lista de aristas con peso, nodo origen.

? Salida: Distancia mínima desde origen a cada nodo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar distancias con infinito.

2. Usar priority_queue para nodos pendientes.

3. Relajar aristas y actualizar distancias.

4. Mostrar distancias.

? Estructuras de Datos: vector<vector<pair<int,int>>>, priority_queue.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
    int n,m;
    cout<<"Ingrese número de nodos y aristas: ";
    cin>>n>>m;
    vector<vector<pair<int,int>>> adj(n);
    cout<<"Ingrese aristas (u v peso):\n";
    for(int i=0;i<m;i++){
        int u,v,w; cin>>u>>v>>w;
        adj[u].push_back({v,w});
    }
    int origen; cout<<"Ingrese nodo origen: "; cin>>origen;

    vector<int> dist(n,1e9); dist[origen]=0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0,origen});

    while(!pq.empty()){
        auto [d,u]=pq.top(); pq.pop();
        if(d>dist[u]) continue;
        for(auto [v,w]: adj[u]){
            if(dist[u]+w<dist[v]){
                dist[v]=dist[u]+w;
                pq.push({dist[v],v});
            }
        }
    }

    cout<<"Distancias mínimas desde nodo "<<origen<<":\n";
    for(int i=0;i<n;i++) cout<<i<<": "<<dist[i]<<endl;

    return 0;
}

Pruebas:
? Caso 1: Grafo 0->1(4),0->2(1),2->1(2) ? Salida: 0:0,1:3,2:1

83. Coin Change (Número de Formas de Hacer Cambio)