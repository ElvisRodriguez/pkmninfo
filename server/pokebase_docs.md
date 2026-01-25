#pokebase.APIMetadata:
Helper class for smaller references.

    This class emulates a dictionary, but attribute lookup is via the `.`
    operator, not indexing. (ex. instance.attr, not instance['attr']).

    Used for "Common Models" classes and APIResource helper classes.
    https://pokeapi.co/docsv2/#common-models
    
#pokebase.APIResource:
Core API class, used for accessing the bulk of the data.

    The class uses a modified __getattr__ function to serve the appropriate
    data, so lookup data via the `.` operator, and use the `PokeAPI docs
    <https://pokeapi.co/docsv2/>`_ or the builtin `dir` function to see the
    possible lookups.

    This class takes the complexity out of lots of similar classes for each
    different kind of data served by the API, all of which are very similar,
    but not identical.
    
#pokebase.APIResourceList:
Class for a data container.

    Used to access data corresponding to a category, rather than an individual
    reference. Ex. APIResourceList('berry') gives information about all
    berries, such as which ID's correspond to which berry names, and
    how many berries there are.

    You can iterate through all the names or all the urls, using the respective
    properties. You can also iterate on the object itself to run through the
    `dict`s with names and urls together, whatever floats your boat.
    
#pokebase.SpriteResource:
No docstring found.

#pokebase.ability:
Quick ability lookup.

    See https://pokeapi.co/docsv2/#abilities for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.api:
No docstring found.

#pokebase.berry:
Quick berry lookup.

    See https://pokeapi.co/docsv2/#berries for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.berry_firmness:
Quick berry-firmness lookup.

    See https://pokeapi.co/docsv2/#berry-firmnesses for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.berry_flavor:
Quick berry-flavor lookup.

    See https://pokeapi.co/docsv2/#berry-flavors for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.cache:
No docstring found.

#pokebase.characteristic:
Quick characteristic lookup.

    See https://pokeapi.co/docsv2/#characteristics for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.common:
No docstring found.

#pokebase.contest_effect:
Quick contest-effect lookup.

    See https://pokeapi.co/docsv2/#contest-effects for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.contest_type:
Quick contest-type lookup.

    See https://pokeapi.co/docsv2/#contest-types for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.egg_group:
Quick egg-group lookup.

    See https://pokeapi.co/docsv2/#egg-groups for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.encounter_condition:
Quick encounter-condition lookup.

    See https://pokeapi.co/docsv2/#encounter-conditions for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.encounter_condition_value:
Quick encounter-condition-value lookup.

    See https://pokeapi.co/docsv2/#encounter-condition-values for attributes
    and more detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.encounter_method:
Quick encounter-method lookup.

    See https://pokeapi.co/docsv2/#encounter-methods for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.evolution_chain:
Quick evolution-chain lookup.

    See https://pokeapi.co/docsv2/#evolution-chains for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.evolution_trigger:
Quick evolution-trigger lookup.

    See https://pokeapi.co/docsv2/#evolution-triggers for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.gender:
Quick gender lookup.

    See https://pokeapi.co/docsv2/#genders for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.generation:
Quick generation lookup.

    See https://pokeapi.co/docsv2/#generations for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.growth_rate:
Quick growth-rate lookup.

    See https://pokeapi.co/docsv2/#growth-rates for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.interface:
No docstring found.

#pokebase.item:
Quick item lookup.

    See https://pokeapi.co/docsv2/#items for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.item_attribute:
Quick item-attribute lookup.

    See https://pokeapi.co/docsv2/#item-attributes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.item_category:
Quick item-category lookup.

    See https://pokeapi.co/docsv2/#item-categories for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.item_fling_effect:
Quick item-fling-effect lookup.

    See https://pokeapi.co/docsv2/#item-fling-effects for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.item_pocket:
Quick item-pocket lookup.

    See https://pokeapi.co/docsv2/#item-pockets for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.language:
Quick language lookup.

    See https://pokeapi.co/docsv2/#languages for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.loaders:
No docstring found.

#pokebase.location:
Quick location lookup.

    See https://pokeapi.co/docsv2/#locations for attributes and more detailed
    information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.location_area:
Quick location-area lookup.

    See https://pokeapi.co/docsv2/#location-areas for attributes and more
    detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.machine:
Quick machine lookup.

    See https://pokeapi.co/docsv2/#machines for attributes and more detailed
    information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.move:
Quick move lookup.

    See https://pokeapi.co/docsv2/#moves for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.move_ailment:
Quick move-ailment lookup.

    See https://pokeapi.co/docsv2/#move-ailments for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.move_battle_style:
Quick move-battle-style lookup.

    See https://pokeapi.co/docsv2/#move-battle-styles for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.move_category:
Quick move-category lookup.

    See https://pokeapi.co/docsv2/#move-categories for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.move_damage_class:
Quick move-damage-class lookup.

    See https://pokeapi.co/docsv2/#move-damage-classes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.move_learn_method:
Quick move-learn-method lookup.

    See https://pokeapi.co/docsv2/#move-learn-methods for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.move_target:
Quick move-target lookup.

    See https://pokeapi.co/docsv2/#move-targets for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.nature:
Quick nature lookup.

    See https://pokeapi.co/docsv2/#natures for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pal_park_area:
Quick pal-park-area lookup.

    See https://pokeapi.co/docsv2/#pal-park-areas for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokeathlon_stat:
Quick pokeathlon-stat lookup.

    See https://pokeapi.co/docsv2/#pokeathlon-stats for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokedex:
Quick pokedex lookup.

    See https://pokeapi.co/docsv2/#pokedexes for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokemon:
Quick pokemon lookup.

    See https://pokeapi.co/docsv2/#pokemon for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokemon_color:
Quick pokemon-color lookup.

    See https://pokeapi.co/docsv2/#pokemon-colors for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokemon_form:
Quick pokemon-form lookup.

    See https://pokeapi.co/docsv2/#pokemon-forms for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokemon_habitat:
Quick pokemon-habitat lookup.

    See https://pokeapi.co/docsv2/#pokemon-habitats for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokemon_shape:
Quick pokemon-shape lookup.

    See https://pokeapi.co/docsv2/#pokemon-shapes for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.pokemon_species:
Quick pokemon-species lookup.

    See https://pokeapi.co/docsv2/#pokemon-species for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.region:
Quick region lookup.

    See https://pokeapi.co/docsv2/#regions for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.sprite:
No docstring found.

#pokebase.stat:
Quick stat lookup.

    See https://pokeapi.co/docsv2/#stats for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.super_contest_effect:
Quick super-contest-effect lookup.

    See https://pokeapi.co/docsv2/#super-contest-effects for attributes and
    more detailed information.

    :param id_: id of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.type_:
Quick type lookup.

    See https://pokeapi.co/docsv2/#types for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.version:
Quick version lookup.

    See https://pokeapi.co/docsv2/#versions for attributes and more detailed
    information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
#pokebase.version_group:
Quick version-group lookup.

    See https://pokeapi.co/docsv2/#version-groups for attributes and more
    detailed information.

    :param id_or_name: id or name of the resource to lookup
    :return: NamedAPIResource with the appropriate data
    
