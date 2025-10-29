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
