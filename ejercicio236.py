// Proyecto de Informatica
// Ejercicio 236
Ejercicio 29  FFT (Fast Fourier Transform) iterative CooleyTukey  convolution of integer sequences
Análisis del problema
 Implementar FFT iterative (bit-reversal + layers) para convolución de two integer sequences (polynomial multiplication). Debe manejar rounding and casting to long long. Complexity O(n log n).
Diseño de la solución
? Implement iterative FFT for complex numbers using std::complex<double>.

? Pad to power of two, do forward FFT, pointwise multiply, inverse FFT, round real parts.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    // bit reversal
    for (int i=1, j=0; i<n; ++i) {
        int bit = n>>1;
        for (; j & bit; bit >>=1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    for (int len=2; len<=n; len <<=1) {
        double ang = 2*PI/len * (invert ? -1 : 1);
        cd wlen = cd(cos(ang), sin(ang));
        for (int i=0; i<n; i += len) {
            cd w(1);
            for (int j=0; j<len/2; ++j) {
                cd u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }
    if (invert) {
        for (cd & x : a) x /= n;
    }
}

vector<long long> convolution(const vector<long long>& a, const vector<long long>& b) {
    int n = 1;
    while (n < (int)(a.size() + b.size() - 1)) n <<= 1;
    vector<cd> fa(n);
    for (size_t i=0;i<a.size();++i) fa[i] = cd(a[i],0);
    for (size_t i=0;i<b.size();++i) fa[i].imag(b[i]);
    // pack trick: compute two FFTs in one by using complex embedding
    fft(fa, false);
    vector<cd> fb(n);
    for (int i=0;i<n;++i) {
        cd x = fa[i];
        cd y = conj(fa[(n - i) % n]);
        cd A = (x + y) * cd(0.5, 0);
        cd B = (x - y) * cd(0, -0.5);
        fb[i] = A * B;
    }
    fft(fb, true);
    vector<long long> res(a.size() + b.size() - 1);
    for (size_t i=0;i<res.size();++i) res[i] = (long long) llround(fb[i].real());
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<long long> a(n), b(m);
    for(int i=0;i<n;++i) cin>>a[i];
    for(int j=0;j<m;++j) cin>>b[j];
    auto c = convolution(a,b);
    for(size_t i=0;i<c.size();++i) cout<<c[i]<<(i+1==c.size()?'\n':' ');
    return 0;
}

Pruebas
? a=[1,2,3], b=[4,5] ? convolution = [4,13,22,15] (polynomial multiplication).

? Works for large sequences; watch numerical precision for very large integer coefficients (use FFT mod techniques for safe integer convolution if needed).