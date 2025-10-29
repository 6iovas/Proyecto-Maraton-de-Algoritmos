// Proyecto de Informatica
// Ejercicio 118
Ejercicio 116: Parseo eficiente usando std::string_view (split sin copiar)
Análisis del Problema
 Dado un string grande, imprimir sus palabras sin crear substrings (evitar copies).
Diseño de la Solución
 Usar string_view para apuntar a segmentos del string.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    getline(cin, s);
    string_view sv(s);
    size_t i=0;
    while(i < sv.size()){
        while(i<sv.size() && isspace((unsigned char)sv[i])) ++i;
        if(i>=sv.size()) break;
        size_t j=i;
        while(j<sv.size() && !isspace((unsigned char)sv[j])) ++j;
        cout << sv.substr(i, j-i) << '\n';
        i = j;
    }
    return 0;
}

Pruebas
? Entrada hola mundo desde string_view imprime cada palabra en su línea.