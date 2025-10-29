// Proyecto de Informatica
// Ejercicio 339
Título del Ejercicio: Clase CuentaBancaria con Depósito y Retiro
Análisis del Problema
? Descripción del Problema: Crear clase CuentaBancaria con saldo, y métodos para depositar, retirar y consultar saldo.

? Entradas y Salidas:

? Entrada: Monto a depositar o retirar.

? Salida: Saldo actualizado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir clase con atributo saldo.

2. Métodos: depositar(monto), retirar(monto) y consultar().

3. Crear objeto y probar operaciones.

? Estructuras de Datos: Clase con variable saldo.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

class CuentaBancaria {
    double saldo;
public:
    CuentaBancaria(double s=0) { saldo=s; }
    void depositar(double monto) { saldo+=monto; }
    void retirar(double monto) {
        if(monto>saldo) cout << "Saldo insuficiente\n";
        else saldo-=monto;
    }
    void consultar() { cout << "Saldo actual: " << saldo << endl; }
};

int main() {
    CuentaBancaria c(100);
    c.consultar(); // 100
    c.depositar(50);
    c.consultar(); // 150
    c.retirar(70);
    c.consultar(); // 80
    c.retirar(100); // Saldo insuficiente
    return 0;
}

Pruebas
? Caso 1: Depositar 50 ? Saldo actualizado 150

? Caso 2: Retirar 70 ? Saldo actualizado 80

? Caso 3: Retirar 100 ? Mensaje "Saldo insuficiente"