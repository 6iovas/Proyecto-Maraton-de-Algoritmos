// Proyecto de Informatica
// Ejercicio 26
Ejercicio 24: Simulación de Merge Externo (esqueleto)
Análisis
 Esquema para ordenar data mayor que RAM: dividir en chunks, sort cada chunk, luego merge k-way.
Diseño
 Mostrar plantilla que simula usando archivos (a modo de ejemplo).
Código (plantilla simplificada)
/* Plantilla conceptual: aquí se simula con vectores en memoria.
   En la práctica: leer bloques desde disco, sort, escribir chunk files, luego k-way merge. */

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Simulamos: dividir vector en chunks, ordenar cada chunk, luego usar priority_queue para merge.
    vector<int> data;
    int x;
    while (cin>>x) data.push_back(x);
    int chunk = 1000; // ejemplo
    vector<vector<int>> chunks;
    for (size_t i=0;i<data.size();i+=chunk){
        vector<int> c(data.begin()+i, data.begin()+min(data.size(), i+chunk));
        sort(c.begin(), c.end());
        chunks.push_back(move(c));
    }
    // k-way merge:
    using T = tuple<int,int,int>; // value, chunk_id, index_in_chunk
    priority_queue<T, vector<T>, greater<T>> pq;
    for(int i=0;i<(int)chunks.size();++i)
        if(!chunks[i].empty()) pq.emplace(chunks[i][0], i, 0);
    while(!pq.empty()){
        auto [val, cid, idx] = pq.top(); pq.pop();
        cout<<val<<' ';
        if(idx+1 < (int)chunks[cid].size()) pq.emplace(chunks[cid][idx+1], cid, idx+1);
    }
    cout<<'\n';
    return 0;
}

Pruebas
? Usar entrada pequeña para verificar orden completo tras merge.