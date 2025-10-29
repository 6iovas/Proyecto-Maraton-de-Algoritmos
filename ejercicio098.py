// Proyecto de Informatica
// Ejercicio 98
Título del Ejercicio: Frecuencia de Números
Código Fuente (C++):
#include <iostream>
#include <map>
using namespace std;

int main(){
    int n; cin>>n;
    map<int,int> freq;
    for(int i=0;i<n;i++){
        int x; cin>>x;
        freq[x]++;
    }

    cout<<"Frecuencia de números:\n";
    for(auto p:freq) cout<<p.first<<": "<<p.second<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [1 2 2 3] ? Salida: 1:1 2:2 3:1
97. Create Contar palabras más frecuentes con std::unordered_map