import csv

# Dicionário para armazenar a música mais tocada de cada ano
top_tracks_by_year = {}

# Abrir o arquivo com codificação 'latin-1'
with open('spotify-2023.csv', 'r', encoding='latin-1') as file:
    reader = csv.reader(file)
    header = next(reader)  # Pular o cabeçalho

    for row in reader:
        # Ignorar linhas que não tenham exatamente o número esperado de colunas
        if len(row) != 10:
            continue

        try:
            track_name = row[0]
            artist_name = row[1]
            artist_count = int(row[2])
            released_year = int(row[3])
            streams = int(row[8])
        except (ValueError, IndexError):
            continue  # pula linhas com dados inválidos

        # Considerar apenas músicas entre 2012 e 2022
        if 2012 <= released_year <= 2022:
            current_best = top_tracks_by_year.get(released_year)

            # Se ainda não há música para esse ano, ou a atual tem mais streams, substitui
            if current_best is None or streams > current_best[3]:
                top_tracks_by_year[released_year] = [track_name, artist_name, released_year, streams]

# Ordenar a lista por ano
top_tracks_sorted = [top_tracks_by_year[year] for year in sorted(top_tracks_by_year)]

# Imprimir a lista final
for track in top_tracks_sorted:
    print(track)
