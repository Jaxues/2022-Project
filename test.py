from audioop import add

from RecipeConverterWebapp import conversion_grams


conversion_to_grams_dict = {'ounce':28.35,
                      'pound':454,
                      'stick':113}

conversion_to_mills_dict = {'cup':240,
                      'teaspoon':5,
                      'tablespoon':15,
                       'pint':473,
                       'quart':946}


measurement_grams='ounce'
number_measurements=1
measurement_mills='cup'
conversion_grams=conversion_to_grams_dict[measurement_grams]*number_measurements
conversion_mills=conversion_to_mills_dict[measurement_mills]*number_measurements
add_to_tale_grams=(measurement_grams,number_measurements,conversion)
add_to_tale_mills=(measurement_mills,number_measurements,conversion_mills)
print(add_to_tale_grams)
print(add_to_tale_mills)