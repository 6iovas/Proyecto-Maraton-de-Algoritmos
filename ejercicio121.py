// Proyecto de Informatica
// Ejercicio 121
Ejercicio 119: Esqueleto de custom allocator para std::vector (plantilla)
Análisis del Problema
 Mostrar cómo declarar un allocator personalizado (conceptual, simplificado).
Diseño de la Solución
 Proveer clase SimpleAlloc adaptada a std::allocator_traits (ejemplo funcional básico que usa ::operator new/delete).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

template <typename T>
struct SimpleAlloc {
    using value_type = T;
    SimpleAlloc() = default;
    template <class U> constexpr SimpleAlloc(const SimpleAlloc<U>&) noexcept {}
    T* allocate(size_t n) { return static_cast<T*>(::operator new(n * sizeof(T))); }
    void deallocate(T* p, size_t) noexcept { ::operator delete(p); }
};

int main(){
    vector<int, SimpleAlloc<int>> v;
    for(int i=0;i<10;++i) v.push_back(i);
    for(int x: v) cout << x << ' ';
    cout << '\n';
    return 0;
}

Pruebas
? Ejecutar: imprime 0 1 2 3 4 5 6 7 8 9.