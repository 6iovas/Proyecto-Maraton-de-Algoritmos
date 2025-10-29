// Proyecto de Informatica
// Ejercicio 205
Ejercicio 1  Quicksort con pivote aleatorio (versión in-place, evitar peor caso)
Análisis del problema
 Implementar Quicksort in-place que use un pivote aleatorio para evitar el peor caso (arreglo ya ordenado). Debe ordenar vector<int> de tamaño n en tiempo promedio O(n log n) y espacio O(log n) (recursión).
Diseño de la solución
? Elegir pivote aleatorio entre [l,r].

? Partición (Hoare o Lomuto); aquí usamos partición de Hoare (mejor en práctica con pivote aleatorio).

? Llamadas recursivas sobre subarreglos menores y mayores.

? Para evitar desbordamiento de pila en distribuciones adversas, recursión sobre el subproblema más pequeño primero (tail recursion on larger subarray iterative or recursive on small then loop).

? Complejidad promedio: O(n log n); espacio O(log n) recursión promedio.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int hoare_partition(vi &a, int l, int r) {
    uniform_int_distribution<int> dist(l, r);
    int pivot = a[dist(rng)];
    int i = l - 1, j = r + 1;
    while (true) {
        do i++; while (a[i] < pivot);
        do j--; while (a[j] > pivot);
        if (i >= j) return j;
        swap(a[i], a[j]);
    }
}

void quicksort(vi &a, int l, int r) {
    while (l < r) {
        int p = hoare_partition(a, l, r);
        // recurse on smaller partition first
        if (p - l < r - (p + 1)) {
            quicksort(a, l, p);
            l = p + 1;
        } else {
            quicksort(a, p + 1, r);
            r = p;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; 
    if (!(cin >> n)) return 0;
    vi a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    quicksort(a, 0, n - 1);
    for (int x : a) cout << x << ' ';
    cout << '\n';
    return 0;
}

Pruebas
? Caso 1 (aleatorio): n=7, a=3 6 1 8 2 5 4 ? salida: 1 2 3 4 5 6 8.

? Caso 2 (ya ordenado): 1 2 3 4 5 ? mantiene estabilidad del orden relativo de valores iguales no garantizada; importante: corre rápido porque pivote aleatorio.

? Caso 3 (con duplicados): 4 4 4 4 ? ordenado igual.