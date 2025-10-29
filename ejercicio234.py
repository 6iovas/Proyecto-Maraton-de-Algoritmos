// Proyecto de Informatica
// Ejercicio 234
Ejercicio 27  Maximum Independent Set on a Tree (Tree DP + reconstruct chosen nodes)
Análisis del problema
 Dado un árbol con n nodos y valores en cada nodo (weight optional), encontrar el conjunto independiente (ningún par adyacente) de máxima suma de pesos (o máximo tamaño si pesos = 1). Retornar el valor máximo y los nodos escogidos. Complejidad O(n).
Diseño de la solución
? DP en árbol: dp[v][0] = máximo si v no es tomado; dp[v][1] = máximo si v sí es tomado.

? Transiciones:

? dp[v][1] = val[v] + sum(dp[ch][0])

? dp[v][0] = sum(max(dp[ch][0], dp[ch][1]))

? Reconstrucción: DFS que decide si tomar v según valores dp y las decisiones tomadas por el padre.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n;
vector<vector<int>> g;
vector<ll> val;
vector<array<ll,2>> dp;
vector<int> parent;

void dfs1(int v,int p){
    parent[v]=p;
    dp[v][1] = val[v];
    dp[v][0] = 0;
    for(int to: g[v]) if(to!=p){
        dfs1(to,v);
        dp[v][1] += dp[to][0];
        dp[v][0] += max(dp[to][0], dp[to][1]);
    }
}

void recon(int v,int take, vector<int>& chosen){
    if(take){
        chosen.push_back(v);
        for(int to: g[v]) if(to!=parent[v]){
            recon(to, 0, chosen);
        }
    } else {
        for(int to: g[v]) if(to!=parent[v]){
            if(dp[to][1] > dp[to][0]) recon(to, 1, chosen);
            else recon(to, 0, chosen);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(!(cin>>n)) return 0;
    g.assign(n, {});
    for(int i=0;i<n-1;++i){ int u,v; cin>>u>>v; g[u].push_back(v); g[v].push_back(u); }
    val.assign(n,0);
    for(int i=0;i<n;++i) cin>>val[i];
    dp.assign(n, {0,0});
    parent.assign(n, -1);
    dfs1(0,-1);
    ll best = max(dp[0][0], dp[0][1]);
    cout<<"Best sum: "<<best<<"\n";
    vector<int> chosen;
    if(dp[0][1] > dp[0][0]) recon(0,1,chosen);
    else recon(0,0,chosen);
    sort(chosen.begin(), chosen.end());
    cout<<"Chosen nodes (0-based):";
    for(int x: chosen) cout<<" "<<x;
    cout<<"\n";
    return 0;
}

Pruebas
? Árbol línea 0-1-2-3, valores 1 1 1 1 ? maximum independent set size = 2, e.g., nodes 0,2 or 1,3. Code returns one valid set and sum 2.