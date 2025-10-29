// Proyecto de Informatica
// Ejercicio 100
Título del Ejercicio: Contar con Condición
Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n,X; cin>>n>>X;
    vector<int> v(n);
    for(int i=0;i<n;i++) cin>>v[i];

    int cnt = count_if(v.begin(),v.end(),[X](int a){ return a>X; });
    cout<<"Cantidad de elementos mayores que "<<X<<": "<<cnt<<endl;
    return 0;
}

Pruebas:
? Caso 1: [1 3 5 7], X=4 ? Salida: 2
99. Reemplazar valores en vector usando std::replace