// Proyecto de Informatica
// Ejercicio 168
Ejercicio 164: Rotar vector k posiciones (derecha)
Análisis
 Rotación en O(n), O(1) espacio usando reverses.
Diseño
 Reverse whole, reverse first k, reverse rest.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n); for(int i=0;i<n;++i) cin>>a[i];
    int k; cin>>k; k%=n;
    reverse(a.begin(), a.end());
    reverse(a.begin(), a.begin()+k);
    reverse(a.begin()+k, a.end());
    for(int x:a) cout<<x<<" ";
    cout<<"\n";
}

Prueba
? Entrada: 5 1 2 3 4 5 2 ? Salida: 4 5 1 2 3