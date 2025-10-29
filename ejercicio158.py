// Proyecto de Informatica
// Ejercicio 158
Ejercicio 155: Calcular la mediana de un vector
Análisis del Problema
 Hallar la mediana (valor central) de un conjunto de números.
Diseño de la Solución
 Ordenar el vector y devolver el elemento medio (o promedio de los dos centrales si n es par).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    vector<double> v(n);
    for(double &x:v) cin >> x;
    sort(v.begin(), v.end());
    double med = (n%2 ? v[n/2] : (v[n/2-1]+v[n/2])/2.0);
    cout << "Mediana: " << fixed << setprecision(2) << med << "\n";
}

Pruebas
? Entrada: 5\n1 3 2 5 4 ? Salida: Mediana: 3.00

? Entrada: 4\n10 20 30 40 ? Mediana: 25.00