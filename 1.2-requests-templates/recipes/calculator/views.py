from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, recipe):
    servings = request.GET.get('servings', None)

    # if servings:
    servings_dict = {}
    for ingredient, quantity in DATA[recipe].items():
         servings_dict[ingredient] = quantity*int(servings)

         context = {
                    'recipe_name': recipe,
                    'recipe': servings_dict
                }

      # else:
      #
      #     context = {
      #         'recipe': {
      #             'ingredient': quantity,
      #             'ingredient': quantity,
      #         }
      #     }
    return render(request, 'calculator/index.html', context)

def home_view(request):

    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, template_name='home/home.html', context=context)