from flask import Flask, jsonify, request
from flask_cors import CORS
import pokebase as pb

import pokedex


app = Flask(__name__)
cors = CORS(app, origins='*')


@app.route("/api/pokemon", methods=["POST"])
def pokemon():
    if request.method == "POST":
        pokemon_name = request.json.get("pokemon_name")
        if not pokedex.check_name(pokemon_name):
            return jsonify({})
        _pokemon = pb.pokemon(pokemon_name)
        pokemon_package = pokedex.retrieve_pokemon_package(pokemon_name)
        if pokemon_package:
            return jsonify(pokemon_package)
        pokemon_package = {
                "name": _pokemon.name,
                "sprite_front_default": _pokemon.sprites.front_default,
                "sprite_front_shiny": _pokemon.sprites.front_shiny,
                "sprite_back_default": _pokemon.sprites.back_default,
                "sprite_back_shiny": _pokemon.sprites.back_shiny,
                "base_stats": [
                    {"hp": _pokemon.stats[0].base_stat},
                    {"attack": _pokemon.stats[1].base_stat},
                    {"defense": _pokemon.stats[2].base_stat},
                    {"special_attack": _pokemon.stats[3].base_stat},
                    {"special_defense": _pokemon.stats[4].base_stat},
                    {"speed": _pokemon.stats[5].base_stat},
                ],
                "cry_latest": _pokemon.cries.latest,
                "cry_legacy": _pokemon.cries.legacy,
                "pokedex_number": _pokemon.id,
            }
        pokedex.insert_pokemon_package(pokemon_package)
        return jsonify(pokemon_package)
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True, port=8080)