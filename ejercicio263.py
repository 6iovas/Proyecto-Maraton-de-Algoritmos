// Proyecto de Informatica
// Ejercicio 263
? Use MillerRabin from ejercicio 34.

? Pollard Rho with randomized polynomial f(x) = x^2 + c (mod n), use gcd and Floyd cycle detection (or Brent).

? Recursively factor.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using u64 = unsigned long long;
using u128 = unsigned __int128;

u64 modmul(u64 a,u64 b,u64 mod){ return (u64)((u128)a*b % mod); }
u64 modpow(u64 a,u64 d,u64 mod){ u64 r=1; while(d){ if(d&1) r=modmul(r,a,mod); a=modmul(a,a,mod); d>>=1;} return r; }
// Miller-Rabin (same as previous)...
bool isPrime(u64 n){
    if(n<2) return false;
    for(u64 p: {2,3,5,7,11,13,17,19,23,29,31,37}){ if(n%p==0) return n==p; }
    u64 d=n-1,s=0; while((d&1)==0){d>>=1;s++;}
    u64 bases[] = {2,325,9375,28178,450775,9780504,1795265022};
    for(u64 a: bases){
        if(a%n==0) continue;
        u64 x = modpow(a,d,n);
        if(x==1||x==n-1) continue;
        bool comp=true;
        for(u64 r=1;r<s;++r){ x=modmul(x,x,n); if(x==n-1){comp=false;break;} }
        if(comp) return false;
    }
    return true;
}

u64 pollards_rho(u64 n){
    if(n%2==0) return 2;
    if(n%3==0) return 3;
    u64 c = rand() % (n-1) + 1;
    u64 x = rand() % n, y = x;
    u64 d = 1;
    auto f = [&](u64 x){ return (modmul(x,x,n) + c) % n; };
    while(d==1){
        x = f(x); y = f(f(y));
        u64 diff = x>y? x-y : y-x;
        d = std::gcd(diff, n);
        if(d==n) return pollards_rho(n);
    }
    return d;
}

void factor(u64 n, vector<u64>& out){
    if(n==1) return;
    if(isPrime(n)){ out.push_back(n); return; }
    u64 d = pollards_rho(n);
    factor(d, out);
    factor(n/d, out);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    u64 n; while(cin>>n){
        vector<u64> fac; factor(n, fac);
        sort(fac.begin(), fac.end());
        for(u64 p: fac) cout<<p<<" ";
        cout<<"\n";
    }
    return 0;
}

Prueba
? Factor 1e12+39 etc. Works probabilistically; combine with MillerRabin.