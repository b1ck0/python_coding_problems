if __name__ == "__main__":
    import breadth_first_search
    import depth_first_search

    Bulgaria = {
        "Shabla": {"Kavarna", "Tulenovo", "Durankulak"},
        "Kavarna": {"Shabla", 'Balchik', 'Balgarevo'},
        "Balchik": {"Albena", "Kavarna", "Dobrich", "Varna"},
        "Varna": {"Balchik", "Dobrich", "Burgas", "Shumen"},
        "Dobrich": {"Silistra", "Varna", "Balchik", "Albena", 'Shumen'},
        "Shumen": {"Ruse", "Silistra", "Dobrich", "Varna", "Veliko Tarnovo"},
        "Veliko Tarnovo": {"Sofia"},
        "Sofia": {"Veliko Tarnovo", "Plovdiv"},
        "Tulenovo": {"Shabla", "Balgarevo"},
        "Balgarevo": {"Tulenovo", "Kavarna"},
        "Burgas": {"Plovdiv", "Varna"},
        "Plovdiv": {"Sofia", "Burgas"},
        "Ruse": {"Shumen"},
        "Durankulak": {"Shabla"},
        "Silistra": {"Dobrich", "Shumen"},
        "Albena" : {"Dobrich", "Balchik", "Varna"}
    }

    print(depth_first_search.dfs_visible_nodes(Bulgaria, "Shabla"))
    print(depth_first_search.dfs_all_possible_paths(Bulgaria, "Shabla", "Sofia"))
