// Proyecto de Informatica
// Ejercicio 102
Título del Ejercicio: Eliminar Condicional
Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n,X; cin>>n>>X;
    vector<int> v(n);
    for(int i=0;i<n;i++) cin>>v[i];

    v.erase(remove_if(v.begin(),v.end(),[X](int a){ return a<X; }), v.end());

    cout<<"Vector después de eliminar elementos menores que "<<X<<": ";
    for(int x:v) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: [1 5 3 7], X=4 ? Salida: 5 7
 
1.- Enunciado: Leer dos enteros e imprimir su suma.

Leer dos enteros e imprimir su suma.

2.- sumas de números enteros 
int main() {
    int a, b;
    cout << "Ingresa dos enteros: ";
    cin >> a >> b;
    cout << "Suma: " << (a + b) << endl;
    return 0;
}


3.-Resta de dos números
Enunciado: Leer dos enteros e imprimir su diferencia (a - b).

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Ingresa a y b: ";
    cin >> a >> b;
    cout << "Diferencia a-b: " << (a - b) << endl;
    return 0;
}


4.-Multiplicación de dos números
Enunciado: Leer dos enteros y mostrar el producto.

#include <iostream>
using namespace std;

int main() {
    int x, y;
    cout << "Ingresa dos enteros: ";
    cin >> x >> y;
    cout << "Producto: " << (x * y) << endl;
    return 0;
}


5.-División entera
Enunciado: Leer dos enteros y mostrar división entera (si b ? 0).

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Ingresa a y b (b != 0): ";
    cin >> a >> b;
    if (b == 0) cout << "Error: division por cero\n";
    else cout << "a/b = " << (a / b) << " (división entera)\n";
    return 0;
}


6.-Promedio de tres números
Enunciado: Leer tres números (pueden ser reales) y calcular su promedio.

Promedio de tres números



7.-Número par o impar
Enunciado: Leer un entero y decir si es par o impar.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa un entero: ";
    cin >> n;
    if (n % 2 == 0) cout << n << " es par\n";
    else cout << n << " es impar\n";
    return 0;
}


8.-Valor absoluto
Enunciado: Leer un número entero y mostrar su valor absoluto.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa un entero: ";
    cin >> n;
    if (n < 0) n = -n;
    cout << "Valor absoluto: " << n << endl;
    return 0;
}


9.-Mayor de dos números
Enunciado: Leer dos números y mostrar el mayor.

#include <iostream>
using namespace std;

int main() {
    double a, b;
    cout << "Ingresa dos números: ";
    cin >> a >> b;
    if (a > b) cout << "Mayor: " << a << endl;
    else cout << "Mayor: " << b << endl;
    return 0;
}


10.-Ordenar dos números
Enunciado: Leer dos números y mostrarlos en orden ascendente.

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Ingresa dos enteros: ";
    cin >> a >> b;
    if (a <= b) cout << a << " " << b << endl;
    else cout << b << " " << a << endl;
    return 0;
}


11.-Intercambio (swap)
Enunciado: Leer dos variables y mostrarlas intercambiadas.

#include <iostream>
using namespace std;

int main() {
    int a, b, temp;
    cout << "Ingresa a y b: ";
    cin >> a >> b;
    temp = a;
    a = b;
    b = temp;
    cout << "Tras swap: a=" << a << " b=" << b << endl;
    return 0;
}


12.-Suma de los primeros N naturales
Enunciado: Leer N y calcular la suma 1+2+...+N usando un for.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Ingresa N: ";
    cin >> N;
    int suma = 0;
    for (int i = 1; i <= N; ++i) suma += i;
    cout << "Suma: " << suma << endl;
    return 0;
}


13.-Factorial (iterativo)
Enunciado: Leer N (N >= 0) y calcular N! de forma iterativa.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Ingresa N (>=0): ";
    cin >> N;
    long long fact = 1;
    for (int i = 2; i <= N; ++i) fact *= i;
    cout << N << "! = " << fact << endl;
    return 0;
}


14.-Contar dígitos
Enunciado: Leer un entero positivo y contar cuántos dígitos tiene.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa un entero positivo: ";
    cin >> n;
    if (n == 0) { cout << "Dígitos: 1\n"; return 0; }
    int cnt = 0;
    while (n != 0) { n /= 10; ++cnt; }
    cout << "Dígitos: " << cnt << endl;
    return 0;
}


15.-Suma de dígitos
Enunciado: Leer un entero positivo y mostrar la suma de sus dígitos.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa un entero positivo: ";
    cin >> n;
    int suma = 0;
    while (n != 0) {
        suma += n % 10;
        n /= 10;
    }
    cout << "Suma de dígitos: " << suma << endl;
    return 0;
}


16.-Invertir número
Enunciado: Leer un entero y mostrar su reverso (ej. 123 -> 321).

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa un entero: ";
    cin >> n;
    int sign = (n < 0) ? -1 : 1;
    if (n < 0) n = -n;
    int rev = 0;
    while (n != 0) {
        rev = rev * 10 + (n % 10);
        n /= 10;
    }
    cout << "Invertido: " << (sign * rev) << endl;
    return 0;
}


17.-Número primo (chequeo simple)
Enunciado: Leer N y verificar si es primo (algoritmo simple).

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa N: ";
    cin >> n;
    if (n <= 1) { cout << "No primo\n"; return 0; }
    bool primo = true;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) { primo = false; break; }
    }
    cout << (primo ? "Primo\n" : "No primo\n");
    return 0;
}


18.-Listar primos hasta N
Enunciado: Leer N y listar los números primos ? N (método simple).

#include <iostream>
using namespace std;

bool esPrimo(int x) {
    if (x <= 1) return false;
    for (int i = 2; i * i <= x; ++i)
        if (x % i == 0) return false;
    return true;
}

int main() {
    int N;
    cout << "Ingresa N: ";
    cin >> N;
    for (int i = 2; i <= N; ++i)
        if (esPrimo(i)) cout << i << " ";
    cout << endl;
    return 0;
}


19.-Máximo entre tres números
Enunciado: Leer tres números y mostrar el mayor.

#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    cout << "Ingresa 3 números: ";
    cin >> a >> b >> c;
    double m = a;
    if (b > m) m = b;
    if (c > m) m = c;
    cout << "Mayor: " << m << endl;
    return 0;
}


20.-Mínimo entre tres números
Enunciado: Leer tres números y mostrar el menor.

#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    cout << "Ingresa 3 números: ";
    cin >> a >> b >> c;
    double m = a;
    if (b < m) m = b;
    if (c < m) m = c;
    cout << "Menor: " << m << endl;
    return 0;
}


21.-Tabla de multiplicar
Enunciado: Leer N y mostrar la tabla de multiplicar del 1 al 10 de N.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Ingresa N: ";
    cin >> N;
    for (int i = 1; i <= 10; ++i)
        cout << N << " x " << i << " = " << (N * i) << endl;
    return 0;
}


22.-Suma pares hasta N
Enunciado: Leer N y calcular la suma de todos los números pares ? N.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Ingresa N: ";
    cin >> N;
    int suma = 0;
    for (int i = 2; i <= N; i += 2) suma += i;
    cout << "Suma pares: " << suma << endl;
    return 0;
}


23.-Contar pares e impares
Enunciado: Leer N números (pedir cuántos) y contar cuántos son pares y cuántos impares.

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "¿Cuántos números?: ";
    cin >> n;
    int pares = 0, impares = 0, x;
    for (int i = 0; i < n; ++i) {
        cin >> x;
        if (x % 2 == 0) ++pares;
        else ++impares;
    }
    cout << "Pares: " << pares << " Impares: " << impares << endl;
    return 0;
}


24.- MCD (algoritmo de Euclides)
Enunciado: Leer dos enteros y calcular su máximo común divisor (MCD).

#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Ingresa a y b: ";
    cin >> a >> b;
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    cout << "MCD: " << (a < 0 ? -a : a) << endl;
    return 0;
}


25.-MCM (mínimo común múltiplo)
Enunciado: Leer dos enteros y calcular su MCM usando MCD.

#include <iostream>
using namespace std;

int mcd(int a, int b) {
    a = (a < 0) ? -a : a;
    b = (b < 0) ? -b : b;
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    int a, b;
    cout << "Ingresa a y b: ";
    cin >> a >> b;
    if (a == 0 || b == 0) { cout << "MCM indefinido (0)\n"; return 0; }
    long long l = (long long) (a / mcd(a,b)) * b;
    if (l < 0) l = -l;
    cout << "MCM: " << l << endl;
    return 0;
}


26.-Tabla de N×M
Enunciado: Mostrar una tabla de multiplicar de tamaño N filas por M columnas (valores 1..N y 1..M).

#include <iostream>
using namespace std;

int main() {
    int N, M;
    cout << "Ingresa N y M: ";
    cin >> N >> M;
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= M; ++j)
            cout << (i * j) << "\t";
        cout << endl;
    }
    return 0;
}


27.-Número perfecto
Enunciado: Leer N y verificar si es número perfecto (la suma de sus divisores propios = N).

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa N: ";
    cin >> n;
    int suma = 0;
    for (int i = 1; i <= n/2; ++i) if (n % i == 0) suma += i;
    if (suma == n) cout << n << " es perfecto\n";
    else cout << n << " no es perfecto\n";
    return 0;
}


28.-Fibonacci (n-ésimo, iterativo)
Enunciado: Leer N y mostrar el N-ésimo número de Fibonacci (0,1,1,2,...).

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Ingresa N (>=0): ";
    cin >> N;
    if (N == 0) { cout << "0\n"; return 0; }
    long long a = 0, b = 1;
    for (int i = 2; i <= N; ++i) {
        long long c = a + b;
        a = b;
        b = c;
    }
    cout << (N==1 ? 1 : b) << endl;
    return 0;
}


29.-Sumar matrices 2x2
Enunciado: Leer dos matrices 2×2 y mostrar su suma (elemento a elemento).

#include <iostream>
using namespace std;

int main() {
    int A[2][2], B[2][2];
    cout << "Ingresa 4 elementos de A (2x2): ";
    for (int i=0;i<2;i++) for (int j=0;j<2;j++) cin >> A[i][j];
    cout << "Ingresa 4 elementos de B (2x2): ";
    for (int i=0;i<2;i++) for (int j=0;j<2;j++) cin >> B[i][j];
    cout << "Suma A+B:\n";
    for (int i=0;i<2;i++) {
        for (int j=0;j<2;j++) cout << (A[i][j]+B[i][j]) << "\t";
        cout << endl;
    }
    return 0;
}


30.-Contar vocales en una palabra
Enunciado: Leer una palabra (sin espacios) y contar cuántas vocales tiene (a,e,i,o,u).

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Ingresa una palabra: ";
    cin >> s;
    int cnt = 0;
    for (char c : s) {
        char ch = tolower(c);
        if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') ++cnt;
    }
    cout << "Vocales: " << cnt << endl;
    return 0;
}


31.-Contar caracteres de una cadena
Enunciado: Leer una línea (usa getline) y mostrar su longitud.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string linea;
    cout << "Ingresa una línea: ";
    getline(cin, linea);
    cout << "Longitud: " << linea.length() << endl;
    return 0;
}


32.-Buscar carácter en cadena
Enunciado: Leer una cadena y un carácter; decir si el carácter aparece y cuántas veces.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    char c;
    cout << "Ingresa cadena: ";
    getline(cin, s);
    cout << "Ingresa un carácter: ";
    cin >> c;
    int cnt = 0;
    for (char ch : s) if (ch == c) ++cnt;
    cout << "Aparece " << cnt << " veces\n";
    return 0;
}


33.-Reemplazar carácter en cadena
Enunciado: Leer una cadena y reemplazar todas las ocurrencias de a por b (caracteres indicados por el usuario).

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    char a, b;
    cout << "Ingresa cadena: ";
    getline(cin, s);
    cout << "Reemplazar qué caracter? ";
    cin >> a;
    cout << "Por qué caracter? ";
    cin >> b;
    for (int i=0;i<(int)s.size();++i) if (s[i]==a) s[i]=b;
    cout << "Resultado: " << s << endl;
    return 0;
}


34.-Eliminar espacios en una cadena
Enunciado: Leer una línea y mostrarla sin espacios.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Ingresa línea: ";
    getline(cin, s);
    string out;
    for (char c : s) if (c != ' ') out.push_back(c);
    cout << "Sin espacios: " << out << endl;
    return 0;
}


35.-Palíndromo (cadena)
Enunciado: Leer una cadena (sin espacios) y verificar si es palíndromo.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Ingresa cadena: ";
    cin >> s;
    bool pal = true;
    for (int i=0, j=s.size()-1; i<j; ++i, --j) if (s[i]!=s[j]) { pal=false; break; }
    cout << (pal ? "Es palíndromo\n" : "No es palíndromo\n");
    return 0;
}


36.-Número de palabras en una línea
Enunciado: Leer una línea y contar cuántas palabras (separadas por espacios).

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string linea;
    cout << "Ingresa una línea: ";
    getline(cin, linea);
    istringstream iss(linea);
    string word;
    int cnt = 0;
    while (iss >> word) ++cnt;
    cout << "Palabras: " << cnt << endl;
    return 0;
}


37.-Buscar mayor en arreglo
Enunciado: Leer N y luego N enteros; mostrar el mayor y su posición (primera).

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Cuántos elementos?: ";
    cin >> N;
    int maxVal, pos=0, x;
    if (N <= 0) { cout << "N inválido\n"; return 0; }
    for (int i=1;i<=N;++i){
        cin >> x;
        if (i==1 || x > maxVal) { maxVal = x; pos = i; }
    }
    cout << "Mayor: " << maxVal << " en posición " << pos << endl;
    return 0;
}


38.-Buscar menor en arreglo
Enunciado: Leer N y N números; mostrar el menor y su posición.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Cuántos elementos?: ";
    cin >> N;
    int minVal, pos=0, x;
    if (N <= 0) { cout << "N inválido\n"; return 0; }
    for (int i=1;i<=N;++i){
        cin >> x;
        if (i==1 || x < minVal) { minVal = x; pos = i; }
    }
    cout << "Menor: " << minVal << " en posición " << pos << endl;
    return 0;
}


39.-Promedio de un arreglo
Enunciado: Leer N y N números; mostrar su promedio.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Cuántos?: ";
    cin >> N;
    double suma = 0, x;
    for (int i=0;i<N;++i){ cin >> x; suma += x; }
    cout << "Promedio: " << (N>0 ? suma / N : 0) << endl;
    return 0;
}


40.-Invertir arreglo
Enunciado: Leer N y N números; mostrarlos en orden inverso.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "N: ";
    cin >> N;
    int a[1000];
    for (int i=0;i<N;++i) cin >> a[i];
    for (int i=N-1;i>=0;--i) cout << a[i] << " ";
    cout << endl;
    return 0;
}


41.-Suma de dos vectores
Enunciado: Leer N y dos vectores de longitud N; mostrar vector suma.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "N: ";
    cin >> N;
    int A[1000], B[1000];
    for (int i=0;i<N;++i) cin >> A[i];
    for (int i=0;i<N;++i) cin >> B[i];
    for (int i=0;i<N;++i) cout << (A[i]+B[i]) << " ";
    cout << endl;
    return 0;
}


42.-Eliminar duplicados en arreglo (mostrar únicos)
Enunciado: Leer N y N enteros; imprimir los elementos únicos en orden de aparición.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "N: ";
    cin >> N;
    int a[1000];
    for (int i=0;i<N;++i) cin >> a[i];
    for (int i=0;i<N;++i) {
        bool seen = false;
        for (int j=0;j<i;++j) if (a[j]==a[i]) { seen = true; break; }
        if (!seen) cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}


43.-Suma condicional (positivos)
Enunciado: Leer N números y sumar solo los positivos.

#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "N: ";
    cin >> N;
    int suma = 0, x;
    for (int i=0;i<N;++i){ cin >> x; if (x > 0) suma += x; }
    cout << "Suma positivos: " << suma << endl;
    return 0;
}


44.-Cuenta vocales y consonantes
Enunciado: Leer una palabra y contar cuántas vocales y consonantes tiene (solo letras).

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Palabra: ";
    cin >> s;
    int v=0, c=0;
    for (char ch : s) {
        char l = tolower(ch);
        if (l>='a' && l<='z') {
            if (l=='a'||l=='e'||l=='i'||l=='o'||l=='u') ++v;
            else ++c;
        }
    }
    cout << "Vocales: " << v << " Consonantes: " << c << endl;
    return 0;
}


45.-Número Armstrong (número narcisista)
Enunciado: Leer un entero de 3 dígitos y verificar si es Armstrong (ej.: 153 = 1^3+5^3+3^3).

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Ingresa un entero (3 dígitos): ";
    cin >> n;
    int original = n, suma = 0;
    while (n) {
        int d = n % 10;
        suma += d*d*d;
        n /= 10;
    }
    cout << (suma == original ? "Es Armstrong\n" : "No es Armstrong\n");
    return 0;
}


46.-Contar números positivos, negativos y ceros
Enunciado: Leer N y N números; contar cuántos son positivos, negativos y ceros.

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    int pos=0, neg=0, cero=0, x;
    for (int i=0;i<N;++i) {
        cin >> x;
        if (x>0) ++pos;
        else if (x<0) ++neg;
        else ++cero;
    }
    cout << "Pos: " << pos << " Neg: " << neg << " Ceros: " << cero << endl;
    return 0;
}


47.-Suma de diagonales de matriz cuadrada
Enunciado: Leer una matriz NxN y mostrar la suma de la diagonal principal.

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    int a[100][100];
    for (int i=0;i<N;++i) for (int j=0;j<N;++j) cin >> a[i][j];
    int suma = 0;
    for (int i=0;i<N;++i) suma += a[i][i];
    cout << "Suma diagonal principal: " << suma << endl;
    return 0;
}


48.-Suma diagonal secundaria
Enunciado: Leer una matriz NxN y mostrar la suma de la diagonal secundaria.

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    int a[100][100];
    for (int i=0;i<N;++i) for (int j=0;j<N;++j) cin >> a[i][j];
    int suma = 0;
    for (int i=0;i<N;++i) suma += a[i][N-1-i];
    cout << "Suma diagonal secundaria: " << suma << endl;
    return 0;
}


49.-Matriz identidad
Enunciado: Dado N, imprimir la matriz identidad NxN (1s en diagonal principal).

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    for (int i=0;i<N;++i) {
        for (int j=0;j<N;++j) cout << (i==j ? 1 : 0) << " ";
        cout << endl;
    }
    return 0;
}


50.-Sumar filas de matriz
Enunciado: Leer NxM y mostrar la suma de cada fila.

#include <iostream>
using namespace std;

int main() {
    int N, M; cout << "N M: "; cin >> N >> M;
    int x;
    for (int i=0;i<N;++i) {
        int suma=0;
        for (int j=0;j<M;++j){ cin >> x; suma += x; }
        cout << "Suma fila " << i+1 << ": " << suma << endl;
    }
    return 0;
}


51.-Producto punto de dos vectores
Enunciado: Leer N y dos vectores de tamaño N; calcular su producto punto.

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    int a[1000], b[1000];
    for (int i=0;i<N;++i) cin >> a[i];
    for (int i=0;i<N;++i) cin >> b[i];
    long long prod = 0;
    for (int i=0;i<N;++i) prod += (long long)a[i]*b[i];
    cout << "Producto punto: " << prod << endl;
    return 0;
}


52.-Número perfecto menor que N (listar)
Enunciado: Leer N y listar todos los números perfectos <= N.

#include <iostream>
using namespace std;

bool esPerfecto(int n) {
    int suma = 0;
    for (int i=1;i<=n/2;++i) if (n%i==0) suma += i;
    return suma == n;
}

int main() {
    int N; cout << "N: "; cin >> N;
    for (int i=1;i<=N;++i) if (esPerfecto(i)) cout << i << " ";
    cout << endl;
    return 0;
}


53.-Suma alternada 1-2+3-4+...
Enunciado: Leer N y calcular 1 - 2 + 3 - 4 + ... ± N.

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    int suma = 0;
    for (int i=1;i<=N;++i) suma += (i % 2 == 1 ? i : -i);
    cout << "Resultado: " << suma << endl;
    return 0;
}


54.-Suma de cuadrados hasta N
Enunciado: Leer N y calcular 1^2 + 2^2 + ... + N^2.

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    long long suma = 0;
    for (int i=1;i<=N;++i) suma += (long long)i*i;
    cout << "Suma cuadrados: " << suma << endl;
    return 0;
}


55.-Contar vocales y consonantes en frase
Enunciado: Leer una línea y contar vocales y consonantes (ignorar otros).

#include <iostream>
#include <string>
using namespace std;

int main() {
    string linea;
    cout << "Ingresa línea: ";
    getline(cin, linea);
    int v=0, c=0;
    for (char ch : linea) {
        char l = tolower(ch);
        if (l>='a' && l<='z') {
            if (l=='a'||l=='e'||l=='i'||l=='o'||l=='u') ++v;
            else ++c;
        }
    }
    cout << "Vocales: " << v << " Consonantes: " << c << endl;
    return 0;
}


56.-Calcular área de un círculo
Enunciado: Leer radio y mostrar el área (? = 3.14159).

#include <iostream>
using namespace std;

int main() {
    double r;
    cout << "Radio: ";
    cin >> r;
    const double PI = 3.14159;
    cout << "Área: " << PI * r * r << endl;
    return 0;
}


57.-Área y perímetro de rectángulo
Enunciado: Leer base y altura y mostrar área y perímetro.

#include <iostream>
using namespace std;

int main() {
    double b, h;
    cout << "Base y altura: ";
    cin >> b >> h;
    cout << "Área: " << (b*h) << " Perímetro: " << (2*(b+h)) << endl;
    return 0;
}


58.-Conversión Celsius a Fahrenheit
Enunciado: Leer temperatura en °C y convertir a °F.

#include <iostream>
using namespace std;

int main() {
    double c;
    cout << "Celsius: ";
    cin >> c;
    double f = c * 9.0/5.0 + 32.0;
    cout << "Fahrenheit: " << f << endl;
    return 0;
}


59.-Conversión Fahrenheit a Celsius
Enunciado: Leer °F y convertir a °C.

#include <iostream>
using namespace std;

int main() {
    double f;
    cout << "Fahrenheit: ";
    cin >> f;
    double c = (f - 32.0) * 5.0/9.0;
    cout << "Celsius: " << c << endl;
    return 0;
}


60.-Interés simple
Enunciado: Calcular interés simple: A = P(1 + r*t). Leer P, r (en decimal) y t.

#include <iostream>
using namespace std;

int main() {
    double P, r, t;
    cout << "P r t: ";
    cin >> P >> r >> t;
    double A = P * (1 + r * t);
    cout << "Monto: " << A << endl;
    return 0;
}


61.-Interés compuesto (anual)
Enunciado: A = P*(1 + r)^t. Leer P, r, t (años).

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double P, r, t;
    cout << "P r t: ";
    cin >> P >> r >> t;
    double A = P * pow(1 + r, t);
    cout << "Monto compuesto: " << A << endl;
    return 0;
}


62.-Convertir número a romano (1..10)
Enunciado: Leer N entre 1 y 10 y mostrar su representación en números romanos.

#include <iostream>
using namespace std;

int main() {
    int n; cout << "N (1-10): "; cin >> n;
    string rom[] = {"","I","II","III","IV","V","VI","VII","VIII","IX","X"};
    if (n>=1 && n<=10) cout << rom[n] << endl;
    else cout << "Fuera de rango\n";
    return 0;
}


63.-Verificar año bisiesto
Enunciado: Leer un año y decir si es bisiesto.

#include <iostream>
using namespace std;

int main() {
    int y; cout << "Año: "; cin >> y;
    bool bis = (y%4==0 && y%100!=0) || (y%400==0);
    cout << (bis ? "Bisiesto\n" : "No bisiesto\n");
    return 0;
}


64.-Suma de números impares hasta N
Enunciado: Leer N y sumar los impares ? N.

#include <iostream>
using namespace std;

int main() {
    int N; cout << "N: "; cin >> N;
    int suma = 0;
    for (int i=1;i<=N;i+=2) suma += i;
    cout << "Suma impares: " << suma << endl;
    return 0;
}


65.-Serie aritmética
Enunciado: Dado a1 (primer término), d (razón) y N, imprimir los N primeros términos.

#include <iostream>
using namespace std;

int main() {
    int a1, d, N;
    cout << "a1 d N: "; cin >> a1 >> d >> N;
    int term = a1;
    for (int i=0;i<N;++i) {
        cout << term << " ";
        term += d;
    }
    cout << endl;
    return 0;
}


66.-Serie geométrica
Enunciado: Dado a1 (primer término), r (razón) y N, imprimir los N primeros términos.

#include <iostream>
using namespace std;

int main() {
    double a1, r;
    int N;
    cout << "a1 r N: "; cin >> a1 >> r >> N;
    double term = a1;
    for (int i=0;i<N;++i) {
        cout << term << " ";
        term *= r;
    }
    cout << endl;
    return 0;
}


67.-Suma de elementos en matriz
Enunciado: Leer NxM y sumar todos los elementos.

#include <iostream>
using namespace std;

int main() {
    int N,M; cin >> N >> M;
    int x, suma=0;
    for (int i=0;i<N;++i) for (int j=0;j<M;++j){ cin>>x; suma+=x; }
    cout << "Suma total: " << suma << endl;
    return 0;
}


68.-contar negativos en matCriz
Enunciado: Leer NxM y contar cuántos elementos son negativos.

#include <iostream>
using namespace std;

int main() {
    int N,M; cin >> N >> M;
    int x, cnt=0;
    for (int i=0;i<N;++i) for (int j=0;j<M;++j){ cin>>x; if (x<0) ++cnt; }
    cout << "Negativos: " << cnt << endl;
    return 0;
}


69.-Suma de dígitos pares
Enunciado: Leer un entero y sumar solo los dígitos pares.

#include <iostream>
using namespace std;

int main() {
    int n; cout << "Número: "; cin >> n;
    n = (n<0)? -n : n;
    int suma=0;
    while (n){ int d=n%10; if (d%2==0) suma+=d; n/=10; }
    cout << "Suma dígitos pares: " << suma << endl;
    return 0;
}


70.-Mayor y menor de arreglo
Enunciado: Leer N y N números; mostrar mayor y menor.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int x, maxv, minv;
    for (int i=0;i<N;++i) {
        cin >> x;
        if (i==0){ maxv=minv=x; }
        else { if (x>maxv) maxv=x; if (x<minv) minv=x; }
    }
    cout << "Mayor: " << maxv << " Menor: " << minv << endl;
    return 0;
}


* 71.-Ordenar 3 números (ascendente)*
Enunciado: Leer a,b,c y mostrarlos ordenados ascendentemente.

#include <iostream>
using namespace std;

int main() {
    int a,b,c; cin >> a >> b >> c;
    if (a>b) swap(a,b);
    if (a>c) swap(a,c);
    if (b>c) swap(b,c);
    cout << a << " " << b << " " << c << endl;
    return 0;
}


72.-Sumar impares en arreglo
Enunciado: Leer N y N enteros; sumar solo los impares.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int suma=0, x;
    for (int i=0;i<N;++i){ cin>>x; if (x%2!=0) suma+=x; }
    cout << "Suma impares: " << suma << endl;
    return 0;
}


73.-Edad en años, meses, días
Enunciado: Leer días totales (entero) y convertir a años (365), meses (30) y días restantes.

#include <iostream>
using namespace std;

int main() {
    int dias; cin >> dias;
    int años = dias / 365;
    dias %= 365;
    int meses = dias / 30;
    dias %= 30;
    cout << años << " años, " << meses << " meses, " << dias << " días\n";
    return 0;
}


74.-Sistema de calificaciones (A-F)
Enunciado: Leer nota 0-100 y mostrar letra: A(90-100), B(80-89), C(70-79), D(60-69), F(<60).

#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    if (n>=90) cout << "A\n";
    else if (n>=80) cout << "B\n";
    else if (n>=70) cout << "C\n";
    else if (n>=60) cout << "D\n";
    else cout << "F\n";
    return 0;
}


75.-Contar números primos en arreglo
Enunciado: Leer N y N enteros; contar cuántos son primos.

#include <iostream>
using namespace std;

bool esPrimo(int n){
    if (n<=1) return false;
    for (int i=2;i*i<=n;++i) if (n%i==0) return false;
    return true;
}

int main() {
    int N; cin >> N;
    int cnt=0, x;
    for (int i=0;i<N;++i){ cin>>x; if (esPrimo(x)) ++cnt; }
    cout << "Primos: " << cnt << endl;
    return 0;
}


76.-Buscar subcadena (posición primera aparición)
Enunciado: Leer una línea y una subcadena; mostrar la posición (1-based) de la primera aparición o 0 si no está.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, sub;
    cout << "Cadena: "; getline(cin, s);
    cout << "Subcadena: "; getline(cin, sub);
    size_t pos = s.find(sub);
    cout << (pos == string::npos ? 0 : (int)pos+1) << endl;
    return 0;
}


77.-Convertir minutos a horas y minutos
Enunciado: Leer minutos totales y mostrar en formato H horas y M minutos.

#include <iostream>
using namespace std;

int main() {
    int mins; cin >> mins;
    int h = mins / 60;
    int m = mins % 60;
    cout << h << " horas " << m << " minutos\n";
    return 0;
}


78.-Ordenar arreglo (burbuja básica)
Enunciado: Leer N y N enteros; ordenarlos ascendentemente usando el algoritmo burbuja.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int a[1000];
    for (int i=0;i<N;++i) cin >> a[i];
    for (int i=0;i<N-1;++i)
        for (int j=0;j<N-1-i;++j)
            if (a[j] > a[j+1]) swap(a[j], a[j+1]);
    for (int i=0;i<N;++i) cout << a[i] << " ";
    cout << endl;
    return 0;
}


79.-Eliminar elemento en arreglo (posición)
Enunciado: Leer N y un arreglo; luego leer posición p (1-based) y eliminar el elemento en p, mostrando el arreglo resultante.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int a[1000];
    for (int i=0;i<N;++i) cin >> a[i];
    int p; cin >> p; // 1-based
    if (p<1 || p> N) { cout << "Posición inválida\n"; return 0; }
    for (int i=p-1;i<N-1;++i) a[i] = a[i+1];
    for (int i=0;i<N-1;++i) cout << a[i] << " ";
    cout << endl;
    return 0;
}


80.-Insertar elemento en arreglo (posición)
Enunciado: Leer N y arreglo; luego leer valor v y posición p; insertar v en p (1-based).

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int a[1000];
    for (int i=0;i<N;++i) cin >> a[i];
    int v, p; cin >> v >> p;
    if (p<1 || p> N+1) { cout << "Pos inválida\n"; return 0; }
    for (int i=N;i>=p;--i) a[i] = a[i-1];
    a[p-1] = v;
    for (int i=0;i<N+1;++i) cout << a[i] << " ";
    cout << endl;
    return 0;
}


81.-Contar ocurrencias en arreglo
Enunciado: Leer N y arreglo; luego leer valor v y contar cuántas veces aparece.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int a[1000], v, cnt=0;
    for (int i=0;i<N;++i) cin >> a[i];
    cin >> v;
    for (int i=0;i<N;++i) if (a[i]==v) ++cnt;
    cout << "Ocurrencias: " << cnt << endl;
    return 0;
}


82.-Suma de dos números grandes (como cadenas)
Enunciado: Leer dos números muy grandes como cadenas y mostrar su suma (sin usar bibliotecas grandes).

#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    string res = "";
    int i = a.size()-1, j = b.size()-1, carry=0;
    while (i>=0 || j>=0 || carry) {
        int da = (i>=0 ? a[i--]-'0' : 0);
        int db = (j>=0 ? b[j--]-'0' : 0);
        int s = da + db + carry;
        res.push_back(char('0' + (s%10)));
        carry = s/10;
    }
    reverse(res.begin(), res.end());
    cout << res << endl;
    return 0;
}


83.-Convertir entero a binario
Enunciado: Leer un entero no negativo y mostrar su representación binaria.

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n; cin >> n;
    if (n==0) { cout << "0\n"; return 0; }
    string b="";
    while (n>0) { b.push_back('0' + (n%2)); n/=2; }
    reverse(b.begin(), b.end());
    cout << b << endl;
    return 0;
}


84.-Sumar números en una línea separados por espacios
Enunciado: Leer una línea con números separados por espacios y mostrar su suma.

#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string linea; getline(cin, linea);
    istringstream iss(linea);
    int x, suma=0;
    while (iss >> x) suma += x;
    cout << "Suma: " << suma << endl;
    return 0;
}


85.-Comparar dos cadenas (lexicográfico)
Enunciado: Leer dos palabras y decir cuál es lexicográficamente menor, o si son iguales.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b; cin >> a >> b;
    if (a == b) cout << "Iguales\n";
    else if (a < b) cout << a << " < " << b << endl;
    else cout << a << " > " << b << endl;
    return 0;
}


86.-Saber si N es cuadrado perfecto
Enunciado: Leer N y decir si es cuadrado perfecto.

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n; cin >> n;
    int r = (int) sqrt(n);
    cout << (r*r == n ? "Cuadrado perfecto\n" : "No es cuadrado perfecto\n");
    return 0;
}


87.-Suma de matrices (general NxM)
Enunciado: Leer NxM y luego otra NxM; mostrar su suma.

#include <iostream>
using namespace std;

int main() {
    int N,M; cin >> N >> M;
    int A[100][100], B[100][100];
    for (int i=0;i<N;++i) for (int j=0;j<M;++j) cin>>A[i][j];
    for (int i=0;i<N;++i) for (int j=0;j<M;++j) cin>>B[i][j];
    for (int i=0;i<N;++i){
        for (int j=0;j<M;++j) cout << (A[i][j]+B[i][j]) << " ";
        cout << endl;
    }
    return 0;
}


88.-Producto de matrices 2x2
Enunciado: Leer dos matrices 2x2 y mostrar su producto.

#include <iostream>
using namespace std;

int main() {
    int A[2][2], B[2][2], C[2][2] = {0};
    for (int i=0;i<2;++i) for (int j=0;j<2;++j) cin >> A[i][j];
    for (int i=0;i<2;++i) for (int j=0;j<2;++j) cin >> B[i][j];
    for (int i=0;i<2;++i)
        for (int j=0;j<2;++j) {
            C[i][j]=0;
            for (int k=0;k<2;++k) C[i][j]+= A[i][k]*B[k][j];
        }
    for (int i=0;i<2;++i){ for (int j=0;j<2;++j) cout << C[i][j] << " "; cout << endl; }
    return 0;
}


89.-Número invertido y comprobar palíndromo numérico
Enunciado: Leer un número y decir si es palíndromo numérico (ej. 121).

#include <iostream>
using namespace std;

int main() {
    int n; cin >> n;
    int orig = n, rev = 0;
    while (n) { rev = rev*10 + n%10; n /= 10; }
    cout << (rev == orig ? "Palíndromo\n" : "No palíndromo\n");
    return 0;
}


90.-Sumar números pares en posición par de arreglo
Enunciado: Leer N y arreglo; sumar números que están en posiciones pares (2,4,...) considerando 1-based.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int x, suma=0;
    for (int i=1;i<=N;++i) { cin>>x; if (i%2==0) suma+=x; }
    cout << "Suma posiciones pares: " << suma << endl;
    return 0;
}


90.-Promedio de notas descartando la menor
Enunciado: Leer N notas y calcular el promedio descartando la nota más baja.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    double suma=0, x;
    double minv=1e9;
    for (int i=0;i<N;++i){ cin>>x; suma+=x; if (x<minv) minv=x; }
    if (N<=1) cout << "No es posible\n";
    else cout << "Promedio: " << ( (suma - minv) / (N-1) ) << endl;
    return 0;
}

*91.-Contar números mayores al promedio
Enunciado: Leer N y N números; mostrar cuántos están por encima del promedio.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    double a[1000], suma=0;
    for (int i=0;i<N;++i){ cin>>a[i]; suma+=a[i]; }
    double prom = suma / N;
    int cnt=0;
    for (int i=0;i<N;++i) if (a[i] > prom) ++cnt;
    cout << "Mayores al promedio: " << cnt << endl;
    return 0;
}


92.-Suma de dígitos recursiva (digital root)
Enunciado: Leer un número y aplicar suma de dígitos repetida hasta obtener un solo dígito.

#include <iostream>
using namespace std;

int main() {
    long long n; cin >> n;
    n = (n<0)? -n : n;
    while (n >= 10) {
        long long s = 0;
        while (n) { s += n%10; n/=10; }
        n = s;
    }
    cout << n << endl;
    return 0;
}


93.-Comprobar si arreglo está ordenado (asc)
Enunciado: Leer N y arreglo; decir si está ordenado ascendentemente.

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    int prev, cur;
    if (N<=0) { cout << "Sí (vacío)\n"; return 0; }
    cin >> prev;
    bool ok = true;
    for (int i=1;i<N;++i) { cin>>cur; if (cur < prev) ok = false; prev = cur; }
    cout << (ok ? "Ordenado\n" : "No ordenado\n");
    return 0;
}


94.-Contar cifras pares en arreglo
Enunciado: Leer N y N enteros; contar cuántos tienen un número par de dígitos.

#include <iostream>
using namespace std;

int digitos(int n){ if (n==0) return 1; int c=0; n = (n<0)? -n : n; while(n){ n/=10; ++c; } return c; }

int main() {
    int N; cin >> N;
    int cnt=0, x;
    for (int i=0;i<N;++i){ cin>>x; if (digitos(x)%2==0) ++cnt; }
    cout << "Con dígitos pares: " << cnt << endl;
    return 0;
}


95.-Imprimir patrón de asteriscos (triángulo)
Enunciado: Leer N y mostrar un triángulo de * de altura N (alineado a la izquierda).

#include <iostream>
using namespace std;

int main() {
    int N; cin >> N;
    for (int i=1;i<=N;++i) {
        for (int j=0;j<i;++j) cout << "*";
        cout << endl;
    }
    return 0;
}


96.-Sumar matrices 3x3 (constantes)
Enunciado: Leer dos matrices 3x3 y mostrar su suma.

#include <iostream>
using namespace std;

int main() {
    int A[3][3], B[3][3];
    for (int i=0;i<3;++i) for (int j=0;j<3;++j) cin>>A[i][j];
    for (int i=0;i<3;++i) for (int j=0;j<3;++j) cin>>B[i][j];
    for (int i=0;i<3;++i){ for (int j=0;j<3;++j) cout << (A[i][j]+B[i][j]) << " "; cout << endl;}
    return 0;
}


97.-Calcular hipotenusa
Enunciado: Leer catetos a y b y calcular la hipotenusa (?(a²+b²)).

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a,b; cin >> a >> b;
    cout << "Hipotenusa: " << sqrt(a*a + b*b) << endl;
    return 0;
}


98.-Área de triángulo (base y altura)
Enunciado: Leer base y altura y calcular área = (base*altura)/2.

#include <iostream>
using namespace std;

int main() {
    double b,h; cin >> b >> h;
    cout << "Área: " << (b*h/2.0) << endl;
    return 0;
}


99.-Conversión decimal a hexadecimal (0..255)
Enunciado: Leer entero 0-255 y mostrar en hexadecimal (usando std::hex con iostream).

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n; cin >> n;
    if (n<0 || n>255) { cout << "Fuera de rango\n"; return 0; }
    cout << hex << uppercase << n << endl;
    return 0;
}


100.-Comparar longitudes de dos cadenas
Enunciado: Leer dos líneas y decir cuál es más larga (o si son iguales).

#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cout << "Linea A: "; getline(cin, a);
    cout << "Linea B: "; getline(cin, b);
    if (a.size() == b.size()) cout << "Iguales\n";
    else if (a.size() > b.size()) cout << "A es más larga\n";
    else cout << "B es más larga\n";
    return 0;
}