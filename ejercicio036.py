// Proyecto de Informatica
// Ejercicio 36
Ejercicio 34: Reordenar array separando pares e impares (in-place)
Análisis
 Mover pares al inicio o fin sin ordenar.
Diseño
 Two-pointer swapping.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int l=0, r=n-1;
    while(l<r){
        while(l<r && a[l]%2==0) ++l;
        while(l<r && a[r]%2!=0) --r;
        if(l<r) swap(a[l++], a[r--]);
    }
    for(int x:a) cout<<x<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? a=[3 1 2 4 7 6] ? pares agrupados al inicio (ej. 6 4 2 1 7 3 o similar dependiendo swaps).