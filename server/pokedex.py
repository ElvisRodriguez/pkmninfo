import sqlite3


def create_database():
    """Create a database for our pokedex.

    Args: None.

    Returns: None.
    """
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT,
        sprite_front_default TEXT,
        sprite_front_shiny TEXT,
        sprite_back_default TEXT,
        sprite_back_shiny TEXT,
        base_stats_hp INTEGER,
        base_stats_attack INTEGER,
        base_stats_defense INTEGER,
        base_stats_special_attack INTEGER,
        base_stats_special_defense INTEGER,
        base_stats_speed INTEGER,
        cry_latest TEXT,
        cry_legacy TEXT,
        pokedex_number INTEGER
    );
    """
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_names_table():
    """Transfer files of pokemon names into a database table.
    
    Args: None.
    
    Returns: None.
    """
    pokemon_names = []
    with open("names.txt", 'r') as file:
        pokemon_names = [line.rstrip('\n') for line in file]
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS pokemon_names (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """
    cursor.execute(query)
    connection.commit()
    for name in pokemon_names:
        query = "INSERT INTO pokemon_names (name) VALUES (?)"
        cursor.execute(query, (name,))
        connection.commit()
    connection.close()


def check_name(name):
    """Check if name is a valid pokemon name.

    Args:
        - name (str): Possible name of a pokemon.
    
    Returns:
        - (bool): Whether or not name is in the database.
    """
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name FROM pokemon_names WHERE name = ?", (name.title(),)
    )
    row = cursor.fetchone()
    if row is None:
        return False
    return True


def insert_pokemon_package(package):
    """Insert pokemon object into database.

    Args:
        - package (dict): Object containing pokemon data.
    
    Returns: None.
    """
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()
    data = (
        package["name"],
        package["sprite_front_default"],
        package["sprite_front_shiny"],
        package["sprite_back_default"],
        package["sprite_back_shiny"],
        package["base_stats"][0]["hp"],
        package["base_stats"][1]["attack"],
        package["base_stats"][2]["defense"],
        package["base_stats"][3]["special_attack"],
        package["base_stats"][4]["special_defense"],
        package["base_stats"][5]["speed"],
        package["cry_latest"],
        package["cry_legacy"],
        package["pokedex_number"]
    )
    query = """
    INSERT INTO pokemon (
        name,
        sprite_front_default,
        sprite_front_shiny,
        sprite_back_default,
        sprite_back_shiny,
        base_stats_hp,
        base_stats_attack,
        base_stats_defense,
        base_stats_special_attack,
        base_stats_special_defense,
        base_stats_speed,
        cry_latest,
        cry_legacy,
        pokedex_number
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    cursor.execute(query, data)
    connection.commit()
    connection.close()


def retrieve_pokemon_package(name):
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row is None:
        return {}
    pokemon_package = {
        "name": row[1],
        "sprite_front_default": row[2],
        "sprite_front_shiny": row[3],
        "sprite_back_default": row[4],
        "sprite_back_shiny": row[5],
        "base_stats": [
            {"hp": row[6]},
            {"attack": row[7]},
            {"defense": row[8]},
            {"special_attack": row[9]},
            {"special_defense": row[10]},
            {"speed": row[11]},
        ],
        "cry_latest": row[12],
        "cry_legacy": row[13],
        "pokedex_number": row[14],
    }
    return pokemon_package


if __name__ == "__main__":
    create_names_table()