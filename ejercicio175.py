// Proyecto de Informatica
// Ejercicio 175
Ejercicio 171: Uso de std::optional para parseo seguro
Análisis
 Mostrar uso de std::optional<T> para retorno que puede fallar.
Diseño
 Función to_int que devuelve optional<int>.
Código
#include <bits/stdc++.h>
using namespace std;
optional<int> to_int(const string& s){
    try{ size_t pos; int v=stoi(s,&pos); if(pos==s.size()) return v; else return nullopt; }
    catch(...) { return nullopt; }
}
int main(){
    string s; while(cin>>s){
        auto v=to_int(s);
        if(v) cout<<"INT "<<*v<<"\n"; else cout<<"BAD\n";
    }
}

Prueba
? Entrada: 123 abc 45 ? Salida: INT 123 BAD INT 45