// Proyecto de Informatica
// Ejercicio 172
Ejercicio 168: Mediana en flujo (dos heaps)
Análisis
 Mantener mediana mientras se insertan números uno a uno.
Diseño
 Max-heap left, min-heap right; rebalanceo.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    priority_queue<int> L;
    priority_queue<int, vector<int>, greater<int>> R;
    int x;
    while(cin>>x){
        if(L.empty() || x<=L.top()) L.push(x); else R.push(x);
        if(L.size()>R.size()+1){ R.push(L.top()); L.pop(); }
        else if(R.size()>L.size()){ L.push(R.top()); R.pop(); }
        double med = (L.size()==R.size()) ? (L.top()+R.top())/2.0 : L.top();
        cout<<med<<"\n";
    }
}

Prueba
? Entrada: 5 15 1 3 (sequence) ? Medianas: 5,10,5,4