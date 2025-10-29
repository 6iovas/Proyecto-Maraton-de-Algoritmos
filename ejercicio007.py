// Proyecto de Informatica
// Ejercicio 7
EJERCICIO #6 - Lógica de Ruta/Gráfico
#include <iostream>
using namespace std;

int main() {
   int posicion = 0; // Posicion inicial (similar a un punto de partida en un mapa)

   cout << "Inicio en la posicion: " << posicion << endl;

   // Secuencia de movimientos simples (pasos):
  
   // Movimiento 1: Avanza 8 pasos
   posicion = posicion + 8;
   cout << "Paso 1 (+8): " << posicion << endl;

   // Movimiento 2: Retrocede 3 pasos
   posicion = posicion - 3;
   cout << "Paso 2 (-3): " << posicion << endl;

   // Movimiento 3: Avanza 5 pasos
   posicion = posicion + 5;
   cout << "Paso 3 (+5): " << posicion << endl;

   cout << "Posicion final alcanzada: " << posicion << endl;
   return 0;
}