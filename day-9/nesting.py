capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#nesting a list in a dictionary
travel_list = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
#nesting a dictionary in a dictionary
travel_list = {
    "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"Cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
#nesting a dictionary in a list
travel_list = [
    {
        "Country": "France",
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
         "Country": "Germany",
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5

    }
]

print(travel_list["Country"][1][1])