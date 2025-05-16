import threading
import random
import time

numFilosofos = 5
tempoLimite = 20
init =time.time()

semaforo = threading.Semaphore(numFilosofos - 1)

ultimoQueComeuLock = threading.Lock()
ultimoQueComeu = None

class Filosofo(threading.Thread):
    def __init__(self, id, garfoEsquerdo, garfoDireito):
        threading.Thread.__init__(self)
        self.id = id
        self.garfoEsquerdo = garfoEsquerdo
        self.garfoDireito = garfoDireito

    def pensar(self):
        print(f"🧠 Filósofo {self.id} está pensando.")
        time.sleep(random.uniform(1, 2))

    def comer(self):
        global ultimoQueComeu
        with ultimoQueComeuLock:
            if ultimoQueComeu == self.id:
                print(f"⛔ Filósofo {self.id} acabou de comer. Esperando para evitar repetição.")
                return False

            print(f"🍝 Filósofo {self.id} começa a comer.")
            time.sleep(random.uniform(1, 2))
            print(f"✅ Filósofo {self.id} terminou de comer.")
            ultimoQueComeu = self.id
            return True

    def run(self):
        while True:
            self.pensar()

            semaforo.acquire()
            primeiro, segundo = (self.garfoEsquerdo, self.garfoDireito) \
                if id(self.garfoEsquerdo) < id(self.garfoDireito) \
                else (self.garfoDireito, self.garfoEsquerdo)

            with primeiro:
                with segundo:
                    if not self.comer():
                        semaforo.release()
                        time.sleep(random.uniform(0.5, 1))
                        continue

            semaforo.release()

if __name__ == "__main__":
    garfos = [threading.Lock() for _ in range(numFilosofos)]

    filosofos = [
        Filosofo(i, garfos[i], garfos[(i + 1) % numFilosofos])
        for i in range(numFilosofos)
    ]

    for f in filosofos:
        f.start()