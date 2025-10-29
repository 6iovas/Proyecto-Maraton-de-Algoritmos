// Proyecto de Informatica
// Ejercicio 217
Ejercicio 12  Convex Hull (Graham scan / Andrew monotone chain) y perímetro/área
Análisis del problema
 Dado un conjunto de n puntos en el plano, calcular el envolvente convexo (convex hull). Además devolver perímetro y área del polígono convexo.
? Entrada: n puntos (x,y).

? Salida: puntos del hull en orden, perímetro y área.

? Complejidad: O(n log n) por ordenamiento.

Diseño de la solución
? Usar algoritmo Andrew (monotone chain): ordenar por x, luego construir lower y upper hulls.

? Calcular perímetro sumando distancias euclidianas sucesivas (cerrar ciclo).

? Calcular área con fórmula del polígono (shoelace) sobre el hull.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct P { long long x, y; };
long long cross(const P &o, const P &a, const P &b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}
double dist(const P &a, const P &b) {
    long double dx = a.x - b.x, dy = a.y - b.y;
    return sqrt((double)(dx*dx + dy*dy));
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<P> pts(n);
    for(int i=0;i<n;++i) cin>>pts[i].x>>pts[i].y;
    sort(pts.begin(), pts.end(), [](const P&a,const P&b){ return a.x==b.x ? a.y<b.y : a.x<b.x; });
    vector<P> H;
    // lower
    for(auto &p: pts){
        while(H.size()>=2 && cross(H[H.size()-2], H[H.size()-1], p) <= 0) H.pop_back();
        H.push_back(p);
    }
    // upper
    size_t lower_size = H.size();
    for(int i = n-2; i>=0; --i){
        auto &p = pts[i];
        while(H.size()>=lower_size+1 && cross(H[H.size()-2], H[H.size()-1], p) <= 0) H.pop_back();
        H.push_back(p);
        if(i==0) break;
    }
    if(H.size()>1) H.pop_back(); // last equals first
    // output hull points
    cout<<"Hull size: "<<H.size()<<"\n";
    for(auto &p:H) cout<<p.x<<" "<<p.y<<"\n";
    // perimeter
    double per=0;
    for(size_t i=0;i<H.size();++i) per += dist(H[i], H[(i+1)%H.size()]);
    cout<<fixed<<setprecision(6)<<"Perimeter: "<<per<<"\n";
    // area (shoelace)
    long double area = 0;
    for(size_t i=0;i<H.size();++i){
        size_t j=(i+1)%H.size();
        area += (long double)H[i].x * H[j].y - (long double)H[j].x * H[i].y;
    }
    area = fabsl(area)/2.0;
    cout<<fixed<<setprecision(6)<<"Area: "<<(double)area<<"\n";
    return 0;
}

Prueba
? Entradas: los vértices de un rectángulo y algunos puntos interiores. Hull devolverá las cuatro esquinas, perímetro = suma lados, área = width*height.