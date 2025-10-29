// Proyecto de Informatica
// Ejercicio 171
Ejercicio 167: Max en ventana deslizante (deque)
Análisis
 Para cada ventana de tamaño k, hallar el máximo.
Diseño
 Deque mantener índices con valores decrecientes.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<int>a(n); for(int i=0;i<n;++i)cin>>a[i];
    int k; cin>>k;
    deque<int> dq;
    for(int i=0;i<n;++i){
        if(!dq.empty() && dq.front()==i-k) dq.pop_front();
        while(!dq.empty() && a[dq.back()]<=a[i]) dq.pop_back();
        dq.push_back(i);
        if(i>=k-1) cout<<a[dq.front()]<<" ";
    }
    cout<<"\n";
}

Prueba
? Entrada: 8 1 3 -1 -3 5 3 6 7 3 (n=8 arr then k=3) ? Salida: 3 3 5 5 6 7