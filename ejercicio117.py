// Proyecto de Informatica
// Ejercicio 117
Ejercicio 115: std::promise / std::future ejemplo (productor-consumidor simple)
Análisis del Problema
 Coordinar hilo productor que envía un valor y el consumidor que lo recibe usando promise/future.
Diseño de la Solución
 Crear std::promise<int> p; std::future<int> f = p.get_future(); Productor set_value, consumidor f.get().
Código Fuente (C++)
#include <bits/stdc++.h>
#include <thread>
using namespace std;

int main(){
    promise<int> prom;
    future<int> fut = prom.get_future();

    thread producer([&prom](){
        this_thread::sleep_for(chrono::milliseconds(200));
        prom.set_value(123);
    });

    thread consumer([&fut](){
        cout << "Waiting for value...\n";
        int v = fut.get();
        cout << "Got value: " << v << '\n';
    });

    producer.join();
    consumer.join();
    return 0;
}

Pruebas
? Ejecutar, espera breve, imprime Got value: 123.