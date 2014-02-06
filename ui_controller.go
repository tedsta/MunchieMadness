package main

import ()

type UIController struct {
	chef *Chef
}

// Initialization creates a Chef object to which all commands will be passed
func NewUIController() *UIController {
	return &UIController{NewChef(NewIngredientManager(), nil)}
}

// Returns a list of all Ingredients that MunchieMadness knows about
func (u *UIController) GetAllIngredients() IngredientList {
	return u.chef.GetAllIngredients()
}

// Indicates that user actually has a given Ingredient
func (u *UIController) AddToInventory(ingredient string) {
	u.chef.AddToInventory(ingredient)
}

// Oops, user doesn't actually have any of that Ingredient
func (u *UIController) RemoveFromInventory(ingredient string) {
	u.chef.RemoveFromInventory(ingredient)
}

// Start fresh
func (u *UIController) ClearInventory() {
	u.chef.ClearInventory()
}

// Returns address of image corresponding to an Ingredient
func (u *UIController) GetImage(ingredient string) string {
	return u.chef.GetImage(ingredient)
}

// This is where the magic happens. Returns a Recipe, which has:
// title, a string like "Peanut Butter Chocoloate Chip Popcorn Sandwich"
// ingredients, a list of strings like ['Bread', 'Peanut Butter', 'Chocolate Chips', 'Popcorn']
// instructions, a list of strings like ['Spread peanut butter on one or both slices of bread', 'Sprinkle with Chocolate Chips', ...]
// TODO some sort of weirdness score?
func (u *UIController) GenerateRecipe(maxScore int) *Recipe {
	return u.chef.GenerateRecipe(maxScore)
}
