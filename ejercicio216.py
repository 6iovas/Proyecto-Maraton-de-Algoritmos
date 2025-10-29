// Proyecto de Informatica
// Ejercicio 216
Ejercicio 11  Binary Search on Answer: Aggressive Cows / maximizar la mínima distancia
Análisis del problema
 Dado un array de posiciones de n estancias en una granja y k vacas, colocar las vacas en estancias de forma que la mínima distancia entre dos vacas sea máxima. Problema clásico de "binary search on answer".
? Entradas: n (número de estancias), posiciones pos[i], k (nº vacas).

? Objetivo: devolver la máxima d tal que se puedan colocar k vacas con separación ? d.

? Complejidad objetivo: ordenar O(n log n) + verificación O(n) por prueba ? O(n log RANGE).

Código (C++)
#include <bits/stdc++.h>
using namespace std;

bool canPlace(const vector<long long>& pos, int k, long long d) {
    long long last = pos[0];
    int cnt = 1;
    for (size_t i = 1; i < pos.size() && cnt < k; ++i) {
        if (pos[i] - last >= d) {
            last = pos[i];
            ++cnt;
        }
    }
    return cnt >= k;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> pos(n);
    for (int i = 0; i < n; ++i) cin >> pos[i];
    sort(pos.begin(), pos.end());
    long long lo = 0, hi = pos.back() - pos.front(), ans = 0;
    while (lo <= hi) {
        long long mid = lo + (hi - lo) / 2;
        if (canPlace(pos, k, mid)) { ans = mid; lo = mid + 1; }
        else hi = mid - 1;
    }
    cout << ans << '\n';
    return 0;
}

Prueba
Entrada:

 5 3
1 2 8 4 9
?  Ordenadas: 1 2 4 8 9. Máxima mínima distancia = 3 (colocar en 1,4,8 o 1,4,9). Salida: 3.