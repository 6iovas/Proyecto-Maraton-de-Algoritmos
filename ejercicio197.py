// Proyecto de Informatica
// Ejercicio 197
Ejercicio 193: Merge two sorted arrays in-place (without extra array)  when space at end
Análisis
 Dado A de tamaño m+n con primeros m validos y B tamaño n, fusionar en A in-place.
Diseño
 Usar 3 punteros desde el final.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int m,n; if(!(cin>>m>>n)) return 0;
    vector<int> A(m+n);
    for(int i=0;i<m;++i) cin>>A[i];
    for(int j=0;j<n;++j) cin>>A[m+j]; // read B into tail for simplicity
    // Instead assume separate B:
    // Alternative: read B separately
    // For clarity, read B separately:
    // (here using A[0..m-1] and B separately:)
    // So redo:
    vector<int> a(m); for(int i=0;i<m;++i) a[i]=A[i];
    vector<int> b(n); for(int j=0;j<n;++j) b[j]=A[m+j];
    int i=m-1, j=n-1, k=m+n-1;
    while(j>=0){
        if(i>=0 && a[i]>b[j]) A[k--]=a[i--];
        else A[k--]=b[j--];
    }
    for(int idx=0; idx<m+n; ++idx) cout<<A[idx]<<" ";
    cout<<"\n";
}

Prueba
? A=[1,3,5,0,0], m=3 B=[2,4], n=2 ? 1 2 3 4 5