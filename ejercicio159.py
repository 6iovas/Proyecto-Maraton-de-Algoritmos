// Proyecto de Informatica
// Ejercicio 159
Ejercicio 156: Contar inversions (pares desordenados) con Merge Sort
Análisis del Problema
 Contar cuántos pares (i,j) existen con i < j y a[i] > a[j].
Diseño de la Solución
 Usar Merge Sort modificando el merge para contar las inversiones cruzadas.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

long long merge_count(vector<int>& a, int l, int r){
    if(l >= r) return 0;
    int m = (l+r)/2;
    long long inv = merge_count(a,l,m) + merge_count(a,m+1,r);
    vector<int> temp; int i=l,j=m+1;
    while(i<=m && j<=r){
        if(a[i]<=a[j]) temp.push_back(a[i++]);
        else { temp.push_back(a[j++]); inv += (m-i+1); }
    }
    while(i<=m) temp.push_back(a[i++]);
    while(j<=r) temp.push_back(a[j++]);
    copy(temp.begin(),temp.end(),a.begin()+l);
    return inv;
}

int main(){
    int n; cin >> n;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin >> a[i];
    cout << "Inversiones: " << merge_count(a,0,n-1) << "\n";
}

Pruebas
? Entrada: 5\n2 4 1 3 5

? Salida: Inversiones: 3