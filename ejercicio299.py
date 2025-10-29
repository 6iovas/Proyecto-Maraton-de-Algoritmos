// Proyecto de Informatica
// Ejercicio 299
Título del Ejercicio: Clase CuentaBancaria con Depósito y Retiro
Análisis del Problema
? Descripción del Problema: Crear clase CuentaBancaria con atributo saldo y métodos depositar(), retirar() y consultarSaldo().

? Entradas y Salidas:

? Entrada: Monto a depositar o retirar.

? Salida: Saldo actualizado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase CuentaBancaria con atributo saldo.

2. Implementar métodos para depositar, retirar y mostrar saldo.

3. Crear objeto CuentaBancaria y realizar operaciones.

? Estructuras de Datos: Clase con variable saldo.

? Funciones Principales: main() y métodos de la clase.

Código Fuente (C++)
#include <iostream>

class CuentaBancaria {
private:
    double saldo;

public:
    CuentaBancaria() { saldo = 0; }

    void depositar(double monto) { saldo += monto; }

    void retirar(double monto) {
        if(monto <= saldo) saldo -= monto;
        else std::cout << "Saldo insuficiente.\n";
    }

    void consultarSaldo() { std::cout << "Saldo: " << saldo << std::endl; }
};

int main() {
    CuentaBancaria c;
    c.depositar(500);
    c.retirar(200);
    c.consultarSaldo(); // Saldo esperado: 300

    c.retirar(400); // Saldo insuficiente
    c.consultarSaldo(); // Saldo esperado: 300
    return 0;
}

Pruebas
? Caso 1: Depositar 500, retirar 200 ? Saldo 300

? Caso 2: Retirar 400 ? Saldo 300 y mensaje "Saldo insuficiente"

? Caso 3: Depositar 1000, retirar 500 ? Saldo 500