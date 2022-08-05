sample_dict = {'WINTER': 12, 'SUMMER': 21, 'AUTUMN': 27, 'SPRING': 22}


def max_temp_season():
    season_key = list(sample_dict.keys())
    values_season = list(sample_dict.values())
    return season_key[values_season.index(max(values_season))]


print(max_temp_season())
