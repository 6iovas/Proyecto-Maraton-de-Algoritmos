// Proyecto de Informatica
// Ejercicio 133
Ejercicio 131: Dijkstra con priority_queue (camino más corto en grafo ponderado positivo)
Análisis del Problema
 Encontrar el camino más corto desde un nodo origen a todos los demás en un grafo con pesos positivos.
Diseño de la Solución
 Usar una cola de prioridad (min-heap) para seleccionar el vértice con menor distancia provisional.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct Edge { int to, w; };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<vector<Edge>> g(n);
    for (int i = 0; i < m; ++i) {
        int u, v, w; cin >> u >> v >> w;
        g[u].push_back({v, w});
        g[v].push_back({u, w}); // no dirigido
    }
    int s; cin >> s;
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[s] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [d,u] = pq.top(); pq.pop();
        if (d != dist[u]) continue;
        for (auto &e : g[u]) {
            if (dist[e.to] > d + e.w) {
                dist[e.to] = d + e.w;
                pq.push({dist[e.to], e.to});
            }
        }
    }
    for (int i = 0; i < n; ++i)
        cout << "Distancia a " << i << ": " << dist[i] << "\n";
}

Pruebas
Entrada:

 5 6
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 1
0
? 
Salida esperada:

 Distancia a 0: 0
Distancia a 1: 2
Distancia a 2: 3
Distancia a 3: 7
Distancia a 4: 6