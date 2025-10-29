// Proyecto de Informatica
// Ejercicio 120
Ejercicio 118: Investigar colisiones en std::unordered_map (ver buckets, load factor)
Análisis del Problema
 Medir bucket_count, max_load_factor, load_factor tras insertar muchas claves.
Diseño de la Solución
 Insertar n enteros (o strings), imprimir bucket_count y load_factor.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    unordered_map<string,int> um;
    for(int i=0;i<n;++i){
        string s = "key_" + to_string(i);
        um[s] = i;
    }
    cout << "size: " << um.size() << '\n';
    cout << "bucket_count: " << um.bucket_count() << '\n';
    cout << "load_factor: " << um.load_factor() << '\n';
    cout << "max_load_factor: " << um.max_load_factor() << '\n';
    // show collisions per bucket (sample)
    int collisions = 0;
    for(size_t b = 0; b < um.bucket_count(); ++b){
        size_t bs = um.bucket_size(b);
        if(bs > 1) collisions += (bs - 1);
    }
    cout << "collisions (approx): " << collisions << '\n';
    return 0;
}

Pruebas
? Ejecutar con n=10000 y observar bucket metrics.