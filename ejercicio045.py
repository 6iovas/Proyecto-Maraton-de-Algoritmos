// Proyecto de Informatica
// Ejercicio 45
Ejercicio 43: Knapsack fraccional (greedy)
Análisis
 Objetos divisibles  tomar según relación value/weight.
Diseño
 Ordenar por ratio y llenar.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
struct Item{ double w,v; double r()const{return v/w;} };
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; double W; if(!(cin>>n>>W)) return 0;
    vector<Item> it(n);
    for(int i=0;i<n;++i) cin>>it[i].w>>it[i].v;
    sort(it.begin(), it.end(), [](const Item& a,const Item& b){ return a.r()>b.r(); });
    double value=0;
    for(auto &itx: it){
        if(W<=0) break;
        double take = min(W, itx.w);
        value += take * (itx.v / itx.w);
        W -= take;
    }
    cout<<fixed<<setprecision(6)<<value<<"\n";
    return 0;
}

Pruebas
? Casos clásicos  probar con valores simples.