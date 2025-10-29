// Proyecto de Informatica
// Ejercicio 500
Ejercicio 113
Título del Ejercicio: Calcular Potencia Recursiva
Análisis del Problema
? Descripción del Problema: Calcular base^exponente usando recursión.

? Entradas y Salidas:

? Entrada: Base y exponente enteros.

? Salida: Resultado de la potencia.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si exponente=0 ? retornar 1.

2. Retornar base * potencia(base, exponente-1).

? Estructuras de Datos: Enteros.

? Funciones Principales: main() y potenciaRecursiva().

Código Fuente (C++)
#include <iostream>
using namespace std;

int potenciaRecursiva(int base, int exp){
    if(exp==0) return 1;
    return base*potenciaRecursiva(base,exp-1);
}

int main() {
    int base=2, exp=5;
    cout << base << "^" << exp << " = " << potenciaRecursiva(base,exp) << endl; // 32
    return 0;
}

Pruebas
? Caso 1: 2^5 ? 32

? Caso 2: 3^3 ? 27

? Caso 3: 5^0 ? 1


Ejercicio 114
Título del Ejercicio: Factorial Recursivo
Análisis del Problema
? Descripción del Problema: Calcular el factorial de un número usando recursión.

? Entradas y Salidas:

? Entrada: Número entero n.

? Salida: Factorial de n.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si n=0 o n=1 ? retornar 1.

2. Retornar n * factorial(n-1).

? Estructuras de Datos: Enteros.

? Funciones Principales: main() y factorial().

Código Fuente (C++)
#include <iostream>
using namespace std;

int factorial(int n){
    if(n==0 || n==1) return 1;
    return n*factorial(n-1);
}

int main() {
    int n=5;
    cout << "Factorial de " << n << " = " << factorial(n) << endl; // 120
    return 0;
}

Pruebas
? Caso 1: 5! ? 120

? Caso 2: 0! ? 1

? Caso 3: 3! ? 6


Ejercicio 115
Título del Ejercicio: Sumar Números en Array con Punteros
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de un array usando punteros.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Suma de elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Usar puntero para recorrer array y sumar valores.

? Estructuras de Datos: Array de enteros y puntero.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4}, n=4, suma=0;
    int *p=arr;
    for(int i=0;i<n;i++) suma+=*(p+i);
    cout << "Suma de elementos: " << suma << endl; // 10
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4] ? 10

? Caso 2: [0,0,0] ? 0

? Caso 3: [5,5] ? 10


Ejercicio 116
Título del Ejercicio: Intercambiar Valores con Punteros
Análisis del Problema
? Descripción del Problema: Intercambiar los valores de dos variables usando punteros.

? Entradas y Salidas:

? Entrada: Dos enteros a y b.

? Salida: Valores intercambiados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar punteros para almacenar direcciones de a y b.

2. Intercambiar los valores usando variable temporal.

? Estructuras de Datos: Variables enteras y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int a=5, b=10;
    int *pa=&a, *pb=&b;
    int temp=*pa;
    *pa=*pb;
    *pb=temp;
    cout << "a=" << a << " b=" << b << endl; // a=10 b=5
    return 0;
}

Pruebas
? Caso 1: a=5, b=10 ? a=10, b=5

? Caso 2: a=0, b=0 ? a=0, b=0

? Caso 3: a=7, b=3 ? a=3, b=7


Ejercicio 117
Título del Ejercicio: Copiar Cadena con Punteros
Análisis del Problema
? Descripción del Problema: Copiar una cadena de caracteres usando aritmética de punteros.

? Entradas y Salidas:

? Entrada: Cadena origen.

? Salida: Cadena destino idéntica.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar punteros para recorrer la cadena origen.

2. Copiar carácter por carácter hasta '\0'.

? Estructuras de Datos: Cadena de caracteres y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    char origen[]="Hola Mundo";
    char destino[50];
    char *p1=origen, *p2=destino;
    while(*p1 != '\0') {
        *p2 = *p1;
        p1++;
        p2++;
    }
    *p2='\0';
    cout << "Cadena copiada: " << destino << endl; // Hola Mundo
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? "Hola Mundo"

? Caso 2: "" ? ""

? Caso 3: "C++" ? "C++"


Ejercicio 118
Título del Ejercicio: Crear Clase Persona
Análisis del Problema
? Descripción del Problema: Crear una clase Persona con atributos nombre y edad, y método saludar.

? Entradas y Salidas:

? Entrada: Nombre y edad.

? Salida: Mensaje de saludo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir clase Persona con atributos y método.

2. Crear objeto y llamar método.

? Estructuras de Datos: Clase y objetos.

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
        cout << "Hola, soy " << nombre << " y tengo " << edad << " años." << endl;
    }
};

int main() {
    Persona p;
    p.nombre="Juan";
    p.edad=25;
    p.saludar(); // Hola, soy Juan
Ejercicio 121
Título del Ejercicio: Crear Clase Libro
Análisis del Problema
? Descripción del Problema: Crear una clase Libro con propiedades título, autor y año, y un método para mostrar la información.

? Entradas y Salidas:

? Entrada: Título, autor y año del libro.

? Salida: Información completa del libro.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir clase Libro con atributos y método mostrar().

2. Crear objeto y asignar valores.

3. Llamar al método mostrar().

? Estructuras de Datos: Clase y objetos.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Libro{
public:
    string titulo;
    string autor;
    int anio;
    void mostrar(){
        cout << "Titulo: " << titulo << ", Autor: " << autor << ", Año: " << anio << endl;
    }
};

int main() {
    Libro libro1;
    libro1.titulo="C++ Basics";
    libro1.autor="Juan Perez";
    libro1.anio=2025;
    libro1.mostrar(); // Titulo: C++ Basics, Autor: Juan Perez, Año: 2025
    return 0;
}

Pruebas
? Caso 1: Titulo="C++ Basics", Autor="Juan Perez", Año=2025 ? Mostrar información correcta

? Caso 2: Titulo="Data Structures", Autor="Ana", Año=2024 ? Mostrar información correcta


Ejercicio 122
Título del Ejercicio: Crear Clase CuentaBancaria
Análisis del Problema
? Descripción del Problema: Crear una clase CuentaBancaria con métodos para depositar, retirar y consultar saldo.

? Entradas y Salidas:

? Entrada: Depósitos y retiros.

? Salida: Saldo actualizado y mensajes de operaciones.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir clase con atributo saldo y métodos depositar(), retirar(), mostrarSaldo().

2. Crear objeto y ejecutar operaciones.

? Estructuras de Datos: Clase y objeto.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

class CuentaBancaria{
private:
    double saldo;
public:
    CuentaBancaria(){ saldo=0; }
    void depositar(double monto){ saldo+=monto; }
    void retirar(double monto){
        if(monto>saldo) cout << "Fondos insuficientes." << endl;
        else saldo-=monto;
    }
    void mostrarSaldo(){ cout << "Saldo actual: " << saldo << endl; }
};

int main() {
    CuentaBancaria cuenta;
    cuenta.depositar(100);
    cuenta.retirar(30);
    cuenta.mostrarSaldo(); // Saldo actual: 70
    return 0;
}

Pruebas
? Caso 1: Depositar 100, retirar 30 ? Saldo 70

? Caso 2: Retirar 200 ? Mensaje de fondos insuficientes


Ejercicio 123
Título del Ejercicio: Buscar Máximo en Array
Análisis del Problema
? Descripción del Problema: Encontrar el valor máximo en un array.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Valor máximo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar max con primer elemento.

2. Recorrer array comparando cada elemento.

3. Actualizar max si se encuentra un valor mayor.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={5,8,2,10,3}, n=5, max=arr[0];
    for(int i=1;i<n;i++)
        if(arr[i]>max) max=arr[i];
    cout << "Valor maximo: " << max << endl; // 10
    return 0;
}

Pruebas
? Caso 1: [5,8,2,10,3] ? 10

? Caso 2: [1,1,1] ? 1

? Caso 3: [-5,-2,-3] ? -2


Ejercicio 124
Título del Ejercicio: Buscar Mínimo en Array
Análisis del Problema
? Descripción del Problema: Encontrar el valor mínimo en un array.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Valor mínimo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar min con primer elemento.

2. Recorrer array comparando cada elemento.

3. Actualizar min si se encuentra un valor menor.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={5,8,2,10,3}, n=5, min=arr[0];
    for(int i=1;i<n;i++)
        if(arr[i]<min) min=arr[i];
    cout << "Valor minimo: " << min << endl; // 2
    return 0;
}

Pruebas
? Caso 1: [5,8,2,10,3] ? 2

? Caso 2: [1,1,1] ? 1

? Caso 3: [-5,-2,-3] ? -5


Ejercicio 125
Título del Ejercicio: Calcular Promedio con Punteros
Análisis del Problema
? Descripción del Problema: Calcular el promedio de los elementos de un array usando punteros.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Promedio (float).

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer array usando puntero y acumular valores.

3. Dividir suma entre tamaño.

? Estructuras de Datos: Array y puntero.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={2,4,6,8}, n=4;
    int *p=arr, suma=0;
    for(int i=0;i<n;i++) suma+=*(p+i);
    cout << "Promedio: " << (float)suma/n << endl; // 5
    return 0;
}

Pruebas
? Caso 1: [2,4,6,8] ? 5

? Caso 2: [1,1,1] ? 1

? Caso 3: [5,10] ? 7.5


Ejercicio 126
Título del Ejercicio: Recorrer Array con Punteros
Análisis del Problema
? Descripción del Problema: Recorrer un array y mostrar cada elemento usando punteros.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Elementos impresos en consola.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar puntero al inicio del array.

2. Recorrer array incrementando el puntero y mostrando valores.

? Estructuras de Datos: Array y puntero.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4}, n=4;
    int *p=arr;
    for(int i=0;i<n;i++) cout << *(p+i) << " "; // 1 2 3 4
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4] ? 1 2 3 4

? Caso 2: [5,6] ? 5 6

? Caso 3: [0] ? 0


Ejercicio 127
Título del Ejercicio: Invertir Array con Punteros
Análisis del Problema
? Descripción del Problema: Invertir los elementos de un array usando punteros.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Array invertido.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar punteros al inicio y al final del array.

2. Intercambiar valores mientras inicio < fin.

? Estructuras de Datos: Array y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    int *inicio=arr, *fin=arr+n-1;
    while(inicio<fin){
        int temp=*inicio;
        *inicio=*fin;
        *fin=temp;
        inicio++; fin--;
    }
    for(int i=0;i<n;i++) cout << arr[i]
Ejercicio 131
Título del Ejercicio: Invertir Array con Punteros (continuación)
Análisis del Problema
? Descripción del Problema: Invertir los elementos de un array usando punteros.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Array invertido.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar punteros al inicio y al final del array.

2. Intercambiar valores mientras inicio < fin.

? Estructuras de Datos: Array y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    int *inicio=arr, *fin=arr+n-1;
    while(inicio<fin){
        int temp=*inicio;
        *inicio=*fin;
        *fin=temp;
        inicio++; fin--;
    }
    for(int i=0;i<n;i++) cout << arr[i] << " "; // 5 4 3 2 1
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? [5,4,3,2,1]

? Caso 2: [1,2] ? [2,1]

? Caso 3: [1] ? [1]


Ejercicio 132
Título del Ejercicio: Recorrer Matriz y Sumar Elementos
Análisis del Problema
? Descripción del Problema: Calcular la suma de todos los elementos de una matriz.

? Entradas y Salidas:

? Entrada: Matriz de enteros y dimensiones.

? Salida: Suma total.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer filas y columnas sumando elementos.

? Estructuras de Datos: Matriz 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][3]={{1,2,3},{4,5,6}}, suma=0;
    for(int i=0;i<2;i++)
        for(int j=0;j<3;j++)
            suma+=mat[i][j];
    cout << "Suma de elementos: " << suma << endl; // 21
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? 21

? Caso 2: [[0,0],[0,0]] ? 0

? Caso 3: [[-1,-2],[3,4]] ? 4


Ejercicio 133
Título del Ejercicio: Buscar Número en Matriz
Análisis del Problema
? Descripción del Problema: Verificar si un número existe en una matriz.

? Entradas y Salidas:

? Entrada: Matriz de enteros, dimensiones y número x.

? Salida: true si existe, false si no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer todas las posiciones de la matriz.

2. Comparar cada elemento con x.

? Estructuras de Datos: Matriz 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][2]={{1,2},{3,4}}, x=3;
    bool encontrado=false;
    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++)
            if(mat[i][j]==x) encontrado=true;
    if(encontrado) cout << x << " existe en la matriz" << endl;
    else cout << x << " no existe" << endl;
    return 0;
}

Pruebas
? Caso 1: x=3 ? existe

? Caso 2: x=5 ? no existe

? Caso 3: x=1 ? existe


Ejercicio 134
Título del Ejercicio: Sumar Diagonal Principal de Matriz
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de la diagonal principal de una matriz cuadrada.

? Entradas y Salidas:

? Entrada: Matriz cuadrada de tamaño n.

? Salida: Suma de la diagonal principal.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer posiciones [i][i] de la matriz.

2. Acumular los valores en suma.

? Estructuras de Datos: Matriz 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[3][3]={{1,2,3},{4,5,6},{7,8,9}}, suma=0;
    for(int i=0;i<3;i++) suma+=mat[i][i];
    cout << "Suma diagonal principal: " << suma << endl; // 15
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6],[7,8,9]] ? 15

? Caso 2: [[1,0],[0,1]] ? 2

? Caso 3: [[5]] ? 5


Ejercicio 135
Título del Ejercicio: Sumar Diagonal Secundaria de Matriz
Análisis del Problema
? Descripción del Problema: Calcular la suma de la diagonal secundaria de una matriz cuadrada.

? Entradas y Salidas:

? Entrada: Matriz cuadrada de tamaño n.

? Salida: Suma de diagonal secundaria.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer posiciones [i][n-1-i] de la matriz.

2. Acumular los valores en suma.

? Estructuras de Datos: Matriz 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[3][3]={{1,2,3},{4,5,6},{7,8,9}}, suma=0, n=3;
    for(int i=0;i<n;i++) suma+=mat[i][n-1-i];
    cout << "Suma diagonal secundaria: " << suma << endl; // 15
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6],[7,8,9]] ? 15

? Caso 2: [[1,0],[0,1]] ? 1

? Caso 3: [[5]] ? 5


Ejercicio 136
Título del Ejercicio: Multiplicar Elementos de Array por Escalar
Análisis del Problema
? Descripción del Problema: Multiplicar todos los elementos de un array por un número dado.

? Entradas y Salidas:

? Entrada: Array y número escalar.

? Salida: Array modificado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer array y multiplicar cada elemento por el escalar.

? Estructuras de Datos: Array.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4}, n=4, escalar=3;
    for(int i=0;i<n;i++) arr[i]*=escalar;
    for(int i=0;i<n;i++) cout << arr[i] << " "; // 3 6 9 12
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4], escalar=3 ? [3,6,9,12]

? Caso 2: [0,1], escalar=5 ? [0,5]


Ejercicio 137
Título del Ejercicio: Sumar Dos Arrays
Análisis del Problema
? Descripción del Problema: Sumar elemento a elemento dos arrays del mismo tamaño.

? Entradas y Salidas:

? Entrada: Dos arrays de tamaño n.

? Salida: Array resultado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer los arrays y sumar cada par de elementos.

2. Guardar resultado en un tercer array.

? Estructuras de Datos: Arrays.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int A[]={1,2,3}, B[]={4,5,6}, n=3, C[3];
    for(int i=0;i<n;i++) C[i]=A[i]+B[i];
    for(int i=0;i<n;i++) cout << C[i] << " "; // 5 7 9
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: A=[1,2,3], B=[4,5,6] ? [5,7,9]

? Caso 2: A=[0], B=[0] ? [0]


Ejercicio 138
Título del Ejercicio: Restar Dos Arrays
Análisis del Problema
? Descripción del Problema: Restar elemento a elemento dos arrays del mismo tamaño.

? Entradas y Salidas:

? Entrada: Dos arrays de tamaño n.

? Salida: Array resultado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer los arrays y restar cada par de elementos.

2. Guardar resultado en un tercer array.

? Estructuras de Datos: Arrays.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int A[]={5,6,7}, B[]={1,2,3}, n=3, C[3];
    for(int i=0;i<n;i++) C[i]=A[i]-B[i];
    for(int i=0;i<n;i++) cout << C[i] << " "; // 4 4 4
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: A=[5,6,7], B=[1,2,3] ? [4,4,4]

? Caso 2: A=[0], B=[0] ? [0]


Ejercicio 139
Título del Ejercicio: Contar Vocales en Cadena
Análisis del Problema
? Descripción del Problema: Contar la cantidad de vocales en una cadena de caracteres de forma recursiva.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de vocales.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si la cadena está vacía ? retornar 0.

2. Si primer carácter es vocal ? 1 + contar vocales resto.

3. Si no ? contar vocales resto.

? Estructuras de Datos: Cadena y función recursiva.

? Funciones Principales: main() y contarVocales().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int contarVocales(string s, int i=0){
    if(i==s.length()) return 0;
    char c=tolower(s[i]);
    if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u') return 1+contarVocales(s,i+1);
    return contarVocales(s,i+1);
}

int main() {
    string texto="Hola Mundo";
    cout << "Cantidad de vocales: " << contarVocales(texto) << endl; // 4
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? 4

? Caso 2: "xyz" ? 0

? Caso 3: "AEIOU" ? 5


Ejercicio 140
Título del Ejercicio: Contar Consonantes en Cadena
Análisis del Problema
? Descripción del Problema: Contar la cantidad de consonantes en una cadena de caracteres de forma recursiva.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de consonantes.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si la cadena está vacía ? retornar

Ejercicio 140 (continuación)
Título del Ejercicio: Contar Consonantes en Cadena
Análisis del Problema
? Descripción del Problema: Contar la cantidad de consonantes en una cadena de caracteres de forma recursiva.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de consonantes.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si la cadena está vacía ? retornar 0.

2. Si el carácter actual es consonante ? 1 + contar consonantes del resto.

3. Si no ? contar consonantes del resto.

? Estructuras de Datos: Cadena y función recursiva.

? Funciones Principales: main() y contarConsonantes().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

bool esConsonante(char c){
    c=tolower(c);
    return (c>='a' && c<='z') && !(c=='a'||c=='e'||c=='i'||c=='o'||c=='u');
}

int contarConsonantes(string s, int i=0){
    if(i==s.length()) return 0;
    if(esConsonante(s[i])) return 1+contarConsonantes(s,i+1);
    return contarConsonantes(s,i+1);
}

int main() {
    string texto="Hola Mundo";
    cout << "Cantidad de consonantes: " << contarConsonantes(texto) << endl; // 5
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? 5

? Caso 2: "AEIOU" ? 0

? Caso 3: "C++ Programming" ? 10


Ejercicio 141
Título del Ejercicio: Implementar Pila (Stack) con Array
Análisis del Problema
? Descripción del Problema: Crear una pila usando un array estático con operaciones push, pop y mostrar elementos.

? Entradas y Salidas:

? Entrada: Números a insertar o retirar.

? Salida: Estado actual de la pila.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir tamaño máximo y array para pila.

2. Usar variable top para controlar el tope de la pila.

3. Implementar funciones push(), pop() y mostrar().

? Estructuras de Datos: Array y variable top.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

#define MAX 5

class Pila {
    int arr[MAX];
    int top;
public:
    Pila(){ top=-1; }
    void push(int x){
        if(top==MAX-1) cout << "Pila llena\n";
        else arr[++top]=x;
    }
    void pop(){
        if(top==-1) cout << "Pila vacia\n";
        else top--;
    }
    void mostrar(){
        for(int i=top;i>=0;i--) cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Pila pila;
    pila.push(1);
    pila.push(2);
    pila.push(3);
    pila.mostrar(); // 3 2 1
    pila.pop();
    pila.mostrar(); // 2 1
    return 0;
}

Pruebas
? Caso 1: Push 1,2,3 ? Mostrar ? 3 2 1

? Caso 2: Pop ? Mostrar ? 2 1

? Caso 3: Pop 2 veces más ? Mostrar ? Pila vacía


Ejercicio 142
Título del Ejercicio: Implementar Cola (Queue) con Array
Análisis del Problema
? Descripción del Problema: Crear una cola usando array estático con operaciones enqueue, dequeue y mostrar.

? Entradas y Salidas:

? Entrada: Números a encolar o desencolar.

? Salida: Estado actual de la cola.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir array y variables front y rear.

2. Implementar enqueue() y dequeue().

3. Mostrar estado actual de la cola.

? Estructuras de Datos: Array y variables front/rear.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

#define MAX 5

class Cola {
    int arr[MAX];
    int front, rear;
public:
    Cola(){ front=0; rear=-1; }
    void enqueue(int x){
        if(rear==MAX-1) cout << "Cola llena\n";
        else arr[++rear]=x;
    }
    void dequeue(){
        if(front>rear) cout << "Cola vacia\n";
        else front++;
    }
    void mostrar(){
        for(int i=front;i<=rear;i++) cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Cola cola;
    cola.enqueue(1);
    cola.enqueue(2);
    cola.enqueue(3);
    cola.mostrar(); // 1 2 3
    cola.dequeue();
    cola.mostrar(); // 2 3
    return 0;
}

Pruebas
? Caso 1: Enqueue 1,2,3 ? Mostrar ? 1 2 3

? Caso 2: Dequeue ? Mostrar ? 2 3

? Caso 3: Dequeue todas ? Mostrar ? Cola vacía


Ejercicio 143
Título del Ejercicio: Sumar Elementos de Dos Matrices
Análisis del Problema
? Descripción del Problema: Sumar dos matrices del mismo tamaño elemento a elemento.

? Entradas y Salidas:

? Entrada: Dos matrices 2D de enteros.

? Salida: Matriz suma.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer filas y columnas de las matrices.

2. Sumar cada par de elementos y guardar en matriz resultado.

? Estructuras de Datos: Matrices 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int A[2][2]={{1,2},{3,4}}, B[2][2]={{5,6},{7,8}}, C[2][2];
    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++)
            C[i][j]=A[i][j]+B[i][j];
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++) cout << C[i][j] << " ";
        cout << endl;
    }
    return 0;
}

Pruebas
? Caso 1: [[1,2],[3,4]] + [[5,6],[7,8]] ? [[6,8],[10,12]]

? Caso 2: [[0,0],[0,0]] + [[1,1],[1,1]] ? [[1,1],[1,1]]


Ejercicio 144
Título del Ejercicio: Multiplicar Elementos de Dos Matrices
Análisis del Problema
? Descripción del Problema: Multiplicar elemento a elemento dos matrices del mismo tamaño.

? Entradas y Salidas:

? Entrada: Dos matrices 2D de enteros.

? Salida: Matriz resultado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer filas y columnas.

2. Multiplicar elementos correspondientes y guardar en matriz resultado.

? Estructuras de Datos: Matrices 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int A[2][2]={{1,2},{3,4}}, B[2][2]={{5,6},{7,8}}, C[2][2];
    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++)
            C[i][j]=A[i][j]*B[i][j];
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++) cout << C[i][j] << " ";
        cout << endl;
    }
    return 0;
}

Pruebas
? Caso 1: [[1,2],[3,4]] * [[5,6],[7,8]] ? [[5,12],[21,32]]

? Caso 2: [[1,1],[1,1]] * [[2,2],[2,2]] ? [[2,2],[2,2]]


Ejercicio 145
Título del Ejercicio: Sumar Fila de Matriz
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de una fila específica de una matriz.

? Entradas y Salidas:

? Entrada: Matriz, número de fila.

? Salida: Suma de la fila.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer la fila indicada y sumar elementos.

? Estructuras de Datos: Matriz 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[3][3]={{1,2,3},{4,5,6},{7,8,9}}, fila=1, suma=0;
    for(int j=0;j<3;j++) suma+=mat[fila][j];
    cout << "Suma fila " << fila << ": " << suma << endl; // 15
    return 0;
}

Pruebas
? Caso 1: fila 1 ? 4+5+6=15

? Caso 2: fila 0 ? 1+2+3=6

? Caso 3: fila 2 ? 7+8+9=24

Ejercicio 146
Título del Ejercicio: Sumar Columna de Matriz
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de una columna específica de una matriz.

? Entradas y Salidas:

? Entrada: Matriz, número de columna.

? Salida: Suma de la columna.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer la columna indicada y sumar elementos.

? Estructuras de Datos: Matriz 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[3][3]={{1,2,3},{4,5,6},{7,8,9}}, col=2, suma=0;
    for(int i=0;i<3;i++) suma+=mat[i][col];
    cout << "Suma columna " << col << ": " << suma << endl; // 18
    return 0;
}

Pruebas
? Caso 1: col=2 ? 3+6+9=18

? Caso 2: col=0 ? 1+4+7=12

? Caso 3: col=1 ? 2+5+8=15


Ejercicio 147
Título del Ejercicio: Calcular Factorial de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular el factorial de un número entero n usando recursividad.

? Entradas y Salidas:

? Entrada: Número entero n ? 0.

? Salida: Factorial de n.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si n=0 ? retornar 1.

2. Si n>0 ? retornar n * factorial(n-1).

? Estructuras de Datos: Variables enteras.

? Funciones Principales: main() y factorial().

Código Fuente (C++)
#include <iostream>
using namespace std;

int factorial(int n){
    if(n==0) return 1;
    return n*factorial(n-1);
}

int main() {
    int num=5;
    cout << "Factorial de " << num << ": " << factorial(num) << endl; // 120
    return 0;
}

Pruebas
? Caso 1: n=5 ? 120

? Caso 2: n=0 ? 1

? Caso 3: n=3 ? 6


Ejercicio 148
Título del Ejercicio: Calcular Potencia (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular la potencia de un número base elevado a exponente usando recursión.

? Entradas y Salidas:

? Entrada: base y exponente ? 0.

? Salida: Resultado base^exponente.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si exponente=0 ? retornar 1.

2. Si exponente>0 ? retornar base * potencia(base, exponente-1).

? Estructuras de Datos: Variables enteras.

? Funciones Principales: main() y potencia().

Código Fuente (C++)
#include <iostream>
using namespace std;

int potencia(int base, int exp){
    if(exp==0) return 1;
    return base*potencia(base, exp-1);
}

int main() {
    int base=2, exp=5;
    cout << base << "^" << exp << " = " << potencia(base, exp) << endl; // 32
    return 0;
}

Pruebas
? Caso 1: 2^5 ? 32

? Caso 2: 3^0 ? 1

? Caso 3: 5^3 ? 125


Ejercicio 149
Título del Ejercicio: Contar Números Pares en Array (Recursivo)
Análisis del Problema
? Descripción del Problema: Contar la cantidad de números pares en un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño n.

? Salida: Cantidad de números pares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño=0 ? retornar 0.

2. Si último elemento es par ? 1 + contar en el resto.

3. Si no ? contar en el resto.

? Estructuras de Datos: Array y función recursiva.

? Funciones Principales: main() y contarPares().

Código Fuente (C++)
#include <iostream>
using namespace std;

int contarPares(int arr[], int n){
    if(n==0) return 0;
    return (arr[n-1]%2==0) + contarPares(arr,n-1);
}

int main() {
    int arr[]={1,2,3,4,5,6}, n=6;
    cout << "Cantidad de pares: " << contarPares(arr,n) << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5,6] ? 3

? Caso 2: [1,3,5] ? 0

? Caso 3: [2,4,6,8] ? 4


Ejercicio 150
Título del Ejercicio: Contar Números Impares en Array (Recursivo)
Análisis del Problema
? Descripción del Problema: Contar la cantidad de números impares en un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño n.

? Salida: Cantidad de números impares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño=0 ? retornar 0.

2. Si último elemento es impar ? 1 + contar en el resto.

3. Si no ? contar en el resto.

? Estructuras de Datos: Array y función recursiva.

? Funciones Principales: main() y contarImpares().

Código Fuente (C++)
#include <iostream>
using namespace std;

int contarImpares(int arr[], int n){
    if(n==0) return 0;
    return (arr[n-1]%2!=0) + contarImpares(arr,n-1);
}

int main() {
    int arr[]={1,2,3,4,5,6}, n=6;
    cout << "Cantidad de impares: " << contarImpares(arr,n) << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5,6] ? 3

? Caso 2: [2,4,6] ? 0

? Caso 3: [1,3,5,7] ? 4


Ejercicio 151
Título del Ejercicio: Intercambiar Dos Variables Usando Punteros
Análisis del Problema
? Descripción del Problema: Intercambiar el valor de dos variables enteras usando punteros.

? Entradas y Salidas:

? Entrada: Dos números enteros.

? Salida: Números intercambiados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear punteros apuntando a las variables.

2. Usar variable temporal para intercambio.

? Estructuras de Datos: Variables enteras y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int a=5, b=10, *pa=&a, *pb=&b;
    int temp=*pa;
    *pa=*pb;
    *pb=temp;
    cout << "a=" << a << ", b=" << b << endl; // a=10, b=5
    return 0;
}

Pruebas
? Caso 1: a=5, b=10 ? a=10, b=5

? Caso 2: a=0, b=1 ? a=1, b=0

Ejercicio 146
Título del Ejercicio: Sumar Columna de Matriz
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de una columna específica de una matriz.

? Entradas y Salidas:

? Entrada: Matriz, número de columna.

? Salida: Suma de la columna.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer la columna indicada y sumar elementos.

? Estructuras de Datos: Matriz 2D.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[3][3]={{1,2,3},{4,5,6},{7,8,9}}, col=2, suma=0;
    for(int i=0;i<3;i++) suma+=mat[i][col];
    cout << "Suma columna " << col << ": " << suma << endl; // 18
    return 0;
}

Pruebas
? Caso 1: col=2 ? 3+6+9=18

? Caso 2: col=0 ? 1+4+7=12

? Caso 3: col=1 ? 2+5+8=15


Ejercicio 147
Título del Ejercicio: Calcular Factorial de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular el factorial de un número entero n usando recursividad.

? Entradas y Salidas:

? Entrada: Número entero n ? 0.

? Salida: Factorial de n.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si n=0 ? retornar 1.

2. Si n>0 ? retornar n * factorial(n-1).

? Estructuras de Datos: Variables enteras.

? Funciones Principales: main() y factorial().

Código Fuente (C++)
#include <iostream>
using namespace std;

int factorial(int n){
    if(n==0) return 1;
    return n*factorial(n-1);
}

int main() {
    int num=5;
    cout << "Factorial de " << num << ": " << factorial(num) << endl; // 120
    return 0;
}

Pruebas
? Caso 1: n=5 ? 120

? Caso 2: n=0 ? 1

? Caso 3: n=3 ? 6


Ejercicio 148
Título del Ejercicio: Calcular Potencia (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular la potencia de un número base elevado a exponente usando recursión.

? Entradas y Salidas:

? Entrada: base y exponente ? 0.

? Salida: Resultado base^exponente.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si exponente=0 ? retornar 1.

2. Si exponente>0 ? retornar base * potencia(base, exponente-1).

? Estructuras de Datos: Variables enteras.

? Funciones Principales: main() y potencia().

Código Fuente (C++)
#include <iostream>
using namespace std;

int potencia(int base, int exp){
    if(exp==0) return 1;
    return base*potencia(base, exp-1);
}

int main() {
    int base=2, exp=5;
    cout << base << "^" << exp << " = " << potencia(base, exp) << endl; // 32
    return 0;
}

Pruebas
? Caso 1: 2^5 ? 32

? Caso 2: 3^0 ? 1

? Caso 3: 5^3 ? 125


Ejercicio 149
Título del Ejercicio: Contar Números Pares en Array (Recursivo)
Análisis del Problema
? Descripción del Problema: Contar la cantidad de números pares en un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño n.

? Salida: Cantidad de números pares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño=0 ? retornar 0.

2. Si último elemento es par ? 1 + contar en el resto.

3. Si no ? contar en el resto.

? Estructuras de Datos: Array y función recursiva.

? Funciones Principales: main() y contarPares().

Código Fuente (C++)
#include <iostream>
using namespace std;

int contarPares(int arr[], int n){
    if(n==0) return 0;
    return (arr[n-1]%2==0) + contarPares(arr,n-1);
}

int main() {
    int arr[]={1,2,3,4,5,6}, n=6;
    cout << "Cantidad de pares: " << contarPares(arr,n) << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5,6] ? 3

? Caso 2: [1,3,5] ? 0

? Caso 3: [2,4,6,8] ? 4


Ejercicio 150
Título del Ejercicio: Contar Números Impares en Array (Recursivo)
Análisis del Problema
? Descripción del Problema: Contar la cantidad de números impares en un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño n.

? Salida: Cantidad de números impares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño=0 ? retornar 0.

2. Si último elemento es impar ? 1 + contar en el resto.

3. Si no ? contar en el resto.

? Estructuras de Datos: Array y función recursiva.

? Funciones Principales: main() y contarImpares().

Código Fuente (C++)
#include <iostream>
using namespace std;

int contarImpares(int arr[], int n){
    if(n==0) return 0;
    return (arr[n-1]%2!=0) + contarImpares(arr,n-1);
}

int main() {
    int arr[]={1,2,3,4,5,6}, n=6;
    cout << "Cantidad de impares: " << contarImpares(arr,n) << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5,6] ? 3

? Caso 2: [2,4,6] ? 0

? Caso 3: [1,3,5,7] ? 4


Ejercicio 151
Título del Ejercicio: Intercambiar Dos Variables Usando Punteros
Análisis del Problema
? Descripción del Problema: Intercambiar el valor de dos variables enteras usando punteros.

? Entradas y Salidas:

? Entrada: Dos números enteros.

? Salida: Números intercambiados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear punteros apuntando a las variables.

2. Usar variable temporal para intercambio.

? Estructuras de Datos: Variables enteras y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int a=5, b=10, *pa=&a, *pb=&b;
    int temp=*pa;
    *pa=*pb;
    *pb=temp;
    cout << "a=" << a << ", b=" << b << endl; // a=10, b=5
    return 0;
}

Pruebas
? Caso 1: a=5, b=10 ? a=10, b=5

? Caso 2: a=0, b=1 ? a=1, b=0

Ejercicio 152
Título del Ejercicio: Copiar Cadena con Aritmética de Punteros
Análisis del Problema
? Descripción del Problema: Copiar una cadena de caracteres a otra usando punteros y aritmética de punteros.

? Entradas y Salidas:

? Entrada: Cadena de caracteres fuente.

? Salida: Cadena de caracteres destino copiada.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear punteros apuntando al inicio de las cadenas.

2. Copiar carácter por carácter hasta encontrar el fin de la cadena ('\0').

? Estructuras de Datos: Arreglos de caracteres y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    char src[] = "Hola Mundo";
    char dest[50];
    char *pSrc = src;
    char *pDest = dest;
    while(*pSrc != '\0'){
        *pDest = *pSrc;
        pSrc++;
        pDest++;
    }
    *pDest = '\0';
    cout << "Cadena copiada: " << dest << endl; // Hola Mundo
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? "Hola Mundo"

? Caso 2: "" ? ""

? Caso 3: "C++" ? "C++"


Ejercicio 153
Título del Ejercicio: Crear Array Dinámico
Análisis del Problema
? Descripción del Problema: Crear un array de tamaño variable usando memoria dinámica (new).

? Entradas y Salidas:

? Entrada: Tamaño n del array.

? Salida: Array dinámico con valores ingresados por el usuario.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir al usuario el tamaño del array.

2. Reservar memoria dinámica con new.

3. Ingresar y mostrar elementos.

4. Liberar memoria con delete[].

? Estructuras de Datos: Array dinámico.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa tamaño del array: ";
    cin >> n;
    int *arr = new int[n];
    for(int i=0;i<n;i++){
        cout << "Elemento " << i << ": ";
        cin >> arr[i];
    }
    cout << "Elementos ingresados: ";
    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl;
    delete[] arr;
    return 0;
}

Pruebas
? Caso 1: n=3 ? elementos 1,2,3 ? salida 1 2 3

? Caso 2: n=0 ? salida vacía

? Caso 3: n=5 ? elementos 5,4,3,2,1 ? salida 5 4 3 2 1


Ejercicio 154
Título del Ejercicio: Clase Persona con Método Saludar
Análisis del Problema
? Descripción del Problema: Crear clase Persona con atributos nombre y edad, y método saludar() que imprima un saludo.

? Entradas y Salidas:

? Entrada: Nombre y edad.

? Salida: Saludo personalizado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase con atributos y constructor.

2. Implementar método saludar().

3. Crear objeto e invocar método.

? Estructuras de Datos: Clase y objeto.

? Funciones Principales: main() y métodos de clase.

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Persona {
public:
    string nombre;
    int edad;
    Persona(string n, int e){ nombre=n; edad=e; }
    void saludar(){ cout << "Hola, soy " << nombre << " y tengo " << edad << " años.\n"; }
};

int main() {
    Persona p("Juan", 25);
    p.saludar(); // Hola, soy Juan y tengo 25 años.
    return 0;
}

Pruebas
? Caso 1: "Juan", 25 ? "Hola, soy Juan y tengo 25 años."

? Caso 2: "Ana", 30 ? "Hola, soy Ana y tengo 30 años."


Ejercicio 155
Título del Ejercicio: Clase Libro con Método Mostrar Información
Análisis del Problema
? Descripción del Problema: Crear clase Libro con atributos titulo, autor, anio, y método mostrar() que muestre la información.

? Entradas y Salidas:

? Entrada: Título, autor y año.

? Salida: Información del libro.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase Libro con constructor.

2. Implementar método mostrar().

3. Crear objeto y llamar al método.

? Estructuras de Datos: Clase y objeto.

? Funciones Principales: main() y método de clase.

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Libro {
public:
    string titulo, autor;
    int anio;
    Libro(string t, string a, int an){ titulo=t; autor=a; anio=an; }
    void mostrar(){ cout << "Libro: " << titulo << ", Autor: " << autor << ", Año: " << anio << endl; }
};

int main() {
    Libro libro1("1984","George Orwell",1949);
    libro1.mostrar(); // Libro: 1984, Autor: George Orwell, Año: 1949
    return 0;
}

Pruebas
? Caso 1: "1984", "George Orwell", 1949 ? salida correcta

? Caso 2: "C++ Primer", "Lippman", 2012 ? salida correcta


Ejercicio 156
Título del Ejercicio: Clase CuentaBancaria con Depósito y Retiro
Análisis del Problema
? Descripción del Problema: Crear clase CuentaBancaria con atributos titular y saldo, y métodos depositar(), retirar(), consultarSaldo().

? Entradas y Salidas:

? Entrada: Cantidades a depositar o retirar.

? Salida: Saldo actualizado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase con atributos y métodos.

2. Crear objeto, depositar, retirar y mostrar saldo.

? Estructuras de Datos: Clase y variables.

? Funciones Principales: main() y métodos de clase.

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class CuentaBancaria {
    string titular;
    double saldo;
public:
    CuentaBancaria(string t, double s){ titular=t; saldo=s; }
    void depositar(double monto){ saldo+=monto; }
    void retirar(double monto){ if(monto<=saldo) saldo-=monto; else cout << "Saldo insuficiente\n"; }
    void consultarSaldo(){ cout << "Saldo de " << titular << ": " << saldo << endl; }
};

int main() {
    CuentaBancaria c("Juan",1000);
    c.depositar(500);
    c.retirar(200);
    c.consultarSaldo(); // 1300
    return 0;
}

Pruebas
? Caso 1: Depositar 500, retirar 200 ? saldo 1300

? Caso 2: Retirar 1500 ? "Saldo insuficiente"


Ejercicio 157
Título del Ejercicio: Verificar Si Array Está Ordenado
Análisis del Problema
? Descripción del Problema: Determinar si un array de enteros está ordenado de forma ascendente.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: true si está ordenado, false si no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer el array y comparar cada elemento con el siguiente.

2. Si alguno no cumple, retornar false.

? Estructuras de Datos: Array.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

bool estaOrdenado(int arr[], int n){
    for(int i=0;i<n-1;i++)
        if(arr[i]>arr[i+1]) return false;
    return true;
}

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    if(estaOrdenado(arr,n)) cout << "Array ordenado\n";
    else cout << "Array no ordenado\n";
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? ordenado

? Caso 2: [5,3,4] ? no ordenado


Ejercicio 158
Título del Ejercicio: Encontrar Mayor Elemento en Array
Análisis del Problema
? Descripción del Problema: Encontrar el elemento máximo en un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Elemento máximo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar max con el primer elemento.

2. Recorrer array comparando y actualizando max.

? Estructuras de Datos: Array.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={3,7,2,9,5}, n=5;
    int max=arr[0];
    for(int i=1;i<n;i++) if(arr[i]>max) max=arr[i];
    cout << "Mayor elemento: " << max << endl; // 9
    return 0;
}

Pruebas
? Caso 1: [3,7,2,9,5] ? 9

? Caso 2: [1] ? 1


Ejercicio 159
Título del Ejercicio: Encontrar Menor Elemento en Array
Análisis del Problema
? Descripción del Problema: Encontrar el elemento mínimo en un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Elemento mínimo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar min con el primer elemento.

2. Recorrer array comparando y actualizando min.

? Estructuras de Datos: Array.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={3,7,2,9,5}, n=5;
    int min=arr[0];
    for(int i=1;i<n;i++) if(arr[i]<min) min=arr[i];
    cout << "Menor elemento: " << min << endl; // 2
    return 0;
}

Pruebas
? Caso 1: [3,7,2,9,5] ? 2

? Caso 2: [10] ? 10


Ejercicio 160
Título del Ejercicio: Contar Elementos Mayores que X en Array
Análisis del Problema
? Descripción del Problema: Contar la cantidad de elementos en un array que sean mayores que un valor X.

? Entradas y Salidas:

? Entrada: Array de enteros y valor X.

? Salida: Cantidad de elementos mayores que X.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer array y sumar a contador si elemento > X.

? Estructuras de Datos: Array.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,5,7,3,9}, n=5, X=4, contador=0;
    for(int i=0;i<n;i++) if(arr[i]>X) contador++;
    cout << "Elementos mayores que " << X << ": " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,5,7,3,9], X=4 ? 3

? Caso 2: [1,2,3], X=5 ? 0
Ejercicio 161
Título del Ejercicio: Sumar Elementos Positivos de un Array
Análisis del Problema
? Descripción del Problema: Calcular la suma de todos los elementos positivos en un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Suma de los elementos positivos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer el array.

3. Si el elemento >0, sumarlo a la variable suma.

? Estructuras de Datos: Array.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={-1,2,3,-4,5}, n=5, suma=0;
    for(int i=0;i<n;i++){
        if(arr[i]>0) suma+=arr[i];
    }
    cout << "Suma de elementos positivos: " << suma << endl; // 10
    return 0;
}

Pruebas
? Caso 1: [-1,2,3,-4,5] ? 10

? Caso 2: [0,-2,-3] ? 0


Ejercicio 162
Título del Ejercicio: Sumar Elementos Negativos de un Array
Análisis del Problema
? Descripción del Problema: Calcular la suma de todos los elementos negativos en un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Suma de los elementos negativos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer el array.

3. Si el elemento <0, sumarlo a la variable suma.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={-1,2,3,-4,5}, n=5, suma=0;
    for(int i=0;i<n;i++){
        if(arr[i]<0) suma+=arr[i];
    }
    cout << "Suma de elementos negativos: " << suma << endl; // -5
    return 0;
}

Pruebas
? Caso 1: [-1,2,3,-4,5] ? -5

? Caso 2: [1,2,3] ? 0


Ejercicio 163
Título del Ejercicio: Calcular Promedio de Array
Análisis del Problema
? Descripción del Problema: Calcular el promedio de todos los elementos de un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Promedio de los elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer el array y acumular elementos.

3. Dividir suma entre tamaño del array.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={2,4,6,8}, n=4, suma=0;
    for(int i=0;i<n;i++) suma+=arr[i];
    double promedio = (double)suma/n;
    cout << "Promedio: " << promedio << endl; // 5
    return 0;
}

Pruebas
? Caso 1: [2,4,6,8] ? 5

? Caso 2: [1,1,1,1] ? 1


Ejercicio 164
Título del Ejercicio: Contar Ceros en Array
Análisis del Problema
? Descripción del Problema: Contar la cantidad de elementos iguales a 0 en un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Cantidad de ceros.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer el array.

3. Incrementar contador si el elemento es 0.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={0,2,0,3,0}, n=5, contador=0;
    for(int i=0;i<n;i++) if(arr[i]==0) contador++;
    cout << "Cantidad de ceros: " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [0,2,0,3,0] ? 3

? Caso 2: [1,2,3] ? 0


Ejercicio 165
Título del Ejercicio: Invertir Array
Análisis del Problema
? Descripción del Problema: Invertir el orden de los elementos de un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Array invertido.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar dos índices: inicio=0, fin=n-1.

2. Intercambiar elementos hasta que inicio>=fin.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    for(int i=0,j=n-1;i<j;i++,j--){
        int temp=arr[i]; arr[i]=arr[j]; arr[j]=temp;
    }
    for(int i=0;i<n;i++) cout << arr[i] << " "; // 5 4 3 2 1
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? [5,4,3,2,1]

? Caso 2: [1] ? [1]


Ejercicio 166
Título del Ejercicio: Buscar Elemento en Array
Análisis del Problema
? Descripción del Problema: Determinar si un elemento dado existe en un array.

? Entradas y Salidas:

? Entrada: Array y elemento a buscar.

? Salida: true si existe, false si no.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,3,5,7}, n=4, x=5;
    bool encontrado=false;
    for(int i=0;i<n;i++) if(arr[i]==x) encontrado=true;
    cout << (encontrado ? "Elemento encontrado\n" : "Elemento no encontrado\n"); // Encontrado
    return 0;
}

Pruebas
? Caso 1: x=5 ? encontrado

? Caso 2: x=2 ? no encontrado


Ejercicio 167
Título del Ejercicio: Contar Apariciones de un Elemento
Análisis del Problema
? Descripción del Problema: Contar cuántas veces aparece un elemento en un array.

? Entradas y Salidas:

? Entrada: Array y elemento a contar.

? Salida: Número de apariciones.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,2,3,2}, n=5, x=2, contador=0;
    for(int i=0;i<n;i++) if(arr[i]==x) contador++;
    cout << "El elemento " << x << " aparece " << contador << " veces.\n"; // 3
    return 0;
}

Pruebas
? Caso 1: x=2 ? 3 veces

? Caso 2: x=5 ? 0 veces


Ejercicio 168
Título del Ejercicio: Eliminar Elemento en Array (Reordenando)
Análisis del Problema
? Descripción del Problema: Eliminar un elemento específico de un array desplazando los elementos restantes.

? Entradas y Salidas:

? Entrada: Array y elemento a eliminar.

? Salida: Array modificado.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,2}, n=5, x=2;
    int nuevo_n=0;
    for(int i=0;i<n;i++){
        if(arr[i]!=x) arr[nuevo_n++]=arr[i];
    }
    for(int i=0;i<nuevo_n;i++) cout << arr[i] << " "; // 1 3 4
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: x=2 ? [1,3,4]

? Caso 2: x=5 ? [1,2,3,4,2]


Ejercicio 169
Título del Ejercicio: Sumar Elementos de Array Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular la suma de todos los elementos de un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Suma de elementos.

Código Fuente (C++)
#include <iostream>
using namespace std;

int sumaRec(int arr[], int n){
    if(n==0) return 0;
    return arr[n-1]+sumaRec(arr,n-1);
}

int main() {
    int arr[]={1,2,3,4}, n=4;
    cout << "Suma total: " << sumaRec(arr,n) << endl; // 10
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4] ? 10

? Caso 2: [0,0,0] ? 0


Ejercicio 170
Título del Ejercicio: Calcular Producto de Array Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular el producto de todos los elementos de un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Producto de elementos.

Código Fuente (C++)
#include <iostream>
using namespace std;

int productoRec(int arr[], int n){
    if(n==0) return 1;
    return arr[n-1]*productoRec(arr,n-1);
}

int main() {
    int arr[]={1,2,3,4}, n=4;
    cout << "Producto total: " << productoRec(arr,n) << endl; // 24
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4] ? 24

? Caso 2: [2,2,2] ? 8
Ejercicio 181
Título del Ejercicio: Buscar Elemento en Matriz
Análisis del Problema
? Descripción del Problema: Determinar si un elemento dado existe en una matriz.

? Entradas y Salidas:

? Entrada: Matriz m×n y elemento a buscar.

? Salida: Mensaje indicando si se encuentra o no el elemento.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer todas las filas y columnas de la matriz.

2. Comparar cada elemento con el valor buscado.

3. Si se encuentra, retornar true; si no, false.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][3]={{1,2,3},{4,5,6}};
    int m=2, n=3, x=5;
    bool encontrado=false;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(mat[i][j]==x) encontrado=true;
        }
    }
    cout << (encontrado ? "Elemento encontrado\n" : "Elemento no encontrado\n"); // Encontrado
    return 0;
}

Pruebas
? Caso 1: x=5 ? "Elemento encontrado"

? Caso 2: x=7 ? "Elemento no encontrado"


Ejercicio 182
Título del Ejercicio: Contar Apariciones de un Elemento en Matriz
Análisis del Problema
? Descripción del Problema: Contar cuántas veces aparece un elemento específico en una matriz.

? Entradas y Salidas:

? Entrada: Matriz m×n y elemento a contar.

? Salida: Número de apariciones del elemento.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer la matriz fila por fila y columna por columna.

3. Incrementar contador si el elemento coincide con el valor buscado.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][3]={{1,2,3},{2,2,6}}, m=2, n=3, x=2;
    int contador=0;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(mat[i][j]==x) contador++;
        }
    }
    cout << "El elemento " << x << " aparece " << contador << " veces.\n"; // 3
    return 0;
}

Pruebas
? Caso 1: x=2 ? 3 apariciones

? Caso 2: x=5 ? 0 apariciones
Ejercicio 183
Título del Ejercicio: Sumar Filas de Matriz Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de cada fila de una matriz usando recursión.

? Entradas y Salidas:

? Entrada: Matriz m×n.

? Salida: Suma de cada fila.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? int sumaFilaRec(int mat[][3], int fila, int col, int nCol){
?     if(col==nCol) return 0;
?     return mat[fila][col] + sumaFilaRec(mat,fila,col+1,nCol);
? }
? 
? int main() {
?     int mat[2][3]={{1,2,3},{4,5,6}};
?     for(int i=0;i<2;i++)
?         cout << "Suma fila " << i << ": " << sumaFilaRec(mat,i,0,3) << endl; // 6, 15
?     return 0;
? }

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? 6, 15

? Caso 2: [[0,0,0],[1,1,1]] ? 0, 3


Ejercicio 184
Título del Ejercicio: Sumar Columnas de Matriz Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de cada columna de una matriz usando recursión.

? Entradas y Salidas:

? Entrada: Matriz m×n.

? Salida: Suma de cada columna.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? int sumaColRec(int mat[][3], int fila, int col, int nFilas){
?     if(fila==nFilas) return 0;
?     return mat[fila][col] + sumaColRec(mat,fila+1,col,nFilas);
? }
? 
? int main() {
?     int mat[2][3]={{1,2,3},{4,5,6}};
?     for(int j=0;j<3;j++)
?         cout << "Suma columna " << j << ": " << sumaColRec(mat,0,j,2) << endl; // 5,7,9
?     return 0;
? }

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? 5,7,9


Ejercicio 185
Título del Ejercicio: Trasponer Matriz Recursivamente
Análisis del Problema
? Descripción del Problema: Trasponer una matriz (intercambiar filas por columnas) usando recursión.

? Entradas y Salidas:

? Entrada: Matriz m×n.

? Salida: Matriz traspuesta.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? void trasponerRec(int mat[][3], int trans[][2], int i, int j, int m, int n){
?     if(i==m) return;
?     if(j<n){
?         trans[j][i] = mat[i][j];
?         trasponerRec(mat, trans, i, j+1, m, n);
?     } else trasponerRec(mat, trans, i+1, 0, m, n);
? }
? 
? int main() {
?     int mat[2][3]={{1,2,3},{4,5,6}}, trans[3][2];
?     trasponerRec(mat, trans, 0, 0, 2, 3);
?     for(int i=0;i<3;i++){
?         for(int j=0;j<2;j++) cout << trans[i][j] << " ";
?         cout << endl;
?     }
?     return 0;
? }

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? [[1,4],[2,5],[3,6]]


Ejercicio 186
Título del Ejercicio: Verificar Matriz Simétrica
Análisis del Problema
? Descripción del Problema: Determinar si una matriz cuadrada es simétrica (igual a su traspuesta).

? Entradas y Salidas:

? Entrada: Matriz n×n.

? Salida: true si es simétrica, false si no.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? int main() {
?     int mat[3][3]={{1,2,3},{2,5,6},{3,6,9}}, n=3;
?     bool simetrica=true;
?     for(int i=0;i<n;i++)
?         for(int j=0;j<n;j++)
?             if(mat[i][j]!=mat[j][i]) simetrica=false;
?     cout << (simetrica ? "Simétrica" : "No simétrica") << endl; // Simétrica
?     return 0;
? }

Pruebas
? Caso 1: [[1,2,3],[2,5,6],[3,6,9]] ? Simétrica

? Caso 2: [[1,0],[2,1]] ? No simétrica


Ejercicio 187
Título del Ejercicio: Calcular Factorial Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular el factorial de un número usando recursión.

? Entradas y Salidas:

? Entrada: Número entero n?0.

? Salida: Factorial de n.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? int factorial(int n){
?     if(n==0) return 1;
?     return n*factorial(n-1);
? }
? 
? int main() {
?     int n=5;
?     cout << "Factorial de " << n << ": " << factorial(n) << endl; // 120
?     return 0;
? }

Pruebas
? Caso 1: n=5 ? 120

? Caso 2: n=0 ? 1


Ejercicio 188
Título del Ejercicio: Calcular Potencia Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular a^b usando recursión.

? Entradas y Salidas:

? Entrada: Base a y exponente b?0.

? Salida: Resultado de a^b.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? int potencia(int a, int b){
?     if(b==0) return 1;
?     return a*potencia(a,b-1);
? }
? 
? int main() {
?     int a=2,b=3;
?     cout << a << "^" << b << " = " << potencia(a,b) << endl; // 8
?     return 0;
? }

Pruebas
? Caso 1: 2^3 ? 8

? Caso 2: 5^0 ? 1


Ejercicio 189
Título del Ejercicio: Contar Vocales Recursivamente
Análisis del Problema
? Descripción del Problema: Contar la cantidad de vocales en una cadena usando recursión.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de vocales.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? int contarVocales(char *str){
?     if(*str=='\0') return 0;
?     char c = tolower(*str);
?     return ((c=='a'||c=='e'||c=='i'||c=='o'||c=='u')?1:0)+contarVocales(str+1);
? }
? 
? int main() {
?     char cadena[]="Hola Mundo";
?     cout << "Cantidad de vocales: " << contarVocales(cadena) << endl; // 4
?     return 0;
? }

Pruebas
? Caso 1: "Hola Mundo" ? 4

? Caso 2: "C++" ? 0


Ejercicio 190
Título del Ejercicio: Sumar Elementos de Pila
Análisis del Problema
? Descripción del Problema: Sumar todos los elementos de una pila implementada con array.

? Entradas y Salidas:

? Entrada: Pila de enteros.

? Salida: Suma de todos los elementos.

Código Fuente (C++)
? #include <iostream>
? using namespace std;
? 
? int main() {
?     int pila[5]={1,2,3,4,5}, n=5, suma=0;
?     for(int i=0;i<n;i++) suma+=pila[i];
?     cout << "Suma elementos de la pila: " << suma << endl; // 15
?     return 0;
? }

Pruebas
? Caso 1: [1,2,3,4,5] ? 15

? Caso 2: [0,0,0] ? 0
Ejercicio 191
Título del Ejercicio: Gestión de Estudiantes con POO
Análisis del Problema
? Descripción del Problema: Crear un sistema simple para almacenar información de estudiantes (nombre, edad, promedio). El programa debe permitir:

? Agregar estudiantes.

? Mostrar todos los estudiantes.

? Calcular promedio general.

? Entradas y Salidas:

? Entrada: Datos de cada estudiante (nombre, edad, promedio).

? Salida: Lista de estudiantes y promedio general.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase Estudiante con atributos: nombre, edad, promedio.

2. Crear métodos para mostrar información.

3. Guardar estudiantes en un array.

4. Recorrer array para calcular promedio general.

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Estudiante{
public:
    string nombre;
    int edad;
    float promedio;

    void mostrarInfo(){
        cout << "Nombre: " << nombre << ", Edad: " << edad << ", Promedio: " << promedio << endl;
    }
};

int main() {
    Estudiante estudiantes[3];
    float sumaProm=0;

    // Agregar información
    estudiantes[0] = {"Juan", 20, 8.5};
    estudiantes[1] = {"Ana", 22, 9.2};
    estudiantes[2] = {"Luis", 19, 7.8};

    cout << "Lista de estudiantes:\n";
    for(int i=0;i<3;i++){
        estudiantes[i].mostrarInfo();
        sumaProm += estudiantes[i].promedio;
    }

    cout << "Promedio general: " << sumaProm/3 << endl; // 8.5 aprox
    return 0;
}

Pruebas
? Caso 1: 3 estudiantes ? Mostrar lista y promedio general

? Caso 2: Cambiar edades/promedios ? Verificar cálculo correcto


Ejercicio 192
Título del Ejercicio: Gestión de Libros con POO y Arreglo Dinámico
Análisis del Problema
? Descripción del Problema: Crear un sistema de biblioteca que permita:

? Agregar libros (título, autor, año).

? Mostrar todos los libros.

? Buscar libros por autor.

? Entradas y Salidas:

? Entrada: Datos de libros.

? Salida: Lista completa y libros filtrados por autor.

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Libro{
public:
    string titulo, autor;
    int anio;
    void mostrar() { cout << titulo << " - " << autor << " (" << anio << ")\n"; }
};

int main(){
    int n = 3;
    Libro* biblioteca = new Libro[n];
    
    biblioteca[0] = {"C++ Moderno", "Bjarne", 2018};
    biblioteca[1] = {"Algoritmos", "Knuth", 1997};
    biblioteca[2] = {"Estructuras de Datos", "Weiss", 2013};

    cout << "Todos los libros:\n";
    for(int i=0;i<n;i++) biblioteca[i].mostrar();

    string autorBuscado = "Knuth";
    cout << "\nLibros de " << autorBuscado << ":\n";
    for(int i=0;i<n;i++)
        if(biblioteca[i].autor==autorBuscado) biblioteca[i].mostrar();

    delete[] biblioteca;
    return 0;
}

Pruebas
? Caso 1: Buscar autor existente ? Mostrar libro

? Caso 2: Autor inexistente ? Sin resultados


Ejercicio 193
Título del Ejercicio: Pila Dinámica con Funciones
Análisis del Problema
? Descripción del Problema: Implementar una pila con array dinámico que permita:

1. Insertar elementos (push)

2. Eliminar elementos (pop)

3. Mostrar la pila

4. Sumar todos los elementos

Código Fuente (C++)
#include <iostream>
using namespace std;

class Pila {
private:
    int* arr;
    int top;
    int capacidad;
public:
    Pila(int size){
        capacidad = size;
        arr = new int[size];
        top = -1;
    }

    void push(int x){
        if(top == capacidad-1) { cout << "Pila llena\n"; return; }
        arr[++top] = x;
    }

    int pop(){
        if(top == -1) { cout << "Pila vacía\n"; return -1; }
        return arr[top--];
    }

    void mostrar(){
        cout << "Pila: ";
        for(int i=0;i<=top;i++) cout << arr[i] << " ";
        cout << endl;
    }

    int sumar(){
        int suma=0;
        for(int i=0;i<=top;i++) suma+=arr[i];
        return suma;
    }

    ~Pila(){ delete[] arr; }
};

int main(){
    Pila pila(5);
    pila.push(1); pila.push(2); pila.push(3);
    pila.mostrar();
    cout << "Suma elementos: " << pila.sumar() << endl; // 6
    pila.pop();
    pila.mostrar(); // 1 2
    return 0;
}

Pruebas
? Caso 1: Push 3 elementos ? Mostrar y sumar

? Caso 2: Pop elemento ? Verificar pila y suma


Ejercicio 194
Título del Ejercicio: Cola Dinámica con Funciones
Análisis del Problema
? Descripción del Problema: Implementar una cola usando array dinámico:

1. Encolar (agregar)

2. Desencolar (eliminar)

3. Mostrar cola

4. Contar elementos

Código Fuente (C++)
#include <iostream>
using namespace std;

class Cola {
private:
    int* arr;
    int frente, fin, capacidad;
public:
    Cola(int size){
        capacidad = size;
        arr = new int[size];
        frente = 0; fin = -1;
    }

    void encolar(int x){
        if(fin == capacidad-1) { cout << "Cola llena\n"; return; }
        arr[++fin] = x;
    }

    int desencolar(){
        if(frente > fin) { cout << "Cola vacía\n"; return -1; }
        return arr[frente++];
    }

    void mostrar(){
        cout << "Cola: ";
        for(int i=frente;i<=fin;i++) cout << arr[i] << " ";
        cout << endl;
    }

    int contar(){ return fin-frente+1; }

    ~Cola(){ delete[] arr; }
};

int main(){
    Cola cola(5);
    cola.encolar(10); cola.encolar(20); cola.encolar(30);
    cola.mostrar();
    cout << "Cantidad elementos: " << cola.contar() << endl; // 3
    cola.desencolar();
    cola.mostrar(); // 20 30
    return 0;
}

Pruebas
? Caso 1: Agregar y eliminar ? Verificar contenido y conteo


Ejercicio 195
Título del Ejercicio: Recursión para Fibonacci
Análisis del Problema
? Descripción del Problema: Calcular n-ésimo número de Fibonacci usando recursión.

? Entradas y Salidas:

? Entrada: Número n?0

? Salida: Fibonacci(n)

Código Fuente (C++)
#include <iostream>
using namespace std;

int fibonacci(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    return fibonacci(n-1)+fibonacci(n-2);
}

int main(){
    int n=10;
    cout << "Fibonacci(" << n << ") = " << fibonacci(n) << endl; // 55
    return 0;
}

Pruebas
? Caso 1: n=10 ? 55

? Caso 2: n=0 ? 0


Ejercicio 196
Título del Ejercicio: Búsqueda Binaria Recursiva
Análisis del Problema
? Descripción del Problema: Implementar búsqueda binaria recursiva para un array ordenado.

? Entradas y Salidas:

? Entrada: Array ordenado, valor a buscar

? Salida: Índice del elemento o -1 si no existe

Código Fuente (C++)
#include <iostream>
using namespace std;

int busquedaBinaria(int arr[], int inicio, int fin, int x){
    if(inicio>fin) return -1;
    int mid = inicio + (fin-inicio)/2;
    if(arr[mid]==x) return mid;
    if(arr[mid]<x) return busquedaBinaria(arr,mid+1,fin,x);
    else return busquedaBinaria(arr,inicio,mid-1,x);
}

int main(){
    int arr[]={1,3,5,7,9,11}, n=6, x=7;
    int indice = busquedaBinaria(arr,0,n-1,x);
    cout << (indice!=-1 ? "Elemento encontrado en indice " + to_string(indice) : "Elemento no encontrado") << endl; // 3
    return 0;
}

Pruebas
? Caso 1: x=7 ? índice 3

? Caso 2: x=2 ? -1


Ejercicio 197
Título del Ejercicio: Ordenamiento Burbuja
Análisis del Problema
? Descripción del Problema: Ordenar un array de enteros usando burbuja y mostrar antes/después.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main(){
    int arr[]={5,3,8,1,2}, n=5;
    cout << "Antes: ";
    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl;

    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-1-i;j++)
            if(arr[j]>arr[j+1]) swap(arr[j],arr[j+1]);

    cout << "Después: ";
    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl;

    return 0;
}

Pruebas
? Caso 1: [5,3,8,1,2] ? [1,2,3,5,8]


Ejercicio 198
Título del Ejercicio: Ordenamiento por Inserción
Análisis del Problema:
? Descripción del Problema: Ordenar un array de enteros usando inserción.

Código Fuente (C++)
#include <iostream>
using namespace std;

int main(){
    int arr[]={9,5,1,4,3}, n=5;
    for(int i=1;i<n;i++){
        int key = arr[i];
        int j=i-1;
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;
    }
    for(int i=0;i<n;i++) cout << arr[i] << " "; // 1 3 4 5 9
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [9,5,1,4,3] ? [1,3,4,5,9]


Ejercicio 199
Título del Ejercicio: Calculadora de Operaciones
Análisis del Problema:
? Descripción del Problema: Implementar calculadora que realice suma, resta, multiplicación y división usando funciones.

Código Fuente (C++)
#include <iostream>
using namespace std;

float suma(float a,float b){return a+b;}
float resta(float a,float b){return a-b;}
float mult(float a,float b){return a*b;}
float divi(float a,float b){return b!=0?a/b:0;}

int main(){
    float x=10,y=5;
    cout << "Suma: " << suma(x,y) << endl;
    cout << "Resta: " << resta(x,y) << endl;
    cout << "Multiplicación: " << mult(x,y) << endl;
    cout << "División: " << divi(x,y) << endl;
    return 0;
}

Pruebas
? Caso 1: x=10,y=5 ? 15,5,50,2


Ejercicio 200
Título del Ejercicio: Sistema Completo de Banco con POO
Análisis del Problema:
? Descripción del Problema: Implementar clase CuentaBancaria que permita:

1. Depositar dinero

2. Retirar dinero

3. Consultar saldo

4. Mostrar información de la cuenta

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class CuentaBancaria{
private:
    string titular;
    float saldo;
public:
    CuentaBancaria(string n,float s){ titular=n; saldo=s; }
    void depositar(float monto){ saldo+=monto; }
    void retirar(float monto){ if(saldo>=monto) saldo-=monto; else cout<<"Saldo insuficiente\n"; }
    void mostrar(){ cout << "Titular: " << titular << ", Saldo: " << saldo << endl; }
    float getSaldo(){ return saldo; }
};

int main(){
    CuentaBancaria c("Juan",1000);
    c.mostrar();
    c.depositar(500);
    c.mostrar();
    c.retirar(2000); // Saldo insuficiente
    c.retirar(800);
    c.mostrar(); // Saldo 700
    return 0;
}

Pruebas
? Depositar, retirar y consultar saldo ? Verificar correctitud de operaciones