// Proyecto de Informatica
// Ejercicio 165
Ejercicio 161: Kadane (subarray suma máxima)
Análisis
 Encontrar suma máxima contigua.
Diseño
 Kadane iterativo, también recuperar subarray si se desea.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<long long> a(n); for(int i=0;i<n;++i) cin>>a[i];
    long long best = a[0], cur = 0;
    for(long long v: a){ cur = max(v, cur+v); best = max(best, cur); }
    cout<<best<<"\n";
}

Prueba
? Entrada: 9 -2 1 -3 4 -1 2 1 -5 4 ? Salida: 6