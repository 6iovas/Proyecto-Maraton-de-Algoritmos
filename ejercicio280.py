// Proyecto de Informatica
// Ejercicio 280
Ejercicio 47  Maximum Subarray Sum with divide-and-conquer (Kadane vs D&C)
Análisis
 Implementar maximum subarray sum using divide-and-conquer (useful didactic alternative to Kadane). Complexity O(n log n). Also show Kadane as faster linear method.
Diseño
? For segment [l,r], compute: left best, right best, prefix max, suffix max and combine. Return structure with these four values.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Node { ll sum, pref, suff, best; };
vector<ll> a;
Node mergeNode(const Node &L, const Node &R){
    Node res;
    res.sum = L.sum + R.sum;
    res.pref = max(L.pref, L.sum + R.pref);
    res.suff = max(R.suff, R.sum + L.suff);
    res.best = max({L.best, R.best, L.suff + R.pref});
    return res;
}
Node build(int l,int r){
    if(l==r) return Node{a[l], a[l], a[l], a[l]};
    int m=(l+r)/2;
    Node L = build(l,m), R = build(m+1,r);
    return mergeNode(L,R);
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    a.resize(n);
    for(int i=0;i<n;++i) cin>>a[i];
    Node res = build(0,n-1);
    cout<<res.best<<"\n";
    return 0;
}

Pruebas
? a = [-2,1,-3,4,-1,2,1,-5,4] ? best = 6 (subarray [4,-1,2,1]).