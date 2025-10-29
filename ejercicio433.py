// Proyecto de Informatica
// Ejercicio 433
Título del Ejercicio: Clase CuentaBancaria
Análisis del Problema
? Descripción del Problema: Implementar clase CuentaBancaria con métodos depositar, retirar y consultarSaldo.

? Entradas y Salidas:

? Entrada: Cantidad a depositar o retirar.

? Salida: Saldo actualizado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir clase con atributo saldo y métodos.

2. Crear objeto y realizar operaciones.

? Estructuras de Datos: Clase y objeto.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

class CuentaBancaria{
private:
    double saldo;
public:
    CuentaBancaria(){saldo=0;}
    void depositar(double monto){saldo+=monto;}
    void retirar(double monto){
        if(monto<=saldo) saldo-=monto;
        else cout << "Saldo insuficiente" << endl;
    }
    void consultarSaldo(){cout << "Saldo: " << saldo << endl;}
};

int main() {
    CuentaBancaria c;
    c.depositar(1000);
    c.retirar(500);
    c.consultarSaldo(); // 500
    return 0;
}

Pruebas
? Caso 1: depositar 1000, retirar 500 ? 500

? Caso 2: retirar 600 ? mensaje saldo insuficiente

? Caso 3: depositar 0 ? saldo correcto