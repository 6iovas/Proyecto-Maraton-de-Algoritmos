// Proyecto de Informatica
// Ejercicio 176
Ejercicio 172: std::nth_element  encontrar mediana en O(n)
Análisis
 Usar nth_element para hallar k-ésimo.
Diseño
 Call nth_element(v.begin(), v.begin()+k, v.end()).
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0; vector<int>a(n); for(int i=0;i<n;++i)cin>>a[i];
    int k = n/2; nth_element(a.begin(), a.begin()+k, a.end());
    cout<<a[k]<<"\n";
}

Prueba
? Entrada: 5 7 1 3 5 9 ? mediana 5 (depending on order may be 5)