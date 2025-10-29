// Proyecto de Informatica
// Ejercicio 173
Ejercicio 169: LRU Cache (list + unordered_map)
Análisis
 Implementar cache LRU con capacidad k: O(1) get/put.
Diseño
 Doble-linked list (std::list) + unordered_map key->iterator.
Código
#include <bits/stdc++.h>
using namespace std;
struct LRU {
    int cap; list<pair<int,int>> l; unordered_map<int, list<pair<int,int>>::iterator> mp;
    LRU(int c):cap(c){}
    int get(int k){
        if(!mp.count(k)) return -1;
        auto it=mp[k]; int val=it->second; l.erase(it); l.push_front({k,val}); mp[k]=l.begin(); return val;
    }
    void put(int k,int v){
        if(mp.count(k)){ l.erase(mp[k]); mp.erase(k); }
        if((int)l.size()==cap){ auto bk=l.back(); mp.erase(bk.first); l.pop_back(); }
        l.push_front({k,v}); mp[k]=l.begin();
    }
};
int main(){
    LRU cache(2);
    cache.put(1,1); cache.put(2,2);
    cout<<cache.get(1)<<"\n"; // 1
    cache.put(3,3);
    cout<<cache.get(2)<<"\n"; // -1
}

Prueba
? Comportamiento según ejemplo (outputs 1 then -1).