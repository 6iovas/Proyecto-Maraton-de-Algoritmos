// Proyecto de Informatica
// Ejercicio 97
Título del Ejercicio: Ordenar Personas por Nombre
Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Persona{
    string nombre;
    int edad;
};

int main(){
    int n; cin>>n;
    vector<Persona> personas(n);
    for(int i=0;i<n;i++) cin>>personas[i].nombre>>personas[i].edad;

    sort(personas.begin(),personas.end(),[](Persona a,Persona b){ return a.nombre<b.nombre; });

    cout<<"Personas ordenadas por nombre:\n";
    for(auto p:personas) cout<<p.nombre<<" "<<p.edad<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada Juan 25, Ana 20 ? Salida: Ana 20, Juan 25
96. Contar frecuencia de números usando std::map