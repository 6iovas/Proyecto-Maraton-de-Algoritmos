// Proyecto de Informatica
// Ejercicio 182
Ejercicio 178: Two pointers  contar pares con suma ? X en array ordenado
Análisis
 Contar pares (i<j) con a[i]+a[j] ? X.
Diseño
 Two pointers l=0, r=n-1; if sum?X add r-l and ++l else --r.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n); for(int i=0;i<n;++i) cin>>a[i];
    sort(a.begin(), a.end());
    long long X; cin>>X; long long cnt=0;
    int l=0, r=n-1;
    while(l<r){
        if(a[l]+a[r]<=X){ cnt += (r-l); ++l; }
        else --r;
    }
    cout<<cnt<<"\n";
}

Prueba
? n=4 a=[1,2,3,4], X=5 ? pares: (1,2),(1,3),(1,4),(2,3)?? check ? output 4