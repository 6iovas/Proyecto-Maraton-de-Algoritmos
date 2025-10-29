// Proyecto de Informatica
// Ejercicio 190
Ejercicio 186: Heurística TSP (nearest neighbor)  aproximación rápida
Análisis
 Greedy nearest neighbor for TSP approximation.
Diseño
 Start at node 0, repeatedly go to nearest unvisited.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<vector<int>> w(n, vector<int>(n)); for(int i=0;i<n;++i) for(int j=0;j<n;++j) cin>>w[i][j];
    vector<char> vis(n,false); int cur=0; vis[0]=1; vector<int> tour={0};
    for(int step=1; step<n; ++step){
        int best=-1, bestd=INT_MAX;
        for(int v=0; v<n; ++v) if(!vis[v] && w[cur][v]<bestd){ best=v; bestd=w[cur][v]; }
        vis[best]=1; tour.push_back(best); cur=best;
    }
    // return to start
    tour.push_back(0);
    for(int x:tour) cout<<x<<" ";
    cout<<"\n";
}