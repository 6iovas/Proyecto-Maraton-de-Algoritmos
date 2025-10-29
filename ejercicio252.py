// Proyecto de Informatica
// Ejercicio 252
Ejercicio 32  Minimum Cut via StoerWagner (global min cut, undirected)
Análisis
 Encontrar corte mínimo global (sin especificar s/t) en grafo no dirigido con pesos (StoerWagner) en O(n³) worst but practical for n ? 500.
Diseño
 Implementar fase de "maximum adjacency search" repetida y contraction de un vértice por fase; track min cut weight.
Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL<<60);

ll stoerWagner(vector<vector<ll>> a){
    int n = a.size();
    vector<int> v(n);
    iota(v.begin(), v.end(), 0);
    ll best = INF;
    for(int phase = n; phase > 1; --phase){
        vector<ll> w(phase,0);
        vector<char> added(phase, false);
        int prev = -1;
        for(int i=0;i<phase;++i){
            int sel = -1;
            for(int j=0;j<phase;++j) if(!added[j] && (sel==-1 || w[j] > w[sel])) sel = j;
            if(added[sel]) break;
            added[sel] = 1;
            if(i == phase-1){
                // sel is t, prev is s
                best = min(best, w[sel]);
                // merge sel into prev
                for(int j=0;j<phase;++j) a[prev][j] += a[sel][j], a[j][prev] = a[prev][j];
                v.erase(v.begin()+sel);
                for(int j=sel;j<phase-1;++j){
                    for(int k=0;k<phase-1;++k) a[j][k] = a[j+1][k+ (k>=sel?1:0)];
                }
            } else {
                prev = sel;
                for(int j=0;j<phase;++j) if(!added[j]) w[j] += a[sel][j];
            }
        }
    }
    return best;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<vector<ll>> a(n, vector<ll>(n,0));
    int m; cin>>m;
    for(int i=0;i<m;++i){ int u,v; ll w; cin>>u>>v>>w; a[u][v]+=w; a[v][u]+=w; }
    cout << "Global min cut: " << stoerWagner(a) << "\n";
    return 0;
}

Prueba
? Small undirected graph compare manual min-cut.