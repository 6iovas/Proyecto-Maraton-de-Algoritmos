// Proyecto de Informatica
// Ejercicio 224
Ejercicio 19  Mos Algorithm (offline queries on array  frequency & distinct count)
Análisis del problema
 Resolver múltiples queries offline de tipo ¿cuántos valores distintos en [L,R]? en un array sin updates. Mo hace O((n+q) * sqrt(n)) y es muy efectivo en práctica.
? Entradas: array a (n), q queries (L,R).

? Salida: distinct count per query.

Diseño de la solución
? Reordenar queries por bloque L (size ~ sqrt(n)) y R.

? Mantener cnt[value] y current distinct while moving pointers curL, curR incrementally.

? Responder queries según orden y devolver en posición correcta.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct Query { int l,r,idx; };
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,q; if(!(cin>>n>>q)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    // coordinate compress if needed
    vector<int> comp = a;
    sort(comp.begin(), comp.end());
    comp.erase(unique(comp.begin(), comp.end()), comp.end());
    for(int i=0;i<n;++i) a[i] = lower_bound(comp.begin(), comp.end(), a[i]) - comp.begin();

    int S = max(1, (int)sqrt(n));
    vector<Query> qs(q);
    for(int i=0;i<q;++i){ cin>>qs[i].l>>qs[i].r; qs[i].idx=i; }
    sort(qs.begin(), qs.end(), [&](const Query &A, const Query &B){
        int ablock = A.l / S, bblock = B.l / S;
        if(ablock != bblock) return ablock < bblock;
        return (ablock & 1) ? (A.r > B.r) : (A.r < B.r);
    });
    vector<int> ans(q);
    vector<int> cnt(comp.size(), 0);
    int curL=0, curR=-1;
    int distinct = 0;
    auto add = [&](int idx){
        int v = a[idx];
        if(cnt[v]==0) ++distinct;
        ++cnt[v];
    };
    auto remove = [&](int idx){
        int v = a[idx];
        --cnt[v];
        if(cnt[v]==0) --distinct;
    };
    for(auto &Q: qs){
        while(curL > Q.l) add(--curL);
        while(curR < Q.r) add(++curR);
        while(curL < Q.l) remove(curL++);
        while(curR > Q.r) remove(curR--);
        ans[Q.idx] = distinct;
    }
    for(int i=0;i<q;++i) cout<<ans[i]<<"\n";
    return 0;
}

Prueba
? a = [1,1,2,1,3], queries: [0,2],[1,4] ? distincts 2 and 3.