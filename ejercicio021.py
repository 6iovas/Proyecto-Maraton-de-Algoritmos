// Proyecto de Informatica
// Ejercicio 21
Ejercicio 20: k-ésimo elemento más grande (std::nth_element)
Análisis
 Usar nth_element para tiempo lineal promedio.
Diseño
 Aplicar nth_element con greater<int>().
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int k; cin>>k;
    if(k<1 || k>n) { cout<<"Error\n"; return 0; }
    nth_element(a.begin(), a.begin()+(k-1), a.end(), greater<int>());
    cout << a[k-1] << '\n';
    return 0;
}

Pruebas