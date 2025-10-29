// Proyecto de Informatica
// Ejercicio 128
Ejercicio 126: Implementar Bloom Filter simple (probabilístico)
Análisis del Problema
 Estructura probabilística para test membership con falsos positivos posibles.
Diseño de la Solución
 Bitset + múltiples hashes (usaremos std::hash with salts).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct Bloom {
    vector<bool> bits;
    int m, k;
    Bloom(int m_, int k_): m(m_), k(k_), bits(m_) {}
    void add(const string &s){
        for(int i=0;i<k;++i){
            size_t h = hash<string>{}(s + to_string(i));
            bits[h % m] = true;
        }
    }
    bool possiblyContains(const string &s){
        for(int i=0;i<k;++i){
            size_t h = hash<string>{}(s + to_string(i));
            if(!bits[h % m]) return false;
        }
        return true;
    }
};

int main(){
    Bloom b(1000, 3);
    b.add("hello");
    cout << b.possiblyContains("hello") << '\n'; // likely 1
    cout << b.possiblyContains("world") << '\n'; // likely 0 (could be 1 due to FP)
    return 0;
}

Pruebas
? hello -> true; world usually false.