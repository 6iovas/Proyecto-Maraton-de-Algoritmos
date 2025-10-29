// Proyecto de Informatica
// Ejercicio 181
Ejercicio 177: Comprimir coordenadas (coordinate compression)
Análisis
 Mapear valores dispersos a rango 0..m-1 manteniendo orden.
Diseño
 Copiar valores, sort unique, map original->index.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n), b;
    for(int i=0;i<n;++i){ cin>>a[i]; b.push_back(a[i]); }
    sort(b.begin(), b.end()); b.erase(unique(b.begin(), b.end()), b.end());
    for(int i=0;i<n;++i){
        int idx = lower_bound(b.begin(), b.end(), a[i]) - b.begin();
        cout<<idx<<" ";
    }
    cout<<"\n";
}

Prueba
? 5 100 500 1000 500 100 ? 0 1 2 1 0