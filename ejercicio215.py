// Proyecto de Informatica
// Ejercicio 215
Ejercicio 10  Suffix Automaton básico: construir y contar substrings distintos
Análisis del problema
 Construir Suffix Automaton (SAM) para una string s y contar el número de substrings distintos en O(n). SAM size O(n*2). También mostrar cómo contar ocurrencias si se extiende.
Diseño de la solución
? Implementar construcción iterativa del SAM (last pointer, cloning states).

? Una propiedad: número de distintos substrings = sum over states of (len[state] - len[link[state]]).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct State {
    int len, link;
    array<int,26> next;
    State():len(0),link(-1){ next.fill(-1); }
};
struct SuffixAutomaton {
    vector<State> st;
    int last;
    SuffixAutomaton(){ st.reserve(2e5); st.push_back(State()); last=0; }
    void extend(char ch){
        int c = ch - 'a';
        int cur = st.size(); st.push_back(State()); st[cur].len = st[last].len + 1;
        int p = last;
        for(; p!=-1 && st[p].next[c]==-1; p = st[p].link) st[p].next[c] = cur;
        if(p==-1){ st[cur].link = 0; }
        else {
            int q = st[p].next[c];
            if(st[p].len + 1 == st[q].len) { st[cur].link = q; }
            else {
                int clone = st.size(); st.push_back(st[q]);
                st[clone].len = st[p].len + 1;
                // update links
                for(; p!=-1 && st[p].next[c]==q; p = st[p].link) st[p].next[c] = clone;
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }
    long long countDistinctSubstrings(){
        long long res = 0;
        for(size_t i=1;i<st.size();++i) res += (st[i].len - st[st[i].link].len);
        return res;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; if(!(cin>>s)) return 0;
    SuffixAutomaton sam;
    for(char c: s) sam.extend(c);
    cout << "Distinct substrings: " << sam.countDistinctSubstrings() << "\n";
    return 0;
}

Pruebas
? s = "ababa" ? substrings distinctos = 9 (verify: a, b, ab, ba, aba, bab, abab, baba, ababa).