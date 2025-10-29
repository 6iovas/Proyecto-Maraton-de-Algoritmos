// Proyecto de Informatica
// Ejercicio 29
Ejercicio 27: Bucket Sort (reales en [0,1))
Análisis
 Distribuir en buckets, sort local y concatenar.
Diseño
 vector<vector<double>> buckets, sort cada bucket.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<double> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int b = max(1, n);
    vector<vector<double>> buckets(b);
    for(double x:a){
        int idx = min(b-1, int(x * b));
        buckets[idx].push_back(x);
    }
    for(auto &bucket: buckets){
        sort(bucket.begin(), bucket.end());
        for(double v: bucket) cout<<v<<' ';
    }
    cout<<'\n';
    return 0;
}

Pruebas
? Entrada valores en (0,1): 0.78 0.17 0.39 0.26 0.72 0.94 0.21 0.12 0.23 0.68