// Proyecto de Informatica
// Ejercicio 28
Ejercicio 26: Radix Sort (enteros no negativos, base 10)
Análisis
 Orden por dígitos menos significativos (LSD) usando buckets.
Diseño
 Iterar por dígitos y aplicar counting sort por dígito.
Código
#include <bits/stdc++.h>
using namespace std;

void radix_sort(vector<int>& a) {
    int n=a.size();
    int mx = *max_element(a.begin(), a.end());
    for (int exp=1; mx/exp > 0; exp *= 10) {
        vector<int> output(n), cnt(10,0);
        for(int i=0;i<n;++i) cnt[(a[i]/exp)%10]++;
        for(int i=1;i<10;++i) cnt[i]+=cnt[i-1];
        for(int i=n-1;i>=0;--i){
            int d=(a[i]/exp)%10;
            output[--cnt[d]] = a[i];
        }
        a.swap(output);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    radix_sort(a);
    for(int x:a) cout<<x<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? a=[170 45 75 90 802 24 2 66] ? 2 24 45 66 75 90 170 802.