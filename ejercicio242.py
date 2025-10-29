// Proyecto de Informatica
// Ejercicio 242
Ejercicio 24  2D Fenwick Tree (BIT 2D)  range sum queries on grid with point updates
Análisis
 Soporta actualizaciones puntuales y consultas de suma en subrectángulo (1,1) a (x,y). Ideal para matrices dinámicas con consultas rectangulares. Complejidad O((log n)*(log m)) por operación.
Diseño
 Implementar BIT 2D clásico con add(x,y,val) y sum(x,y) (prefix sum). Para rectangular sum [x1,y1,x2,y2] usar inclusion-exclusion.
Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct BIT2D {
    int n,m;
    vector<vector<long long>> bit;
    BIT2D(int n=0,int m=0){ init(n,m); }
    void init(int _n,int _m){ n=_n; m=_m; bit.assign(n+1, vector<long long>(m+1,0)); }
    void add(int x,int y,long long val){
        for(int i=x;i<=n;i+=i&-i) for(int j=y;j<=m;j+=j&-j) bit[i][j]+=val;
    }
    long long sum(int x,int y){
        long long res=0;
        for(int i=x;i>0;i-=i&-i) for(int j=y;j>0;j-=j&-j) res+=bit[i][j];
        return res;
    }
    long long rangeSum(int x1,int y1,int x2,int y2){
        return sum(x2,y2) - sum(x1-1,y2) - sum(x2,y1-1) + sum(x1-1,y1-1);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    BIT2D bit(n,m);
    int q; cin>>q;
    while(q--){
        int type; cin>>type;
        if(type==1){ int x,y; long long v; cin>>x>>y>>v; bit.add(x,y,v); }
        else { int x1,y1,x2,y2; cin>>x1>>y1>>x2>>y2; cout<<bit.rangeSum(x1,y1,x2,y2)<<"\n"; }
    }
    return 0;
}

Pruebas
? n=m=4, add(2,3,5), query(1,1,3,3) => 5.