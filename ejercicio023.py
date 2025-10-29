// Proyecto de Informatica
// Ejercicio 23
Ejercicio 21: Ordenar objetos (struct) por múltiples claves
Análisis
 Ordenar una lista de Person{name, age} por age ascendente y name lexicográfico si edades iguales.
Diseño
 std::sort con comparator lambda.
Código
#include <bits/stdc++.h>
using namespace std;
struct Person { string name; int age; };

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<Person> v(n);
    for(int i=0;i<n;++i) cin>>v[i].name>>v[i].age;
    sort(v.begin(), v.end(), [](const Person& a, const Person& b){
        if(a.age != b.age) return a.age < b.age;
        return a.name < b.name;
    });
    for(auto &p: v) cout<<p.name<<' '<<p.age<<'\n';
    return 0;
}

Pruebas
? Input: 3 Ana 30 Luis 25 Ana 25 ? order: Ana 25 Luis 25 Ana 30.