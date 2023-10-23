

import itertools
import math

#Methode zum Berechnen des kürzesten Weges.
class shortWay_01:
    @staticmethod
    def euclidean_distance(city1, city2):
        x1, y1 = city1
        x2, y2 = city2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    @staticmethod
    def total_distance(path, cities):
        distance = 0
        for i in range(len(path) - 1):
            distance += shortWay_01.euclidean_distance(cities[path[i]], cities[path[i + 1]])
        distance += shortWay_01.euclidean_distance(cities[path[-1]], cities[path[0]])
        return distance

    @staticmethod
    def getShortWay(staedte_positionen):
        # staedte_positionen = (
        #     (0.010319427306382911, 0.8956251389386756),
        #     (0.6999898714299346, 0.42254500074835377),
        #     (0.4294574582950912, 0.4568408794115657),
        #     (0.6005454852683483, 0.9295407203370832),
        #     (0.9590226056623925, 0.581453646599427),
        #     (0.748521134122647, 0.5437775417153159),
        #     (0.7571232013282426, 0.606435031856663),
        #     (0.07528757443413125, 0.07854082131763074),
        #     (0.32346175150639334, 0.7291706487873425)
        # )

        # Generiere alle möglichen Permutationen der Städte
        all_permutations = itertools.permutations(range(len(staedte_positionen)))

        # Finde die kürzeste Strecke
        shortest_path = None
        shortest_distance = float('inf')

        for path in all_permutations:
            distance = shortWay_01.total_distance(path, staedte_positionen)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

        # Der kürzeste Weg in richtiger Reihenfolge
        shortest_path_in_order = [staedte_positionen[i] for i in shortest_path]

        print("Kurzester Weg:", shortest_path_in_order)
        print("Kurzeste Entfernung:", shortest_distance)
        
        return shortest_path


