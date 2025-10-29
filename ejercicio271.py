// Proyecto de Informatica
// Ejercicio 271
Ejercicio 41  Minimum Cost Maximum Flow for required flow F (Dijkstra + potentials), with path reconstruction
Análisis
 Variación de MCMF: dado s,t y flujo objetivo F, encontrar mínimo coste para enviar exactamente F unidades (o informar si no posible). Necesario en problemas que piden flujo fijo. Usar Dijkstra con potentials para hallar caminos de coste mínimo repetidamente, y reconstruir las rutas/augmentaciones.
Diseño