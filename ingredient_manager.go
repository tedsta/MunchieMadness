package main

import (
	"os"
	"strings"
)

var allIngredients IngredientList = []string{"Bread", "Butter", "Ham", "Cheese", "Popcorn"}

type IngredientManager struct {
}

func NewIngredientManager() *IngredientManager {
	// TODO read a file, call a database, something?
	// for now all ingredient info is hardcoded in the IngredientManager class,
	// but that's not always gonna cut it...
	return &IngredientManager{}
}

// Returns a list of all Ingredients that MunchieMadness knows about
func (i *IngredientManager) GetAllIngredients() IngredientList {
	return allIngredients
}

func (i *IngredientManager) VerifyIngredient(ingredient string) bool {
	return allIngredients.Contains(ingredient)
}

// Returns address of image corresponding to an Ingredient
func (i *IngredientManager) GetImage(ingredient string) string {
	path := "images/" + strings.ToLower(ingredient) + ".png"
	if _, err := os.Stat(path); os.IsExist(err) {
		return path
	} 
	return ""
}
