import itertools #permütasyonlar için kullanılır
import math 
import time 

# İki nokta arasındaki mesafeyi hesaplayan fonksiyon
def calculate_distance(coordinate1, coordinate2):
    x1, y1 = coordinate1
    x2, y2 = coordinate2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Brute force yöntemi ile TSP problemi çözen fonksiyon
def brute_force_tsp(coordinates):
    start_time = time.time() # İşlem süresi hesaplamak için başlangıç zamanı
    shortest_route = None # En kısa rota, başlangıçta boş olarak tanımlanır
    shortest_distance = float("inf") # En kısa mesafe, başlangıçta sonsuz olarak tanımlanır
    for route in itertools.permutations(coordinates): # itertools.permutations() fonksiyonu, noktaların tüm permütasyonlarını oluşturur
        distance = 0 # Rota mesafesi, her döngü başında sıfırlanır
        for i in range(len(route)):
            if i == len(route) - 1: # Son noktaya ulaşıldıysa
                distance += calculate_distance(route[i], route[0]) # Son noktadan başlangıç noktasına olan mesafe eklenir
            else:
                distance += calculate_distance(route[i], route[i+1]) # İki nokta arasındaki mesafe hesaplanır ve toplam mesafeye eklenir
        if distance < shortest_distance: # Mevcut rota, en kısa rotadan daha kısa ise
            shortest_distance = distance # En kısa mesafe güncellenir
            shortest_route = route # En kısa rota güncellenir
    end_time = time.time() # İşlem süresi hesaplamak için bitiş zamanı
    elapsed_time = end_time - start_time # İşlem süresi, bitiş zamanından başlangıç zamanı çıkarılarak hesaplanır
    print(f"En kısa rota: {shortest_route}") # En kısa rotayı ekrana yazdır
    print(f"Toplam mesafe: {shortest_distance}") # En kısa mesafeyi ekrana yazdır
    print(f"İşlem süresi: {elapsed_time} saniye") # İşlem süresini ekrana yazdır

# burada dizinin 0.indisinde dizimizin büyüklüğü yer aldığı için 1.indisinden başlayarak
# x ve y koordinatlarını bir diziye atadığımız fonksiyon var
# strip ve split methodları dosya okurken karşılaşılan /n ve boşluk kavramlarını diziye atarken yok etmeke
with open('tsp_124_1.txt', 'r') as f:
    lines = f.readlines()[1:] # Dosyanın içindeki satırları okur ve ilk satırı atlar

# Noktaları depolamak için boş bir dizi tanımlanır
coordinates = []
for line in lines:
    x, y = line.strip().split()
    coordinates.append((float(x), float(y)))

brute_force_tsp(coordinates)
