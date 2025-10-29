// Proyecto de Informatica
// Ejercicio 166
Ejercicio 162: Mediana de un vector
Análisis
 Calcular mediana (si n par -> promedio de dos centrales).
Diseño
 Ordenar y devolver.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<double> a(n); for(int i=0;i<n;++i) cin>>a[i];
    sort(a.begin(), a.end());
    if(n%2) cout<<a[n/2]<<"\n"; else cout<<((a[n/2-1]+a[n/2])/2.0)<<"\n";
}

Prueba
? Entrada: 4 10 20 30 40 ? Salida: 25