// Proyecto de Informatica
// Ejercicio 99
Título del Ejercicio: Elementos Comunes
Código Fuente (C++):
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main(){
    int n,m; cin>>n>>m;
    vector<int> v1(n),v2(m);
    for(int i=0;i<n;i++) cin>>v1[i];
    for(int i=0;i<m;i++) cin>>v2[i];

    set<int> s1(v1.begin(),v1.end()), s2(v2.begin(),v2.end()), inter;
    for(int x:s1) if(s2.count(x)) inter.insert(x);

    cout<<"Elementos comunes: ";
    for(int x:inter) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: v1=[1 2 3], v2=[2 3 4] ? Salida: 2 3
98. Contar elementos mayores a X usando std::count_if