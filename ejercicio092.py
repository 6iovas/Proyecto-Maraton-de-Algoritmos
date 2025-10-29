// Proyecto de Informatica
// Ejercicio 92
Título del Ejercicio: Top k Números
Código Fuente (C++):
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(){
    int n,k; cin>>n>>k;
    priority_queue<int,vector<int>,greater<int>> pq;
    for(int i=0;i<n;i++){
        int x; cin>>x;
        pq.push(x);
        if(pq.size()>k) pq.pop();
    }

    vector<int> res;
    while(!pq.empty()){ res.push_back(pq.top()); pq.pop();}
    for(int x:res) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [3 1 5 2], k=2 ? Salida: 3 5

91. Ordenar vector de pares por segundo valor