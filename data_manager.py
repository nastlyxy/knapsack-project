import random
from item import Item

class DataManager:
    @staticmethod
    def generate_data(filename: str, C: int, n: int, max_weight: int = 20, max_value: int = 50) -> None:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"{C}\n")
            f.write(f"{n}\n")
            for _ in range(n):
                # Generowanie losowej wartości (p_i) i objętości (w_i)
                p = random.randint(1, max_value)
                w = random.randint(1, max_weight)
                f.write(f"{p} {w}\n")
        print(f"File successfully generated '{filename}' (n={n}, C={C}).")

    @staticmethod
    def load_data(filename: str) -> tuple[int, list[Item]]:
        items = []
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
            C = int(lines[0])
            n = int(lines[1])
            
            # Odczytywanie n wierszy z parametrami przedmiotów (p_i, w_i)
            for i in range(2, 2 + n):
                parts = lines[i].split()
                p = int(parts[0])
                w = int(parts[1])
                # ID na podstawie numeru wiersza (i - 1, by zacząć od 1)
                items.append(Item(id=i-1, value=p, weight=w))
                
        return C, items