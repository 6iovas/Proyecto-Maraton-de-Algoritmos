// Proyecto de Informatica
// Ejercicio 9
EJERCICIO #8Definir un Objeto Simple (struct básico)
C++
#include <iostream>
#include <string>
using namespace std;

// Definimos la estructura (similar a un objeto con propiedades)
struct Estudiante {
   string nombre;
   int edad;
};

int main() {
   // Declarar e inicializar un objeto de ese tipo
   Estudiante miEstudiante;

   // Asignar datos (miembros del objeto)
   miEstudiante.nombre = "Andrea";
   miEstudiante.edad = 19;

   cout << "--- Datos del Estudiante ---" << endl;
   cout << "Nombre: " << miEstudiante.nombre << endl;
   cout << "Edad: " << miEstudiante.edad << " anios" << endl;
   return 0;
}