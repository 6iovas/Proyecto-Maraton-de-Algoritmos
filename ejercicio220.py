// Proyecto de Informatica
// Ejercicio 220
Ejercicio 15  Z-Algorithm (array Z) y aplicaciones (pattern matching & longest substring)
Análisis del problema
 Implementar Z-array (Z-algorithm) que para cada pos i devuelve la longitud del mayor prefijo de s que comienza en i. Sirve para búsqueda de patrón y otras aplicaciones en O(n).
Diseño de la solución
? Calcular Z en O(n) usando ventana [L,R].

? Para pattern matching, construir P + '#' + T y usar Z para localizar posiciones Z[i] >= |P|.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
vector<int> z_function(const string &s){
    int n = s.size();
    vector<int> z(n);
    int l=0, r=0;
    for(int i=1;i<n;++i){
        if(i<=r) z[i] = min(r-i+1, z[i-l]);
        while(i+z[i]<n && s[z[i]]==s[i+z[i]]) ++z[i];
        if(i+z[i]-1 > r){ l=i; r=i+z[i]-1; }
    }
    return z;
}
vector<int> findPattern(const string &text, const string &pat){
    string s = pat + "#" + text;
    auto z = z_function(s);
    vector<int> res;
    int m = pat.size();
    for(int i=0;i<(int)z.size();++i){
        if(z[i] >= m) res.push_back(i - m - 1);
    }
    return res;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string T,P; if(!(cin>>T>>P)) return 0;
    auto occ = findPattern(T,P);
    for(int i:occ) cout<<i<<" ";
    cout<<"\n";
    return 0;
}

Prueba
? T="aaaabaaaab", P="aaab" ? ocurrencias en índices correspondientes.