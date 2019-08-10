#!/usr/bin/env python3

import csv

def get_items_from_csv(file_path):
    items = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)
    return items


def get_avg(items):
    return int(sum(items) / len(items))


class CrimeStatistics:
    def __init__(self, crimes):
        self.crimes = self.sanitize_data(crimes)

    @staticmethod  # because we don't care about self
    def sanitize_data(items):
        return [
            {
                'year': int(item['Year']),
                'population': int(item['Population']),
                'murder': int(item['Murder']),
                'robbery': int(item['Robbery']),
                'assault': int(item['Assault']),
                'burglary': int(item['Burglary']),
                'car_theft': int(item['CarTheft']),
            } for item in items
        ]


    def get_average_population(self):
        return get_avg(
            [item['population'] for item in self.crimes]
        )


if __name__ == '__main__':
    crimes = get_items_from_csv('./crime.csv')
    stats = CrimeStatistics(crimes)
    print(stats.get_average_population())
