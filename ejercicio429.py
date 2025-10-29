// Proyecto de Informatica
// Ejercicio 429
Título del Ejercicio: Crear Clase Persona
Análisis del Problema
? Descripción del Problema: Implementar una clase Persona con atributos nombre y edad y un método para saludar.

? Entradas y Salidas:

? Entrada: Nombre y edad.

? Salida: Saludo con información de la persona.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir clase Persona con atributos y método saludar().

2. Crear objeto y llamar método.

? Estructuras de Datos: Clase y objeto.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Persona{
public:
    string nombre;
    int edad;
    void saludar(){
        cout << "Hola, soy " << nombre << " y tengo " << edad << " años" << endl;
    }
};

int main() {
    Persona p;
    p.nombre="Juan";
    p.edad=25;
    p.saludar(); // Hola, soy Juan y tengo 25 años
    return 0;
}

Pruebas
? Caso 1: Juan, 25 ? saludo correcto

? Caso 2: Ana, 30 ? saludo correcto

? Caso 3: Pedro, 0 ? saludo correcto