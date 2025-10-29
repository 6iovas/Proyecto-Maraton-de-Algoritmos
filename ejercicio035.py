// Proyecto de Informatica
// Ejercicio 35
Ejercicio 33: Eliminar duplicados en array ordenado (in-place)
Análisis
 Compactar array ordenado para eliminar duplicados y devolver nueva longitud.
Diseño
 Dos punteros write y read.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    if(n==0){ cout<<0<<"\n"; return 0;}
    int write = 1;
    for(int i=1;i<n;++i){
        if(a[i]!=a[i-1]) a[write++] = a[i];
    }
    for(int i=0;i<write;++i) cout<<a[i]<<' ';
    cout<<"\nLength: "<<write<<"\n";
    return 0;
}

Pruebas
? a=[1 1 2 2 3] ? 1 2 3, Length 3.