// Proyecto de Informatica
// Ejercicio 34
Ejercicio 32: Intersección de dos arrays ordenados
Análisis
 Producir elementos comunes (sin duplicar resultados si se pide único o con duplicados según criterio  aquí incluimos repetidos según ocurrencia).
Diseño
 Two-pointer.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<int> a(n), b(m);
    for(int i=0;i<n;++i) cin>>a[i];
    for(int j=0;j<m;++j) cin>>b[j];
    int i=0,j=0;
    while(i<n && j<m){
        if(a[i]==b[j]) { cout<<a[i]<<' '; ++i; ++j;}
        else if(a[i]<b[j]) ++i;
        else ++j;
    }
    cout<<'\n';
    return 0;
}

Pruebas
? a=[1 2 2 3], b=[2 2 4] ? 2 2.