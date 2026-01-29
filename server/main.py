from flask import Flask, jsonify, request
from flask_cors import CORS
import pokebase as pb


app = Flask(__name__)
cors = CORS(app, origins='*')


@app.route("/api/sample", methods=["GET"])
def users():
    scizor = pb.pokemon("scizor")
    return jsonify (
        {
            "name": scizor.name,
            "sprite_front_default": scizor.sprites.front_default,
            "base_stats": [
                {"hp": scizor.stats[0].base_stat},
                {"attack": scizor.stats[1].base_stat},
                {"defense": scizor.stats[2].base_stat},
                {"special_attack": scizor.stats[3].base_stat},
                {"special_defense": scizor.stats[4].base_stat},
                {"speed": scizor.stats[5].base_stat},
            ],
            "cry_latest": scizor.cries.latest,
            "pokedex_number": scizor.id,
        }
    )

@app.route("/api/pokemon", methods=["POST"])
def pokemon():
    if request.method == "POST":
        pokemon_name = request.json.get("pokemon_name")
        _pokemon = pb.pokemon(pokemon_name)
        if hasattr(_pokemon, "results"):
            return {}
        return jsonify (
            {
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
        )
    return {}


if __name__ == "__main__":
    app.run(debug=True, port=8080)