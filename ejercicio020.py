// Proyecto de Informatica
// Ejercicio 20
Ejercicio 19: k-ésimo elemento más grande (min-heap)
Análisis
 Encontrar k-ésimo mayor manteniendo un min-heap de tamaño k.
Diseño
 priority_queue<int, vector<int>, greater<int>>.
Código
#include <bits/stdc++.h>
using namespace std;

int kth_largest_heap(const vector<int>& a, int k) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int x : a) {
        pq.push(x);
        if ((int)pq.size() > k) pq.pop();
    }
    return pq.top();
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    int k; cin>>k;
    if(k<1 || k>n) { cout<<"Error\n"; return 0; }
    cout << kth_largest_heap(a,k) << '\n';
    return 0;
}

Pruebas
? a=[7 10 4 3 20 15], k=3 ? 7

? a=[5 5 5], k=2 ? 5

? k=1 ? máximo