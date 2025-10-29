// Proyecto de Informatica
// Ejercicio 8
EJERCICIO #7Contador de Vocales (Precursor de std::map para Frecuencia)
C++
#include <iostream>
#include <string>
using namespace std;

int main() {
   string palabra = "algoritmo";
   int contador_o = 0;
   int longitud = palabra.length();

   cout << "Palabra a analizar: " << palabra << endl;

   // Recorrer la palabra caracter por caracter
   for (int i = 0; i < longitud; i++) {
       // Usar 'if' para verificar el caracter en esa posicion
       if (palabra[i] == 'o') {
           contador_o++; // Aumentar el conteo
       }
   }

   cout << "La vocal 'o' aparece " << contador_o << " veces en la palabra." << endl;
   return 0;
}