// Proyecto de Informatica
// Ejercicio 5
EJERCICIO #4 - Lógica de Ciclos
#include <iostream>
using namespace std;

int main() {
   int limite = 10;

   cout << "Contando del 1 al " << limite << ":" << endl;

   // Usamos el ciclo 'for' para repetir una accion
   for (int i = 1; i <= limite; i++) {
       cout << "Numero: " << i << endl;
   }
  
   return 0;
}