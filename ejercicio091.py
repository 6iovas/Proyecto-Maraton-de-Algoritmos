// Proyecto de Informatica
// Ejercicio 91
Título del Ejercicio: Frecuencia de Palabras
Código Fuente (C++):
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main(){
    int n; cin>>n;
    unordered_map<string,int> freq;
    for(int i=0;i<n;i++){ string s; cin>>s; freq[s]++;}

    for(auto p:freq) cout<<p.first<<": "<<p.second<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada hola mundo hola ? Salida: hola:2 mundo:1

90. Mantener top k números más grandes con priority_queue