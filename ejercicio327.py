// Proyecto de Informatica
// Ejercicio 327
Título del Ejercicio: Clase Rectángulo con Área y Perímetro
Análisis del Problema
? Descripción del Problema: Crear clase Rectangulo con atributos base y altura y métodos para calcular área y perímetro.

? Entradas y Salidas:

? Entrada: Base y altura.

? Salida: Área y perímetro.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase Rectangulo.

2. Implementar métodos area() y perimetro().

3. Crear objeto e imprimir resultados.

? Estructuras de Datos: Clase con variables base y altura.

? Funciones Principales: main(), area(), perimetro().

Código Fuente (C++)
#include <iostream>
using namespace std;

class Rectangulo {
public:
    double base, altura;
    double area() { return base*altura; }
    double perimetro() { return 2*(base+altura); }
};

int main() {
    Rectangulo r;
    r.base=5; r.altura=3;
    cout << "Area: " << r.area() << ", Perimetro: " << r.perimetro() << endl;
    return 0;
}

Pruebas
? Caso 1: base=5, altura=3 ? Área=15, Perímetro=16

? Caso 2: base=10, altura=10 ? Área=100, Perímetro=40

? Caso 3: base=0, altura=5 ? Área=0, Perímetro=10