// Proyecto de Informatica
// Ejercicio 270
Ejercicio 40  Suffix Automaton: contar ocurrencias de cada substring (endpos size)
Análisis
 Construir un Suffix Automaton (SAM) para una string s. Además de contar substrings distintos, queremos saber cuántas veces aparece cada substring en s. Esto se obtiene contando el número de posiciones finales (endpos) asociados a cada estado: inicialmente cada extensión crea un estado con cnt=1 (representa la nueva aparición), luego se propaga la cuenta sumando cnt de estados hacia sus link en orden decreciente de len.
Diseño
? Construir SAM con next, link, len.

? Mantener cnt[state] = 1 para estados correspondientes a finales durante la construcción.

? Después de construir, agrupar estados por len y procesarlos de mayor a menor: cnt[link[v]] += cnt[v].

? Para obtener cuántas veces aparece una cadena t, se recorre t por las transiciones a partir de estado 0; si se falla, ocurrencias = 0; si llega a estado v, ocurrencias = cnt[v].

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct SAM {
    struct State {
        int next[26];
        int link;
        int len;
        long long cnt;
        State(){ fill(begin(next), end(next), -1); link=-1; len=0; cnt=0; }
    };
    vector<State> st;
    int last;
    SAM(){ st.reserve(200005); st.push_back(State()); last=0; }
    void extend(char ch){
        int c = ch - 'a';
        int cur = st.size(); st.push_back(State());
        st[cur].len = st[last].len + 1;
        st[cur].cnt = 1; // each extension corresponds to one endpos
        int p = last;
        while(p!=-1 && st[p].next[c]==-1){ st[p].next[c]=cur; p=st[p].link; }
        if(p==-1){ st[cur].link = 0; }
        else {
            int q = st[p].next[c];
            if(st[p].len + 1 == st[q].len) st[cur].link = q;
            else {
                int clone = st.size(); st.push_back(st[q]);
                st[clone].len = st[p].len + 1;
                st[clone].cnt = 0; // clone doesn't add endpos directly
                while(p!=-1 && st[p].next[c]==q){ st[p].next[c]=clone; p=st[p].link; }
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }
    void build(const string &s){ for(char c: s) extend(c); }
    void compute_occurrences(){
        int sz = st.size();
        int maxlen = 0;
        for(auto &s: st) maxlen = max(maxlen, s.len);
        vector<int> cntLen(maxlen+1, 0);
        for(auto &s: st) cntLen[s.len]++;
        for(int i=1;i<=maxlen;++i) cntLen[i]+=cntLen[i-1];
        vector<int> order(sz);
        for(int i=sz-1;i>=0;--i) order[--cntLen[st[i].len]] = i;
        for(int i=sz-1;i>0;--i){ // from longer to shorter
            int v = order[i];
            if(st[v].link!=-1) st[st[v].link].cnt += st[v].cnt;
        }
    }
    long long occurrences_of(const string &t){
        int v = 0;
        for(char ch: t){
            int c = ch - 'a';
            if(st[v].next[c]==-1) return 0;
            v = st[v].next[c];
        }
        return st[v].cnt;
    }
    long long distinct_substrings(){
        long long res = 0;
        for(size_t i=1;i<st.size();++i) res += (st[i].len - st[st[i].link].len);
        return res;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; if(!(cin>>s)) return 0;
    SAM sam; sam.build(s); sam.compute_occurrences();
    cout << "Distinct substrings: " << sam.distinct_substrings() << "\n";
    // Example queries: read q and q patterns, print occurrences
    int q; cin >> q;
    while(q--){
        string t; cin >> t;
        cout << sam.occurrences_of(t) << "\n";
    }
    return 0;
}

Pruebas
? s = "ababa". Distinct substrings = 9. Queries: "a" -> 3, "aba" -> 2, "ababa" -> 1, "b" -> 2.