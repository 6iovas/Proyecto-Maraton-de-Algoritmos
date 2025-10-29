// Proyecto de Informatica
// Ejercicio 48
Ejercicio 46: Longest Increasing Subsequence (LIS) O(n log n)
Análisis
 Calcular longitud LIS.
Diseño
 tails con lower_bound.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int lis_len(const vector<int>& a){
    vector<int> tails;
    for(int x: a){
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if(it==tails.end()) tails.push_back(x);
        else *it = x;
    }
    return tails.size();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    cout<<lis_len(a)<<"\n";
    return 0;
}

Pruebas
? 10 9 2 5 3 7 101 18 ? 4.