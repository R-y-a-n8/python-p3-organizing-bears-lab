select_all_female_animals = """
    SELECT name, species, age
    FROM animals
    WHERE gender='F';
"""

select_all_dogs = """
    SELECT name, age
    FROM animals
    WHERE species='Dog';
"""

select_adopted_animals = """
    SELECT name, species, age
    FROM animals
    WHERE adopted=1;
"""
