// Proyecto de Informatica
// Ejercicio 147
Ejercicio 145: Calcular la moda de una lista de números
Análisis del Problema
 Determinar el número que aparece con mayor frecuencia en una lista.
Diseño de la Solución
 Usar std::map<int,int> para contar las frecuencias y luego seleccionar la clave con mayor valor.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    map<int,int> freq;
    for (int i=0;i<n;++i){
        int x; cin >> x;
        freq[x]++;
    }
    int moda=-1, maxf=0;
    for(auto &[num, f]:freq)
        if(f>maxf) maxf=f, moda=num;
    cout << "Moda: " << moda << " (frecuencia " << maxf << ")\n";
}

Pruebas
? Entrada: 7\n1 2 2 3 3 3 4

? Salida: Moda: 3 (frecuencia 3)