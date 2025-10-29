// Proyecto de Informatica
// Ejercicio 38
Ejercicio 36: Dutch National Flag (0s,1s,2s)
Análisis
 Reordenar array con solo 0,1,2 en orden ascendiente en O(n), O(1) espacio.
Diseño
 Tres punteros: low, mid, high.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int low=0, mid=0, high=n-1;
    while(mid<=high){
        if(a[mid]==0) swap(a[low++], a[mid++]);
        else if(a[mid]==1) ++mid;
        else swap(a[mid], a[high--]);
    }
    for(int x:a) cout<<x<<' ';
    cout<<'\n';
    return 0;
}

PrueAnálisis
 Ejemplo práctico donde stable_sort preserva orden relativo de claves iguales.
Diseño
 Personas con group y name; stable_sort por group.
Código
#include <bits/stdc++.h>
using namespace std;
struct P { int group; string name; };

int main(){
    vector<P> v = {{1,"A"},{2,"B"},{1,"C"},{2,"D"},{1,"E"}};
    stable_sort(v.begin(), v.end(), [](const P& a, const P& b){ return a.group < b.group; });
    for(auto &p: v) cout<<p.group<<':'<<p.name<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? Observa que entre group==1 original order A,C,E preserved.