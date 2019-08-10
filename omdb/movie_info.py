#!/usr/bin/env python3

import sys

import requests

BASE_URL = "http://www.omdbapi.com/"
API_KEY = "f4c7dec0"

class Movie:
    def __init__(self, title):
        self.title = title
        self._data = {}
        self.year = self.data['Year']
        self.title = self.data['Title']
        self.director = self.data['Director']
        self.plot = self.data['Plot']
        self.genres = self.data['Genre'].split(', ')
        self.actors = self.data['Actors'].split(', ')

    @property
    def url(self):
        return f'{BASE_URL}?t={self.title}&apikey={API_KEY}'

    @property
    def data(self):
        if not self._data:
            response = requests.get(self.url)
            self._data = response.json()
        return self._data

    def print_movie(self):
        genres = ', '.join(self.genres)
        actors = ', '.join(self.actors)
        print(f"""
        {self.year} - {self.title}
        Director: {self.director}
        Actors: {actors}
        Genres: {genres}
        """)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a movie name')
    else:
        title = sys.argv[1]
        movie = Movie(title)
        movie.print_movie()
