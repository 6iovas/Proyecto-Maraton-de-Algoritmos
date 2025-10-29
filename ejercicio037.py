// Proyecto de Informatica
// Ejercicio 37
Ejercicio 35: Ordenar por número de bits (popcount) y valor
Análisis
 Ordenar enteros por __builtin_popcount y por valor en caso de empate.
Diseño
 std::sort con comparator que usa __builtin_popcount.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    sort(a.begin(), a.end(), [](int x, int y){
        int bx = __builtin_popcount((unsigned)x);
        int by = __builtin_popcount((unsigned)y);
        if (bx != by) return bx < by;
        return x < y;
    });
    for(int x:a) cout<<x<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? a=[3 7 8 9] ? popcounts: 3(2),7(3),8(1),9(2) ? orden 8 3 9 7.