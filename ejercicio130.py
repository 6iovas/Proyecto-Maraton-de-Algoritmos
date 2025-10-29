// Proyecto de Informatica
// Ejercicio 130
Ejercicio 128: K-d Tree básico (insert + nearest neighbor search skeleton)
Análisis del Problema
 Estructura para búsquedas k-NN en 2D (here: nearest neighbor).
Diseño de la Solución
 Recursive split by axis, track best distance.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
struct Pt { double x,y; };
struct KDNode {
    Pt p; KDNode *l=nullptr, *r=nullptr;
    KDNode(Pt pt): p(pt) {}
};

KDNode* build(vector<Pt>& pts, int l, int r, int depth){
    if(l>r) return nullptr;
    int axis = depth%2;
    int m = (l+r)/2;
    nth_element(pts.begin()+l, pts.begin()+m, pts.begin()+r+1, [&](const Pt &a,const Pt &b){
        return axis==0? a.x < b.x : a.y < b.y;
    });
    KDNode* node = new KDNode(pts[m]);
    node->l = build(pts, l, m-1, depth+1);
    node->r = build(pts, m+1, r, depth+1);
    return node;
}

double dist2(const Pt&a,const Pt&b){ double dx=a.x-b.x, dy=a.y-b.y; return dx*dx+dy*dy; }

void nn_search(KDNode* node, const Pt& target, int depth, Pt& best, double& bestd){
    if(!node) return;
    double d = dist2(node->p, target);
    if(d < bestd){ bestd = d; best = node->p; }
    int axis = depth%2;
    double diff = (axis==0 ? target.x - node->p.x : target.y - node->p.y);
    KDNode *first = diff < 0 ? node->l : node->r;
    KDNode *second = diff < 0 ? node->r : node->l;
    nn_search(first, target, depth+1, best, bestd);
    if(diff*diff < bestd) nn_search(second, target, depth+1, best, bestd);
}

int main(){
    vector<Pt> pts = {{0,0},{1,2},{3,1},{-1,-2},{2,2}};
    KDNode* root = build(pts, 0, pts.size()-1, 0);
    Pt target{1.1, 1.9}, best{0,0}; double bestd = 1e100;
    nn_search(root, target, 0, best, bestd);
    cout << "Nearest: " << best.x << "," << best.y << "\n";
    return 0;
}

Pruebas
? Target near (1,2) should find (1,2) or nearby.