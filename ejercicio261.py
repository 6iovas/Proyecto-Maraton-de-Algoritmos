// Proyecto de Informatica
// Ejercicio 261
Ejercicio 34  Randomized algorithms: MillerRabin primality test (64-bit safe bases)
Análisis
 Implementar MillerRabin deterministic set of bases to test 64-bit integers for primality. Fast and reliable for competitive programming.
Diseño
? Use modular multiplication avoiding overflow (128-bit).

? Use known good bases for 64-bit (e.g., {2,3,5,7,11,13} or canonical set {2,3,5,7,11,13,17}).

? Implement powmod and witness routine.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using u128 = unsigned __int128;
using u64 = unsigned long long;

u64 modmul(u64 a, u64 b, u64 mod){
    return (u64)((u128)a * b % mod);
}
u64 modpow(u64 a, u64 d, u64 mod){
    u64 res=1;
    while(d){
        if(d&1) res = modmul(res,a,mod);
        a = modmul(a,a,mod);
        d >>= 1;
    }
    return res;
}
bool isPrime(u64 n){
    if(n<2) return false;
    for(u64 p: {2,3,5,7,11,13,17,19,23,29,31,37}){
        if(n%p==0) return n==p;
    }
    u64 d = n-1, s=0;
    while((d&1)==0){ d>>=1; ++s; }
    // bases for 64-bit deterministic
    u64 bases[] = {2,325,9375,28178,450775,9780504,1795265022};
    for(u64 a: bases){
        if(a%n==0) continue;
        u64 x = modpow(a, d, n);
        if(x==1 || x==n-1) continue;
        bool comp = true;
        for(u64 r=1;r<s;++r){
            x = modmul(x, x, n);
            if(x==n-1){ comp=false; break; }
        }
        if(comp) return false;
    }
    return true;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    unsigned long long x;
    while(cin>>x) cout << x << (isPrime(x) ? " is prime\n" : " is composite\n");
    return 0;
}

Prueba
? Test primes and composites: 2,3,4,17,1e9+7, large Carmichael numbers.