// Proyecto de Informatica
// Ejercicio 218
Ejercicio 13  Closest Pair of Points (divide-and-conquer, O(n log n))
Análisis del problema
 Dado n puntos en el plano, encontrar la distancia euclidiana mínima entre cualquier par de puntos. Debe ser O(n log n) usando D&C en lugar de O(n²).
? Restricción: puntos con coordenadas reales/enteras; n puede ser grande (? 2e5 en variantes).

? En la práctica usar ordenamiento por X y mantener banda por Y.

Diseño de la solución
1. Ordenar puntos por x.

2. Recursivamente resolver mitades, obtener d = min(dl, dr).

3. Construir vector de puntos cuya x esté dentro de d del corte, ordenado por y (optimización: mantener orden por y durante merge).

4. Para cada punto en banda comprobar hasta 7 siguientes puntos para distancias menores (teorema).

5. Devolver d.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct P { double x,y; };
double dist2(const P &a, const P&b){ double dx=a.x-b.x, dy=a.y-b.y; return dx*dx + dy*dy; }

double solveRec(vector<P>& pts, int l, int r, vector<P>& tmp){
    if(r - l <= 3){
        double d = 1e300;
        for(int i=l;i<=r;++i) for(int j=i+1;j<=r;++j) d=min(d, dist2(pts[i], pts[j]));
        sort(pts.begin()+l, pts.begin()+r+1, [](const P&a,const P&b){ return a.y < b.y; });
        return d;
    }
    int m=(l+r)/2;
    double midx = pts[m].x;
    double dl = solveRec(pts, l, m, tmp);
    double dr = solveRec(pts, m+1, r, tmp);
    double d = min(dl, dr);
    // merge by y into tmp
    merge(pts.begin()+l, pts.begin()+m+1, pts.begin()+m+1, pts.begin()+r+1, tmp.begin(), [](const P&a,const P&b){ return a.y < b.y; });
    copy(tmp.begin(), tmp.begin()+(r-l+1), pts.begin()+l);
    // build strip
    vector<P> strip;
    for(int i=l;i<=r;++i) if((pts[i].x - midx)*(pts[i].x - midx) < d) strip.push_back(pts[i]);
    for(size_t i=0;i<strip.size();++i){
        for(size_t j=i+1; j<strip.size() && (strip[j].y - strip[i].y)*(strip[j].y - strip[i].y) < d; ++j){
            d = min(d, dist2(strip[i], strip[j]));
        }
    }
    return d;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<P> pts(n);
    for(int i=0;i<n;++i) cin>>pts[i].x>>pts[i].y;
    sort(pts.begin(), pts.end(), [](const P&a,const P&b){ return a.x < b.x; });
    vector<P> tmp(n);
    double d2 = solveRec(pts, 0, n-1, tmp);
    cout<<fixed<<setprecision(6)<<sqrt(d2)<<"\n";
    return 0;
}

Prueba
? Puntos: (0,0),(1,1),(3,4),(7,8),(2,2) ? minimal distance between (1,1) and (2,2): sqrt(2) ~ 1.414214.