// Proyecto de Informatica
// Ejercicio 105
Ejercicio 103: Generar subconjuntos (potencia de un conjunto)
Análisis del Problema
 Generar todos los subconjuntos posibles (2? combinaciones) de un conjunto de elementos.
Diseño de la Solución
 Usar una máscara de bits de 0 a (2? - 1) para seleccionar elementos.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    for (int mask = 0; mask < (1 << n); ++mask) {
        cout << "{ ";
        for (int i = 0; i < n; ++i)
            if (mask & (1 << i)) cout << a[i] << ' ';
        cout << "}\n";
    }
}

Pruebas
? Entrada: 3 seguido de 1 2 3

Salida:

 { }
{ 1 }
{ 2 }
{ 1 2 }
{ 3 }
{ 1 3 }
{ 2 3 }
{ 1 2 3 }
?