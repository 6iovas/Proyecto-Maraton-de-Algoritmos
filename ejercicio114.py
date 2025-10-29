// Proyecto de Informatica
// Ejercicio 114
Ejercicio 112: Leer archivos en un directorio usando std::filesystem y contar líneas
Análisis del Problema
 Recorrer un directorio y contar el número total de líneas de archivos .txt.
Diseño de la Solución
 Usar std::filesystem::directory_iterator para listar archivos; para cada .txt, abrir y contar líneas.
Código Fuente (C++)
#include <bits/stdc++.h>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string path; // ejemplo: "."
    if(!(cin >> path)) return 0;
    long long total_lines = 0;
    for (auto &entry : fs::directory_iterator(path)) {
        if (!entry.is_regular_file()) continue;
        auto p = entry.path();
        if (p.extension() == ".txt") {
            ifstream in(p);
            string line;
            while (getline(in, line)) ++total_lines;
        }
    }
    cout << "Total lines in .txt files: " << total_lines << '\n';
    return 0;
}

Pruebas
? Ejecutar con ruta donde hay .txt para obtener suma de líneas.