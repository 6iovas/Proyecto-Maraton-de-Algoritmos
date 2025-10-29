// Proyecto de Informatica
// Ejercicio 249
Ejercicio 30  Minimum Vertex Cover in Bipartite Graph via Konigs theorem (matching ? min vertex cover)
Análisis del problema
 En grafos bipartitos, tamaño de minimum vertex cover = size of maximum matching (K?nig). Además se puede constructively find the vertex cover from a maximum matching: run BFS/DFS from unmatched left nodes alternating unmatched/matched edges; then cover = (Left \ reachable) ? (Right ? reachable). Complexity: O(E) after matching.
Diseño de la solución