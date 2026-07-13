//
resolução achar o caminho menor usando dijkstra 

ShortestPath_Dijkstra(G,start)
    para cada u em V[G]
        intree[u] = false
        distance[u] = INT_MAX
        parent[u] = -1
    distance[start] = 0
    v = start
    enquanto(intree[v]==false)
        intree[v] = true
        para cada p em adj[v]
            destino = p->v
            weight = p->peso
            se distance[destino]>distance[v]+weight
                distance[destino] = distance[v]+weight
                parent[destino] = v
        v = 0
        dist = INT_MAX
        para cada u em V[G]
            se(intree[u]==false && dist>distance[u])
                dist = distance[u]
                v=u

para grafos direcionados e ponderados 
vai ter 3 vetores 
distancia 
parent 
visitado 
				
				
				
				
				
				
				
				
O objetivo é calcular o menor caminho a partir do vértice 1 para todos os outros vértices, seguindo o algoritmo de Dijkstra. O gráfico fornecido tem 6 vértices e várias arestas com pesos, conforme indicado pelas setas no diagrama.

2. Inicialização
No algoritmo de Dijkstra:

Iniciamos o vetor distance com 8 (ou INT_MAX) para todos os vértices, exceto o vértice de origem (neste caso, o vértice 1), que será inicializado com 0.
Criamos também um vetor intree que indica se o vértice já foi visitado ou não (todos começam como false).
Começamos o cálculo a partir do vértice 1.
3. Adjacências e pesos
O grafo fornecido tem as seguintes arestas com pesos:

1 ? 2 com peso 1
1 ? 4 com peso 4
2 ? 3 com peso 5
2 ? 5 com peso 1
3 ? 6 com peso 3
4 ? 5 com peso 3
5 ? 3 com peso 1
5 ? 6 com peso 4
4. Execução do algoritmo de Dijkstra
Vamos começar a partir do vértice 1 e atualizar as distâncias para seus vizinhos.

Iteração 1 (vértice 1):
Distâncias iniciais: [0, 8, 8, 8, 8, 8]
Atualizamos as distâncias para os vértices adjacentes ao 1:
1 ? 2: distance[2] = 0 + 1 = 1
1 ? 4: distance[4] = 0 + 4 = 4
Distâncias agora: [0, 1, 8, 4, 8, 8]
Iteração 2 (vértice 2):
Menor distância disponível é do vértice 2 com distance[2] = 1.
Atualizamos as distâncias para os vizinhos de 2:
2 ? 3: distance[3] = 1 + 5 = 6
2 ? 5: distance[5] = 1 + 1 = 2
Distâncias agora: [0, 1, 6, 4, 2, 8]
Iteração 3 (vértice 5):
Menor distância agora é do vértice 5 com distance[5] = 2.
Atualizamos as distâncias para os vizinhos de 5:
5 ? 3: distance[3] = min(6, 2 + 1) = 3
5 ? 6: distance[6] = 2 + 4 = 6
Distâncias agora: [0, 1, 3, 4, 2, 6]
Iteração 4 (vértice 4):
Menor distância agora é do vértice 4 com distance[4] = 4.
Atualizamos as distâncias para os vizinhos de 4:
4 ? 5: distance[5] = min(2, 4 + 3) = 2 (não muda)
Distâncias agora: [0, 1, 3, 4, 2, 6]
Iteração 5 (vértice 3):
Menor distância agora é do vértice 3 com distance[3] = 3.
Atualizamos as distâncias para os vizinhos de 3:
3 ? 6: distance[6] = min(6, 3 + 3) = 6 (não muda)
Distâncias agora: [0, 1, 3, 4, 2, 6]
Iteração 6 (vértice 6):
O vértice 6 já está com sua menor distância final: distance[6] = 6






//