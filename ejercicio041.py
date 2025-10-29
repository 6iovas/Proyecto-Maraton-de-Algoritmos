// Proyecto de Informatica
// Ejercicio 41
Ejercicio 40: Búsqueda binaria en array rotado
Análisis
 Buscar un target en array rotado en O(log n).
Diseño
 Determinar mitad ordenada y dirigir búsqueda.
Código
#include <bits/stdc++.h>
using namespace std;

int search_rotated(const vector<int>& a, int target){
    int l=0, r=(int)a.size()-1;
    while(l<=r){
        int m = l + (r-l)/2;
        if(a[m]==target) return m;
        if(a[l] <= a[m]){ // left sorted
            if(a[l] <= target && target < a[m]) r = m-1;
            else l = m+1;
        } else { // right sorted
            if(a[m] < target && target <= a[r]) l = m+1;
            else r = m-1;
        }
    }
    return -1;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int t; cin>>t;
    cout<<search_rotated(a,t)<<"\n";
    return 0;
}

Pruebas
? a=[4 5 6 7 0 1 2], t=0 ? 4

? t=3 ? -1

? a=[1], t=1 ? 0