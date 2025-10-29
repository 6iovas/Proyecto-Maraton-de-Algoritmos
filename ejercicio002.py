// Proyecto de Informatica
// Ejercicio 2
EJERCICIO #1
CODIGO FUENTE

#include <iostream>
using namespace std;

int main() {
    float calificacion;

    // Solicitar al usuario que ingrese la calificación anual
    cout << "Ingrese la calificacion anual del estudiante (0 - 10): ";
    cin >> calificacion;

    // Verificar que la calificación esté dentro del rango válido
    if (calificacion < 0 || calificacion > 10) {
        cout << "Calificacion invalida. Debe estar entre 0 y 10." << endl;
        return 1; // Fin del programa con error
    }

    // Evaluar el resultado según el rango
    if (calificacion >= 7.0) {
        cout << "El estudiante ha APROBADO el año lectivo." << endl;
    } else if (calificacion >= 4.0) {
        cout << "El estudiante se encuentra en SUPLETORIO." << endl;
    } else {
        cout << "El estudiante ha REPROBADO el año lectivo." << endl;
    }

    return 0;
}




PRUEBAS: 
CASO1.- CALIFICACION 4
EL ESTUDIANTE ESTA EN SUPLETORIO
CASO2.- CALIFICACION 6.99
EL ESTUDIANTE ESTA EN SUPLETORIO
CASO3.- CALIFICACION 7
EL ESTUDIANTE APROBO LA ASIGNATURA