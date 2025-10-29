// Proyecto de Informatica
// Ejercicio 31
Ejercicio 29: Merge k listas ordenadas (k-way merge)
Análisis
 Dadas k listas ordenadas, combinar en una sola lista ordenada.
Diseño
 Usar priority_queue con tuplas (value, list_id, index).
Código
#include <bits/stdc++.h>
using namespace std;
using T = tuple<int,int,int>;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k; if(!(cin>>k)) return 0;
    vector<vector<int>> lists(k);
    for(int i=0;i<k;++i){
        int m; cin>>m;
        lists[i].resize(m);
        for(int j=0;j<m;++j) cin>>lists[i][j];
    }
    priority_queue<T, vector<T>, greater<T>> pq;
    for(int i=0;i<k;++i) if(!lists[i].empty()) pq.emplace(lists[i][0], i, 0);
    while(!pq.empty()){
        auto [val, lid, idx] = pq.top(); pq.pop();
        cout<<val<<' ';
        if(idx+1 < (int)lists[lid].size()) pq.emplace(lists[lid][idx+1], lid, idx+1);
    }
    cout<<'\n';
    return 0;
}

Pruebas
? k=3; lists: [1 4],[2 3],[0 5] ? 0 1 2 3 4 5.