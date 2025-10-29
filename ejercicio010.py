// Proyecto de Informatica
// Ejercicio 10
EJERCICIO #9Verificación de Existencia (Precursor de std::set)
#include <iostream>
#include <string>
using namespace std;

int main() {
   string colores[] = {"rojo", "azul", "verde", "amarillo"};
   int tamano = 4;
   string color_buscar;
   bool encontrado = false;

   cout << "Lista de colores: rojo, azul, verde, amarillo" << endl;
   cout << "Ingresa un color para verificar si esta en la lista: ";
   cin >> color_buscar;

   // Recorrer el arreglo y comparar
   for (int i = 0; i < tamano; i++) {
       if (colores[i] == color_buscar) {
           encontrado = true;
           break;
       }
   }

   if (encontrado) {
       cout << "El color '" << color_buscar << "' SI se encuentra." << endl;
   } else {
       cout << "El color '" << color_buscar << "' NO se encuentra." << endl;
   }
   return 0;