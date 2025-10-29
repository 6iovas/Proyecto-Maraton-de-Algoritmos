// Proyecto de Informatica
// Ejercicio 192
Ejercicio 188: Validar número palíndromo (sin usar string extra)
Análisis
 Determinar si un entero es palíndromo sin convertir a string.
Diseño
 Dar vuelta la mitad del número (evitar overflow).
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    long long x; if(!(cin>>x)) return 0;
    if(x<0 || (x%10==0 && x!=0)){ cout<<"NO\n"; return 0; }
    long long rev=0;
    while(x>rev){
        rev = rev*10 + x%10;
        x /= 10;
    }
    cout << (x==rev || x==rev/10 ? "YES\n" : "NO\n");
}

Prueba
? 121 -> YES

? 10 -> NO