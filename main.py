from data_manager import DataManager
from solvers import Knapsack_Solver


def main():
    filename = "knapsack_data.txt"

    capacity = 50
    num_items = 5
    

    #Generowanie danych
    DataManager.generate_data(filename, num_items, capacity,max_weight=30, max_value=100)


    

