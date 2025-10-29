// Proyecto de Informatica
// Ejercicio 269
Ejercicio 40  Suffix Automaton: count occurrences of every substring (endpos sizes)
Análisis
 Extender el Suffix Automaton (SAM) para, además de contar substrings distintos, calcular cuántas veces aparece cada substring en el texto (el número de endpos por estado). Usamos el atributo cnt[state] = número de end positions (ocurrencias) para ese estado; después de construir SAM, propagamos cnt por orden decreciente de len (topo / counting sort by length). Luego número de ocurrencias de cualquier substring represented by state v es cnt[v]. El número de distintas ocurrencias totales se puede obtener o usar para responder queries.
Diseño
? En extensión extend(c), set `cnt[cur] =