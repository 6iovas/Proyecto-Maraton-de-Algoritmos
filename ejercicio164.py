// Proyecto de Informatica
// Ejercicio 164
Ejercicio 160: Elemento más cercano a x (array ordenado)
Análisis
 Dado ordenado, hallar elemento con mínima diferencia absoluta.
Diseño
 lower_bound y comparar con anterior.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n); for(int i=0;i<n;++i) cin>>a[i];
    sort(a.begin(), a.end());
    int x; cin>>x;
    auto it=lower_bound(a.begin(), a.end(), x);
    if(it==a.begin()) cout<<*it<<"\n";
    else if(it==a.end()) cout<<a.back()<<"\n";
    else {
        int a1=*(it-1), a2=*it;
        cout<< (abs(a1-x)<=abs(a2-x) ? a1 : a2) <<"\n";
    }
}

Prueba
Entrada:

 5
1 5 8 10 12
9
?  Salida: 8