from array_queue_ext import ArrayQueueExt
from data_structures import ArrayQueue

def ejecutar_pruebas():
    print("=== CLIENTE DE PRUEBA: ArrayQueueExt ===")
    
    cola_a = ArrayQueueExt()
    print(f"\n1. probando __bool__:")
    print(f"la cola esta vacia? {bool(cola_a)} (Esperado: True)")

    elementos = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    for x in elementos:
        cola_a.enqueue(x)
    
    print(f"Cargando elementos: {elementos}")
    print(f"la cola esta vacía ahora? {bool(cola_a)} (Esperado: False)")

   
    print(f"\n2. Probando reverse_upto(k=4):")
    cola_a.reverse_upto(4)
   
    print("Estado esperado: [40, 30, 20, 10, 50, 60, 70, 80, 90]")

    print(f"\n3. Probando intercalar:")
    cola_b = ArrayQueue()
    for x in [1, 2, 3, 4, 5]:
        cola_b.enqueue(x)
    
    print(f"Intercalando con otra cola: [1, 2, 3, 4, 5]")
    cola_a.intercalar(cola_b)

    print("\nRESULTADO FINAL (Intercalado)")
    resultados = []
    while not cola_a.is_empty():
        resultados.append(str(cola_a.dequeue()))
    
    print(" -> ".join(resultados))

if __name__ == "__main__":
    ejecutar_pruebas()
    