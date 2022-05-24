import time
import datetime
import networkx as nx

# LOGISTICS
class Transport:
    def __init__(self,name: str,fuel_cons: float,speed: float,volume: float, weight: float, temperature: float):
        """
        :param speed: Скорость транспорта
        :param volume: Объем кузова
        :param weight: Максимально возможный вес груза
        :param temperature: Температура в кузове (грузовой части салона)
        :rtype: None
        """
        self.name = name
        self.fuel_cons = fuel_cons
        self.cur_pos = cur_pos
        self.max_weight = max_weight
        self.weight = weight
        self.max_volume = max_volume
        self.place_of_residence = place_of_residence
        self.load_cond_id = load_cond_id
        self.speed = speed
        self.volume = volume
        self.temperature = temperature

        self.products: list[Product] = []

        if not (isinstance(speed, int) or isinstance(speed, float)):
            raise TypeError("speed must be an integer or float")
        if not (isinstance(volume, int) or isinstance(volume, float)):
            raise TypeError("volume must be an integer or float")
        if not (isinstance(temperature, int) or isinstance(temperature, float)):
            raise TypeError("temperature must be an integer or float")
        if not (isinstance(weight, int) or isinstance(weight, float)):
            raise TypeError("weight must be an integer or float")
        
class Car(Transport)
        
    def load(self, products) -> bool:
        summary_weight, summary_volume = 0, 0
        for item in products:
            if not issubclass(item.__class__, Product): # Проверяем, что элемент - продукт или его дочерний класс
                raise TypeError("product must be Product or or its child class")
            summary_weight += item.weight
            summary_volume += item.product_volume
            if (summary_weight > self.weight) or (summary_volume > self.volume):
                return False
            time.sleep(1)
    
        # Уменьшаем макс. возможный вес для данного объекта (1 конкретной машины, в которой уже лежит часть груза)
        self.weight -= summary_weight
        self.volume -= summary_volume
        # Закидываем груз в машину
        self.products += products
        return True
    
    def get_name(self, name:str):
        pass
        
    def get_speed(self, speed:float):
        pass

        
class Map:
    self.nodes = set()
    storages = {'A':(0, 20),
         'B':(15, 24),
         'C':(16, 41),
         'D':(10, 40)}
    stores = {'E':(0, 20),
         'F':(15, 24),
         'G':(16, 41),
         'H':(10, 40)}
    kilometres = {('A', 'B', 15),
                  ('B', 'C', 16),
                  ('B', 'D', 25),
                  ('C', 'D', 14),
                  ('D', 'A', 18)}
    
    graph.add_weighted_edges_from(kilometres)
    graph = nx.Graph()
    graph.add_nodes_from(storages)
    graph.add_nodes_from(stores)
    def create_node(self, nodename):
        if nodename in self.nodes:
            return False
        self.nodes.add(nodename)
        return True 
    
    def connect_node(self, nodeA, nodeB, weight):
        self.Graph.add_edge(nodeA,nodeB,weight=weight)