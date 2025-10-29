// Proyecto de Informatica
// Ejercicio 162
Ejercicio 158: Búsqueda binaria en vector de pares (clave, valor)
Análisis
 Buscar una clave en vector de pair<int,string> ordenado por clave y devolver el valor.
Diseño
 lower_bound por make_pair(key, "").
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<pair<int,string>> v(n);
    for(int i=0;i<n;++i) cin>>v[i].first>>v[i].second;
    sort(v.begin(), v.end());
    int key; cin>>key;
    auto it = lower_bound(v.begin(), v.end(), make_pair(key, string("")));
    if(it!=v.end() && it->first==key) cout<<it->second<<"\n";
    else cout<<"NO\n";
}

Prueba
Entrada:

 3
10 perro
20 gato
30 pez
20
?  Salida: gato