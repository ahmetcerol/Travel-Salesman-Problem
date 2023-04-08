import networkx as nx
import time

# burada dizinin 0.indisinde dizimizin büyüklüğü yer aldığı için 1.indisinden başlayarak
# x ve y koordinatlarını bir diziye atadığımız fonksiyon var
# strip ve split methodları dosya okurken karşılaşılan /n ve boşluk kavramlarını diziye atarken yok etmeke
with open('tsp_11849_1.txt', 'r') as f:
    lines = f.readlines()[1:]

coordinates = []
for line in lines:
    x, y = line.strip().split()
    coordinates.append({'x': float(x), 'y': float(y)})

# Minimum spanning tree'yi bulan algoritma
G = nx.Graph()

for i in range(len(coordinates)):
    x = coordinates[i]['x']
    y = coordinates[i]['y']
    G.add_node(i, pos=(x, y))

for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        dist = ((coordinates[i]['x']-coordinates[j]['x'])**2 + (coordinates[i]['y']-coordinates[j]['y'])**2)**0.5
        G.add_edge(i, j, weight=dist)

T = nx.minimum_spanning_tree(G)

# en kısa yolu bulan ve bu yolu giderken geçilen koordinatları ekrana yazdıran algoritma
#start time ise bu algoritma koşarken toplam ne kadar süre geçirildiğini bulmamıza yarayacak.
start_time = time.time()

pos = nx.get_node_attributes(T, 'pos')

path = list(nx.dfs_preorder_nodes(T, 0))
path.append(0)

total_distance = 0

for i in range(len(path)-1):
    start = path[i]
    end = path[i+1]
    distance = ((pos[start][0]-pos[end][0])**2 + (pos[start][1]-pos[end][1])**2)**0.5
    total_distance += distance
    print(f"Geçilen Düğüm: {start}, Koordinatlar: ({pos[start][0]}, {pos[start][1]})")

#geçilen her düğümü diziye atarak ardından toplam ne kadar bir mesafe yaparak algoritmayı tamamladığımızı gösterir.
print(f"Toplam Mesafe: {total_distance}")

#burada algoritma çalışırken ne kadar süre geçmiş onu hesaplıyoruz.
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Süre: {elapsed_time} saniye")
