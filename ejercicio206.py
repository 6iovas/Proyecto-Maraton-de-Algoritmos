// Proyecto de Informatica
// Ejercicio 206
Ejercicio 2  MergeSort estable para objetos (orden por campo primario y secundario)
Análisis del problema
 Ordenar un vector de objetos struct Item { string name; int age; double score; } por age ascendente y score descendente; mantener estabilidad para name si age y score iguales. Implementar MergeSort estable para objetos (O(n log n), uso de memoria O(n)).
Diseño de la solución
? Emplear MergeSort recursivo que construye vectores temporales; el merge debe copiar en orden garantizando estabilidad.

? Comparator: (a.age, -a.score, original_index)  para preservar orden estable ante igualdad, podemos capturar índice original. Pero como MergeSort es estable, si comparator no rompe igualdad se mantiene el orden.

Código (C++)
#include <bits/stdc++.h>
using namespace std;

struct Item {
    string name;
    int age;
    double score;
    int idx; // original index to illustrate stability (not required if sort stable)
};

bool cmp(const Item &a, const Item &b) {
    if (a.age != b.age) return a.age < b.age;
    if (a.score != b.score) return a.score > b.score; // score desc
    return a.idx < b.idx; // tie-breaker to show stability explicitly
}

void merge_sort(vector<Item>& a, int l, int r, vector<Item>& tmp) {
    if (r - l <= 0) return;
    int m = (l + r) >> 1;
    merge_sort(a, l, m, tmp);
    merge_sort(a, m+1, r, tmp);
    int i = l, j = m+1, k = l;
    while (i <= m && j <= r) {
        if (cmp(a[i], a[j])) tmp[k++] = a[i++];
        else tmp[k++] = a[j++];
    }
    while (i <= m) tmp[k++] = a[i++];
    while (j <= r) tmp[k++] = a[j++];
    for (int t = l; t <= r; ++t) a[t] = tmp[t];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin >> n)) return 0;
    vector<Item> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].name >> a[i].age >> a[i].score;
        a[i].idx = i;
    }
    vector<Item> tmp(n);
    merge_sort(a, 0, n-1, tmp);
    for (auto &it : a) cout << it.name << ' ' << it.age << ' ' << it.score << '\n';
    return 0;
}

Pruebas
Entrada ejemplo:

 4
Ana 25 88.5
Luis 25 90.0
Maria 22 95.0
Ana2 25 90.0
 Salida (orden por age asc, score desc, estabilidad manteniendo idx):

 Maria 22 95.0
Luis 25 90.0
Ana2 25 90.0
Ana 25 88.5
?