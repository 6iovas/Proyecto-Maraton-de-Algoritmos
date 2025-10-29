// Proyecto de Informatica
// Ejercicio 195
Ejercicio 191: Buscar skyline (problema clásico  eventos + multiset)
Análisis
 Dado conjunto de edificios (L,R,H), producir líneas del skyline.
Diseño
 Evento (L, -H), (R, +H), ordenar y usar multiset para alturas activas.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<tuple<int,int,int>> b(n);
    for(int i=0;i<n;++i) cin>>get<0>(b[i])>>get<1>(b[i])>>get<2>(b[i]);
    vector<pair<int,int>> events;
    for(auto &t: b){
        int L,R,H; tie(L,R,H)=t;
        events.push_back({L, -H});
        events.push_back({R, H});
    }
    sort(events.begin(), events.end(), [](auto &a, auto &b){
        if(a.first!=b.first) return a.first<b.first;
        return a.second<b.second;
    });
    multiset<int> heights; heights.insert(0);
    int prev=0;
    for(auto &e: events){
        int x=e.first, h=e.second;
        if(h<0) heights.insert(-h);
        else heights.erase(heights.find(h));
        int cur = *heights.rbegin();
        if(cur != prev){ cout<<x<<" "<<cur<<"\n"; prev=cur; }
    }
}

Prueba
? Edificios [(2,9,10),(3,7,15),(5,12,12)] produce puntos del skyline.