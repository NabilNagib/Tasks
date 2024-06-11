def set_table(the_dead):
    preferences = {
        'Earthenware': set('QUTHCRDMZ'),
        'Waterfall': set('WEVOXING'),
        'Fireplace': set('JFABKPLY'),
        'Windowsill': set('SRUHMNAD')
    }

    preferred_seats = {
        'Earthenware': [1, 12, 2, 11, 3],
        'Waterfall': [4, 3, 5, 2, 6],
        'Fireplace': [7, 6, 8, 5, 9],
        'Windowsill': [10, 9, 11, 8, 12]
    }

    all_seats = list(range(1, 13))
    seating = ["_____" for _ in range(12)]

    def find_clan(name):
        ghost_clans = [
            {'clan': "Earthenware", 'value': "QUTHCRDMZ"},
            {'clan': "Waterfall", 'value': "WEVOXING"},
            {'clan': "Fireplace", 'value': "JFABKPLY"},
            {'clan': "Windowsill", 'value': "SRUHMNAD"}
        ]
        first_letter = name[0].upper()
        found_clan = next((obj['clan'] for obj in ghost_clans if obj['value'].find(first_letter) != -1), None)
        return found_clan

    def ghost_seats(ghost_name):
        clan = find_clan(ghost_name)
        if not clan:
            return None

        clan_seats = preferred_seats[clan]
        if not clan_seats or len(clan_seats) == 0:
            return None

        available_seat_index = next((i for i, seat in enumerate(clan_seats) if seat in all_seats), -1)
        if available_seat_index == -1:
            return None

        seat = clan_seats.pop(available_seat_index)
        all_seats.remove(seat)

        rotated_seats = clan_seats[available_seat_index:] + clan_seats[:available_seat_index]
        preferred_seats[clan] = rotated_seats

        return seat

    seated_ghosts_count = 0
    for ghost in the_dead:
        if seated_ghosts_count >= 12:
            break  # Only seat the first 12 ghosts
        seat = ghost_seats(ghost)
        if seat is not None:
            seating[seat - 1] = ghost
            seated_ghosts_count += 1

    return seating
