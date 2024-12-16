import collections
import operator
import random
from functools import reduce

from matplotlib import patches
from matplotlib.path import Path
from shapely import BufferCapStyle, LineString, Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt
from aocd import get_data
from aocd.post import submit


class Region:
    def __init__(self, character):
        self.vertices = []
        self.visited_vertices = []
        self.sides = []
        self.character = character

    def get_perimeter(self):
        total = 0
        for vertex in self.vertices:
            if (vertex[0] + 1, vertex[1]) not in self.vertices:
                self.sides.append((vertex[0] + 1, vertex[1]))
                total += 1
            if (vertex[0] - 1, vertex[1]) not in self.vertices:
                self.sides.append((vertex[0] - 1, vertex[1]))
                total += 1
            if (vertex[0], vertex[1] - 1) not in self.vertices:
                self.sides.append((vertex[0], vertex[1] - 1))
                total += 1
            if (vertex[0], vertex[1] + 1) not in self.vertices:
                self.sides.append((vertex[0], vertex[1] + 1))
                total += 1

        return total

    def get_sides(self):
        print(self.sides)
        start_point = self.sides[0]
        end_point = self.sides[0]
        current_point = start_point
        visited = []
        while end_point != current_point:
            # Same side
            if (current_point[0] + 1, current_point[1]) in self.vertices:
                pass
            elif (current_point[0] - 1, current_point[1]) in self.vertices:
                pass
            elif (current_point[0], current_point[1] + 1) in self.vertices:
                pass
            elif (current_point[0], current_point[1] - 1) in self.vertices:
                pass

            # New side


def floodfill(data, x, y, character, region_vertices):
    if data[y][x] == character:
        region_vertices.append((y, x))

        if x > 0 and (y, x - 1) not in region_vertices:
            floodfill(data, x - 1, y, character, region_vertices)
        if x < len(data[y]) - 1 and (y, x + 1) not in region_vertices:
            floodfill(data, x + 1, y, character, region_vertices)
        if y > 0 and (y - 1, x) not in region_vertices:
            floodfill(data, x, y - 1, character, region_vertices)
        if y < len(data) - 1 and (y + 1, x) not in region_vertices:
            floodfill(data, x, y + 1, character, region_vertices)


def main(testing: bool = False):
    if not testing:
        data = get_data(
            day=12,
            year=2024
        ).split('\n')
    else:
        data = open('test').read().split('\n')

    data = list(filter(None, data))
    answer = 0
    all_vertices = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            all_vertices.append((data[i][j], (i, j)))

    regions = []
    while True:
        if not all_vertices:
            break
        next_vertex = all_vertices.pop()
        character = next_vertex[0]
        coords = next_vertex[1]
        region = Region(character)
        floodfill(data, coords[1], coords[0], character, region.vertices)
        if region.vertices:
            # region.get_rid_of_dupes()
            regions.append(region)
            for vertex in region.vertices:
                if (character, vertex) in all_vertices:
                    all_vertices.remove((character, vertex))

    for region in regions:
        answer += len(region.vertices) * region.get_perimeter()
        print(region.get_sides())

    if testing:
        print(answer)
    else:
        submit(answer)


if __name__ == '__main__':
    main(True)
