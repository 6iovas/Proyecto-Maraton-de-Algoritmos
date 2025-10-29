// Proyecto de Informatica
// Ejercicio 119
Ejercicio 117: Validar emails con std::regex
Análisis del Problema
 Verificar si cadenas son correos electrónicos básicos usando regex.
Diseño de la Solución
 Patrón simple: ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$.
Código Fuente (C++)
#include <bits/stdc++.h>
#include <regex>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    regex email(R"(^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$)");
    string s;
    while(cin >> s){
        cout << s << ": " << (regex_match(s, email) ? "VALID" : "INVALID") << '\n';
    }
    return 0;
}

Pruebas
? test@example.com -> VALID; bad@com -> INVALID.