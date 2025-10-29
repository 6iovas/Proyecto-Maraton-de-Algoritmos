// Proyecto de Informatica
// Ejercicio 145
Ejercicio 143: Ordenar lista enlazada simple
Análisis del Problema
 Ordenar lista enlazada implementando Merge Sort.
Diseño de la Solución
 Dividir lista en mitades y fusionarlas recursivamente.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct Node{int val;Node*next;Node(int v):val(v),next(nullptr){}};

Node* mergeList(Node*a,Node*b){
    if(!a) return b; if(!b) return a;
    if(a->val<b->val){a->next=mergeList(a->next,b);return a;}
    else {b->next=mergeList(a,b->next);return b;}
}

Node* mergeSort(Node*head){
    if(!head||!head->next)return head;
    Node*slow=head;Node*fast=head->next;
    while(fast&&fast->next){slow=slow->next;fast=fast->next->next;}
    Node*mid=slow->next;slow->next=nullptr;
    Node*l=mergeSort(head),*r=mergeSort(mid);
    return mergeList(l,r);
}

int main(){
    Node*a=new Node(3);a->