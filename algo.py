# algo.py
import click
import googlemaps
import pandas as pd
from itertools import tee

@click.command()
def main():
    df = pd.read_csv('go_track_trackspoints.csv', sep=';')
    gmaps = googlemaps.Client(key='AIzaSyAZs33KAQ57SeZ6HJJYd-4nFisiFTnES94')

    for row in df.iterrows():
        distList = []
        for row2 in df.iterrows():
            result = gmaps.distance_matrix(origins=row[0], destinations=row2[0], mode="driving")["rows"][0]["elements"][0]["distance"]["value"]
            distList.append(result)    
    
    click.echo(list)

if __name__ == "__main__":
    main()