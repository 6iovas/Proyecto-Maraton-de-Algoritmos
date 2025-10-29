// Proyecto de Informatica
// Ejercicio 266
Ejercicio 37  Counting Hamiltonian Paths in a Directed Acyclic Graph (DP over subsets)
Análisis
 Contar cuántos caminos Hamiltonianos (que visitan cada vértice exactamente una vez) existen en un grafo dirigido con n ? 20 usando DP sobre subconjuntos. En grafos generales el problema es #P-hard; para n?20 se usa bitmask DP O(n²·2^n). Si el grafo es DAG o general, algoritmo funciona igualmente (pero toma tiempo exponencial).
Diseño
? dp[mask][v] = número de caminos que usan exactamente los vértices en mask y terminan en v.

? Base: dp[1<<v][v] = 1.

? Transición: para cada u tal que u está en mask y existe arista u->v, dp[mask][v] += dp[mask ^ (1<<v)][u].

? Sumar dp[(1<<n)-1][v] para todos v para obtener el número de Hamiltonian paths (todas las posibles terminaciones).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<int> adj(n,0);
    for(int i=0;i<m;++i){
        int u,v; cin>>u>>v;
        adj[u] |= (1<<v);
    }
    int N = 1<<n;
    vector<vector<unsigned long long>> dp(N, vector<unsigned long long>(n, 0));
    for(int v=0; v<n; ++v) dp[1<<v][v] = 1;
    for(int mask=1; mask<N; ++mask){
        for(int v=0; v<n; ++v){
            if(!(mask & (1<<v))) continue;
            unsigned long long cur = dp[mask][v];
            if(cur==0) continue;
            int ways_to = adj[v] & (~mask); // neighbors not yet in mask
            // we will extend by adding a new vertex 'u' (but common DP moves other way)
        }
        // classical fill: compute dp[mask][v] from smaller masks
        // we'll do the standard inner loops
    }
    // correct standard transitions (recompute DP properly)
    fill(dp.begin(), dp.end(), vector<unsigned long long>(n,0));
    for(int v=0; v<n; ++v) dp[1<<v][v]=1;
    for(int mask=1; mask<N; ++mask){
        for(int last=0; last<n; ++last){
            if(!(mask & (1<<last))) continue;
            unsigned long long ways = dp[mask][last];
            if(ways==0) continue;
            int to_mask = adj[last] & (~mask);
            for(int nxt = to_mask; nxt; nxt &= (nxt-1)){
                int u = __builtin_ctz(nxt);
                dp[mask | (1<<u)][u] += ways;
            }
        }
    }
    unsigned long long total = 0;
    for(int v=0; v<n; ++v) total += dp[N-1][v];
    cout<<total<<"\n";
    return 0;
}

Pruebas
? n=3 edges: 0->1,1->2 ? hay exactamente 1 Hamiltonian path (0?1?2).

? n=3 complete DAG (all i<j edges) ? 6 Hamiltonian paths (3!).