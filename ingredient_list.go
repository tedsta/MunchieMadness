package main

// A list of the ingredients
type IngredientList []string

func (i IngredientList) Contains(ingredient string) bool {
	for _, ing := range i {
		if ing == ingredient {
			return true
		}
	}

	return false
}

func (i IngredientList) Add(ingredient string) {
	i = append(i, ingredient)
}

func (i IngredientList) Remove(ingredient string) {
	for index, ing := range i {
		if ing == ingredient {
			// To remove the ingredient, we set it to the last element and shorten the slice by 1
			i[index] = i[len(i)-1]
			i = i[:len(i)-1]
		}
	}
}

func (i IngredientList) Clear() {
	i = i[:0]
}
