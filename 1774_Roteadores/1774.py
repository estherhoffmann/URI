import sys 
  
class Graph():
  def __init__(self, vertices):
    self.vertices = vertices
    self.matriz_adjacencias = []
    for row in range(0,vertices):
      self.matriz_adjacencias.append([0] * vertices)

  def chave_min(self, chave, vertices_mst):
    minima = sys.maxsize
    for each_v in range(self.vertices):
      if minima > chave[each_v] and vertices_mst[each_v] is False:
        minima = chave[each_v]
        indice_min = each_v 
    return indice_min 
  
  def print_custo(self, anterior):
    custo_mst = 0
    for each_v in range(1, self.vertices):
      custo_mst = custo_mst + self.matriz_adjacencias[each_v][anterior[each_v]]
    print(custo_mst)

  def prim_mst(self):
    chave = [sys.maxsize] * self.vertices
    anterior = [None] * self.vertices
    chave[0] = 0
    vertices_mst = [False] * self.vertices
    
    anterior[0] = -1
    for saida in range(self.vertices):
      vertice_escolhido = self.chave_min(chave, vertices_mst)
      vertices_mst[vertice_escolhido] = True
      for each_v in range(self.vertices):
        if self.matriz_adjacencias[vertice_escolhido][each_v]>0 and vertices_mst[each_v]==False and chave[each_v]>self.matriz_adjacencias[vertice_escolhido][each_v]:
          chave[each_v] = self.matriz_adjacencias[vertice_escolhido][each_v]
          anterior[each_v] = vertice_escolhido
    self.print_custo(anterior) 

quantidade = input().split()
qnt_rot = int(quantidade[0])
qnt_cabos = int(quantidade[1])
g = Graph(qnt_rot)

for i in range(0, qnt_cabos):
  rot_custos = input().split()
  rot1 = int(rot_custos[0])
  rot2 = int(rot_custos[1])
  valor_cabo = int(rot_custos[2])
  g.matriz_adjacencias[rot2-1][rot1-1] = valor_cabo
  g.matriz_adjacencias[rot1-1][rot2-1] = valor_cabo
  
g.prim_mst();
