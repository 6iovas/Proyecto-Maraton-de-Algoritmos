// Proyecto de Informatica
// Ejercicio 265
Ejercicio 36  Minimum Mean Cycle (Karps algorithm)
Análisis
 Encontrar en un grafo dirigido (con pesos que pueden ser positivos o negativos) el ciclo con mínima media aritmética (peso total / longitud). Karp ofrece un algoritmo O(n·m) usando DP por longitudes de camino. Devuelve la media mínima o indica que no existe ciclo.
Diseño
? dp[k][v] = peso mínimo de cualquier camino de longitud k que termina en v (k = 0..n).

? Inicializar dp[0][v] = 0 para todo v.

? Para k = 1..n: relajar aristas: dp[k][to] = min(dp[k][to], dp[k-1][v] + w(v->to)).

? Para cada vértice v con dp[n][v] < INF calcular el máximo (sobre k=0..n-1) de (dp[n][v] - dp[k][v]) / (n - k). Ese máximo es el mínimo promedio para ciclos que llegan a v. La respuesta es el mínimo de esos máximos sobre v.

? Si no se detecta ciclo (ans inf), reportar no cycle.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const long double INF = 1e300;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; 
    if(!(cin>>n>>m)) return 0;
    vector<vector<pair<int,ll>>> g(n);
    for(int i=0;i<m;++i){
        int u,v; ll w; cin>>u>>v>>w;
        g[u].push_back({v,w});
    }
    // dp[k][v] for k=0..n
    const ll INFLL = (1LL<<60);
    vector<vector<long double>> dp(n+1, vector<long double>(n, INFLL));
    for(int v=0; v<n; ++v) dp[0][v] = 0.0L;
    for(int k=1;k<=n;++k){
        for(int v=0; v<n; ++v){
            if(dp[k-1][v] >= INFLL) continue;
            for(auto &e: g[v]){
                int to = e.first; ll w = e.second;
                dp[k][to] = min(dp[k][to], dp[k-1][v] + (long double)w);
            }
        }
    }
    long double ans = INF;
    for(int v=0; v<n; ++v){
        if(dp[n][v] >= INFLL) continue;
        long double best = -INF;
        for(int k=0;k<=n-1;++k){
            if(dp[k][v] >= INFLL) continue;
            long double val = (dp[n][v] - dp[k][v]) / (long double)(n - k);
            if(val > best) best = val;
        }
        if(best > -INF/2) ans = min(ans, best);
    }
    if(ans == INF) cout << "No cycle\n";
    else cout<<fixed<<setprecision(9)<<(double)ans<<"\n";
    return 0;
}

Pruebas
? Grafo con ciclo negativo medio mínimo:
 n=3 m=3 edges: 0->1 1, 1->2 -3, 2->0 1 ? cycle (0?1?2?0) weight -1 length 3 mean -0.333333 ? salida aprox -0.333333333.