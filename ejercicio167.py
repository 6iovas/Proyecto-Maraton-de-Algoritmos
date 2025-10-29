// Proyecto de Informatica
// Ejercicio 167
Ejercicio 163: Contar inversiones (Merge Sort)
Análisis
 Número de pares (i<j, a[i]>a[j]).
Diseño
 Merge count O(n log n).
Código
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll merge_count(vector<int>& a, int l, int r){
    if(l>=r) return 0;
    int m=(l+r)/2; ll cnt=merge_count(a,l,m)+merge_count(a,m+1,r);
    vector<int> tmp; int i=l,j=m+1;
    while(i<=m && j<=r){
        if(a[i]<=a[j]) tmp.push_back(a[i++]);
        else { tmp.push_back(a[j++]); cnt += (m - i + 1); }
    }
    while(i<=m) tmp.push_back(a[i++]);
    while(j<=r) tmp.push_back(a[j++]);
    copy(tmp.begin(), tmp.end(), a.begin()+l);
    return cnt;
}
int main(){ int n; if(!(cin>>n)) return 0; vector<int>a(n); for(int i=0;i<n;++i)cin>>a[i]; cout<<merge_count(a,0,n-1)<<"\n";}

Prueba
? Entrada: 5 2 4 1 3 5 ? Salida: 3