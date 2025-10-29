// Proyecto de Informatica
// Ejercicio 42
Ejercicio 40: Comparar rendimiento entre std::sort y un Quicksort propio
Análisis del Problema
 Comparar tiempos de ejecución entre std::sort y una implementación propia de Quicksort (Lomuto o Hoare) sobre diferentes tamaños y distribuciones de datos.
Diseño de la Solución
? Generar arrays de prueba (aleatorio, ordenado, inverso).

? Medir tiempo con std::chrono para std::sort y quicksort propio.

? Imprimir tiempos.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using clk = chrono::high_resolution_clock;

int partition_lomuto(vector<int>& a, int l, int r) {
    int pivot = a[r], i = l;
    for (int j = l; j < r; ++j) if (a[j] < pivot) swap(a[i++], a[j]);
    swap(a[i], a[r]); return i;
}
void quicksort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int p = partition_lomuto(a,l,r);
    quicksort(a,l,p-1); quicksort(a,p+1,r);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n; // tamaño
    vector<int> a(n);
    for (int i=0;i<n;++i) a[i] = rand(); // aleatorio
    auto b = a;

    auto t1 = clk::now();
    sort(a.begin(), a.end());
    auto t2 = clk::now();

    auto t3 = clk::now();
    quicksort(b,0,n-1);
    auto t4 = clk::now();

    auto std_dur = chrono::duration_cast<chrono::milliseconds>(t2 - t1).count();
    auto qs_dur = chrono::duration_cast<chrono::milliseconds>(t4 - t3).count();

    cout << "std::sort (ms): " << std_dur << "\n";
    cout << "quicksort own (ms): " << qs_dur << "\n";
    return 0;
}

Pruebas
? Ejecutar con n=10000, n=100000, datos ordenados/invertidos y comparar.