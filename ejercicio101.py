// Proyecto de Informatica
// Ejercicio 101
Título del Ejercicio: Reemplazar Elementos
Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n,oldVal,newVal; cin>>n>>oldVal>>newVal;
    vector<int> v(n);
    for(int i=0;i<n;i++) cin>>v[i];

    replace(v.begin(),v.end(),oldVal,newVal);

    cout<<"Vector después de reemplazo: ";
    for(int x:v) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: [1 2 3 2], old=2, new=5 ? Salida: 1 5 3 5
100. Eliminar elementos menores que X usando std::remove_if