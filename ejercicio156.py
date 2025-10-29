// Proyecto de Informatica
// Ejercicio 156
Ejercicio 153: Buscar el elemento más cercano a un valor dado
Análisis del Problema
 En un vector ordenado, hallar el elemento cuyo valor sea más cercano a un número x.
Diseño de la Solución
 Usar lower_bound para encontrar el primer elemento ? x, y comparar con el anterior.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,x; cin >> n;
    vector<int> v(n);
    for (int i=0;i<n;++i) cin >> v[i];
    sort(v.begin(), v.end());
    cin >> x;

    auto it = lower_bound(v.begin(), v.end(), x);
    if(it == v.begin()) cout << *it;
    else if(it == v.end()) cout << v.back();
    else {
        int a = *(it-1), b = *it;
        cout << (abs(a-x) <= abs(b-x) ? a : b);
    }
}

Pruebas
Entrada:

 5
1 5 8 10 12
9
? 
? Salida: 8