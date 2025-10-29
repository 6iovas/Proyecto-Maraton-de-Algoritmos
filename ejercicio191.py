// Proyecto de Informatica
// Ejercicio 191
Ejercicio 187: Validar paréntesis (stack)
Análisis
 Comprobar si una cadena de paréntesis ()[]{} está bien balanceada.
Diseño
 Usar stack<char> y mapa de pares de cierre->apertura.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; if(!(cin>>s)) return 0;
    stack<char> st;
    unordered_map<char,char> mp = {{')','('},{']','['},{'}','{'}};
    for(char c: s){
        if(c=='('||c=='['||c=='{') st.push(c);
        else {
            if(st.empty() || st.top()!=mp[c]){ cout<<"NO\n"; return 0; }
            st.pop();
        }
    }
    cout << (st.empty() ? "YES\n" : "NO\n");
}

Prueba
? ()[]{} -> YES

? ([)] -> NO