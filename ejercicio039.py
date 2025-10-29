// Proyecto de Informatica
// Ejercicio 39
Ejercicio 38: Búsqueda ternaria en función unimodal (max)
Análisis
 Encontrar máximo de función unimodal discreta en un arreglo (no necesariamente continuo).
Diseño
 Aplicar búsqueda ternaria en índices (discreto).
Código
#include <bits/stdc++.h>
using namespace std;

int ternary_search_max(const vector<long long>& a){
    int l=0, r=(int)a.size()-1;
    while(r - l > 2){
        int m1 = l + (r - l) / 3;
        int m2 = r - (r - l) / 3;
        if(a[m1] < a[m2]) l = m1;
        else r = m2;
    }
    long long best = LLONG_MIN;
    int idx = l;
    for(int i=l;i<=r;++i) if(a[i]>best){ best=a[i]; idx=i;}
    return idx;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    cout<<ternary_search_max(a)<<"\n";
    return 0;
}

Pruebas
? a unimodal example: 1 3 8 12 7 4 ? index 3 (value 12).