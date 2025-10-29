// Proyecto de Informatica
// Ejercicio 207
Ejercicio 3  k-ésimo más grande con selección determinista (Median of Medians)  O(n) worst-case
Análisis del problema
 Encontrar el k-ésimo elemento más grande (o k-ésimo por orden) en tiempo O(n) en el peor caso usando el algoritmo Median of Medians (Selección determinista). Entrada: vector a de n elementos distintos (o con duplicados), k (1-based: k=1 ? máximo).
Diseño de la solución
? Implementar select(a, l, r, k) usando pivot obtenido por median-of-medians: dividir en grupos de 5, hallar medianas, recursivamente encontrar mediana de las medianas.

? Partición al estilo Lomuto u Hoare con pivot especificado.

? Complejidad worst-case O(n).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using vi = vector<long long>;

int partition(vi &a, int l, int r, long long pivot) {
    int i = l;
    for (int j = l; j <= r; ++j) {
        if (a[j] < pivot) swap(a[i++], a[j]);
    }
    int pivotPos = i;
    for (int j = i; j <= r; ++j) if (a[j] == pivot) { swap(a[pivotPos], a[j]); break; }
    return pivotPos;
}

long long median_of_medians(vi &a, int l, int r) {
    int n = r - l + 1;
    if (n <= 5) {
        sort(a.begin() + l, a.begin() + r + 1);
        return a[l + n/2];
    }
    int cnt = 0;
    for (int i = l; i <= r; i += 5) {
        int sub_r = min(i+4, r);
        sort(a.begin()+i, a.begin()+sub_r+1);
        swap(a[l + cnt], a[i + (sub_r - i)/2]);
        ++cnt;
    }
    // recursively find median of medians stored starting at a[l]
    return median_of_medians(a, l, l + cnt - 1);
}

long long select_kth(vi &a, int l, int r, int k) { // k is 0-based
    if (l == r) return a[l];
    long long pivot = median_of_medians(a, l, r);
    int pivotIndex = partition(a, l, r, pivot);
    int leftSize = pivotIndex - l;
    if (k < leftSize) return select_kth(a, l, pivotIndex - 1, k);
    else if (k == leftSize) return a[pivotIndex];
    else return select_kth(a, pivotIndex + 1, r, k - leftSize - 1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vi a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int k; cin>>k; // 1-based: k=1 -> largest
    if(k<1||k>n){ cout<<"Error\n"; return 0; }
    // find k-th largest: convert to (n-k)-th smallest (0-based)
    int idx = n - k;
    long long val = select_kth(a, 0, n-1, idx);
    cout<<val<<"\n";
    return 0;
}

Pruebas
? Entrada: 6 7 10 4 3 20 15 k=3 ? tercer más grande = 7 (orden descendente 20,15,10,7,4,3 ? 3rd=10? Wait: check mapping: n=6, k=3 => idx=3 -> 0-based smallest -> sorted ascending 3,4,7,10,15,20 -> idx=3 => 10 => 3rd largest = 10) Salida: 10.

? Nota: verificar conversion k?idx correctamente.