// Proyecto de Informatica
// Ejercicio 163
Ejercicio 159: Moda de una lista (frecuencia máxima)
Análisis
 Encontrar número con mayor frecuencia.
Diseño
 Contar con unordered_map<int,int> y elegir máximo.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    unordered_map<int,int> f;
    for(int i=0;i<n;++i){ int x; cin>>x; f[x]++; }
    int mode=0, mf=0;
    for(auto &p:f) if(p.second>mf){ mf=p.second; mode=p.first; }
    cout<<mode<<" "<<mf<<"\n";
}

Prueba
? Entrada: 7 1 2 2 3 3 3 4 ? Salida: 3 3