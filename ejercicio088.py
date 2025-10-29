// Proyecto de Informatica
// Ejercicio 88
Título del Ejercicio: Ordenar Estudiantes por Nota
Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Estudiante{
    string nombre;
    int nota;
};

int main(){
    int n; cin>>n;
    vector<Estudiante> v(n);
    for(int i=0;i<n;i++) cin>>v[i].nombre>>v[i].nota;

    sort(v.begin(),v.end(),[](Estudiante a,Estudiante b){ return a.nota>b.nota; });

    for(auto e:v) cout<<e.nombre<<" "<<e.nota<<endl;
    return 0;
}

Pruebas:
? Caso 1: [Ana 90, Juan 85] ? Salida: Ana 90, Juan 85
87. Contar elementos duplicados usando std::multiset