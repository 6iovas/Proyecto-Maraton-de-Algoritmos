// Proyecto de Informatica
// Ejercicio 247
Ejercicio 28  Gaussian Elimination (solve linear system Ax = b) con pivoteo parcial y detección de soluciones (única / infinitas / ninguna)
Análisis del problema
 Resolver sistema lineal A x = b de n ecuaciones y n incógnitas (o rectangular) usando eliminación Gaussiana con pivot parcial. Detectar si existe solución única, infinitas soluciones (free variables), o ninguna. Proveer una solución cuando existe (one possible for infinite case).
Diseño de la solución
? Transformar la matriz aumentada [A|b] a su forma escalonada reducida (row-echelon) con pivot parcial (swap de fila con mayor pivote absoluto).

? Después de forward elimination, back-substitution.

? Para rank < n detect free variables  to provide one solution, set free vars = 0 and solve for others.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ld = double;
const ld EPS = 1e-9;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; // we will read n rows and m columns (unknowns = m)
    if(!(cin>>n>>m)) return 0;
    vector<vector<ld>> a(n, vector<ld>(m+1));
    for(int i=0;i<n;++i) for(int j=0;j<=m;++j) cin>>a[i][j];
    int row = 0;
    vector<int> where(m, -1);
    for(int col=0; col<m && row<n; ++col){
        int sel = row;
        for(int i=row;i<n;++i) if(fabs(a[i][col]) > fabs(a[sel][col])) sel = i;
        if(fabs(a[sel][col]) < EPS) continue;
        swap(a[sel], a[row]);
        where[col] = row;
        ld pivot = a[row][col];
        for(int j=col;j<=m;++j) a[row][j] /= pivot;
        for(int i=0;i<n;++i) if(i!=row){
            ld factor = a[i][col];
            for(int j=col;j<=m;++j) a[i][j] -= factor * a[row][j];
        }
        ++row;
    }
    // check consistency
    vector<ld> ans(m, 0);
    for(int i=0;i<m;++i) if(where[i]!=-1) ans[i] = a[where[i]][m];
    for(int i=0;i<n;++i){
        ld sum = 0;
        for(int j=0;j<m;++j) sum += ans[j] * a[i][j];
        if(fabs(sum - a[i][m]) > 1e-6){ cout<<"NO SOLUTION\n"; return 0; }
    }
    bool infinite = false;
    for(int i=0;i<m;++i) if(where[i]==-1) infinite = true;
    if(infinite) cout<<"INFINITE SOLUTIONS (one possible solution shown)\n";
    else cout<<"UNIQUE SOLUTION\n";
    cout.setf(std::ios::fixed); cout<<setprecision(9);
    for(int i=0;i<m;++i) cout<<ans[i]<<(i+1==m?'\n':' ');
    return 0;
}

Pruebas
Unique:

 n=2 m=2
1 1 2
1 -1 0
?  Solution: x=1 y=1.

? No solution: inconsistent row.

? Infinite: two equations identical with 3 unknowns.