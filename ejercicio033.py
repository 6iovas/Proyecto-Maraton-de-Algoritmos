// Proyecto de Informatica
// Ejercicio 33
Ejercicio 31: Dos números cuya suma sea X (array ordenado, two pointers)
Análisis
 Encontrar indices de dos elementos con suma X en array ordenado.
Diseño
 Dos punteros l=0, r=n-1.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int X; cin>>X;
    int l=0, r=n-1;
    while(l<r){
        int s=a[l]+a[r];
        if(s==X){ cout<<l<<' '<<r<<"\n"; return 0;}
        else if(s<X) ++l;
        else --r;
    }
    cout<<"No\n";
    return 0;
}

Pruebas
? a=[1 2 3 4 6], X=6 ? 1 3 (2+4)

? X=11 ? No