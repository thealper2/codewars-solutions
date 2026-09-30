def cakes(recipe, available):
    return min(available.get(ing, 0) // amt for ing, amt in recipe.items())