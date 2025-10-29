// Proyecto de Informatica
// Ejercicio 40
Ejercicio 39: Encontrar punto de rotación en array rotado (mínimo elemento)
Análisis
 Dado un array originalmente ordenado y rotado, encontrar índice del elemento mínimo (punto de rotación).
Diseño
 Búsqueda binaria modificada.
Código
#include <bits/stdc++.h>
using namespace std;

int find_rotation_point(const vector<int>& a){
    int l=0, r=(int)a.size()-1;
    while(l<r){
        int m = l + (r-l)/2;
        if(a[m] > a[r]) l = m+1;
        else r = m;
    }
    return l;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    cout<<find_rotation_point(a)<<"\n";
    return 0;
}

Pruebas
? a=[4 5 6 7 0 1 2] ? index 4 (value 0).

? a=[1 2 3] ? 0.