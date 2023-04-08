import time

start_time = time.time()  # Başlangıç zamanını kaydet

# burada dizinin 0.indisinde dizimizin büyüklüğü yer aldığı için 1.indisinden başlayarak
# x ve y koordinatlarını bir diziye atadığımız fonksiyon var
# strip ve split methodları dosya okurken karşılaşılan /n ve boşluk kavramlarını diziye atarken yok etmeke
with open('tsp_1000_1.txt', 'r') as f:
    lines = f.readlines()[1:]

coordinates = []
for line in lines:
    x, y = line.strip().split()
    coordinates.append((float(x), float(y)))

# Nokta sayısını al ve ilk noktayı ziyaret edildi olarak işaretle
n = len(coordinates)
visited = [False] * n #noktaların geçilip geçilmediği kontrolünü yapmak için ilk başta hepsini false olarak işaretliyoruz.
visited[0] = True
current = 0 #başlangıç konumunu 0 olarak başlat.
total_distance = 0 #toplam mesafeyi 0 olarak başlat.
path = [0]

# Tüm noktalar ziyaret edilene kadar algoritmayı çalıştır.
while False in visited:
    min_distance = float('inf')
    nearest_neighbor = None
     # Ziyaret edilmemiş tüm noktaları gez ve en yakın komşuyu bul
    for j in range(n):
        if not visited[j]:
           # İki nokta arasındaki öklid mesafesini hesapla
            distance = ((coordinates[j][0]-coordinates[current][0])**2 + (coordinates[j][1]-coordinates[current][1])**2)**0.5
            # En küçük mesafeyi bul
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = j
    # En yakın komşuyu ziyaret edildi olarak işaretle ve yeni konuma git
    visited[nearest_neighbor] = True
    current = nearest_neighbor
    total_distance += min_distance
    path.append(nearest_neighbor)

    
# Başlangıç noktasına dönüş yap ve toplam yol mesafesini hesapla
total_distance += ((coordinates[path[0]][0]-coordinates[path[-1]][0])**2 + (coordinates[path[0]][1]-coordinates[path[-1]][1])**2)**0.5
path.append(path[0])

end_time = time.time()  # Bitiş zamanını kaydet
elapsed_time = end_time - start_time  # Geçen süreyi hesapla

print(f"En kısa yol: {total_distance}")
print("Yol: ")
for node in path:
    print(coordinates[node], end="\n")
print()
print(f"Geçen süre: {elapsed_time} saniye")
shortest_path = path[:-1]  # Son noktadan başlangıç noktasına kadar olan kısmı en kısa yolu oluşturur
total_nodes = len(set(shortest_path))  # En kısa yol üzerinde geçilen toplam nokta sayısı
print(f"En kısa yol üzerinde geçilen toplam nokta sayısı: {total_nodes}")

