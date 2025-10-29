// Proyecto de Informatica
// Ejercicio 4
EJERCICIO #3 - Técnica básica de Ordenamiento
#include <iostream>
using namespace std;

int main() {
   int a = 100;
   int b = 25;
   int temp; // Variable auxiliar necesaria para el intercambio

   cout << "--- Intercambio de Variables ---" << endl;
   cout << "Valores iniciales: A = " << a << ", B = " << b << endl;

   // PASO 1: Guardar el valor de A
   temp = a;

   // PASO 2: Poner el valor de B en A
   a = b;

   // PASO 3: Poner el valor guardado (original de A) en B
   b = temp;

   cout << "Valores despues del intercambio: A = " << a << ", B = " << b << endl;
   return 0;
}