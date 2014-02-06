package main

type Recipe struct {
	title        string
	ingredients  []string
	instructions []string
	score        int
}

type Chef struct {
	ingMgr    *IngredientManager
	inventory IngredientList
}

func NewChef(ingMgr *IngredientManager, inventory IngredientList) *Chef {
	return &Chef{ingMgr, inventory}
}

// Returns a list of all Ingredients that MunchieMadness knows about
func (c *Chef) GetAllIngredients() IngredientList {
	return c.ingMgr.GetAllIngredients()
}

func (c *Chef) HasIngredient(ingredient string) bool {
	return c.inventory.Contains(ingredient)
}

// Indicates that user actually has a given Ingredient
func (c *Chef) AddToInventory(ingredient string) {
	if c.ingMgr.VerifyIngredient(ingredient) {
		c.inventory.Add(ingredient)
	}
}

// Oops, user doesn't actually have any of that Ingredient
func (c *Chef) RemoveFromInventory(ingredient string) {
	c.inventory.Remove(ingredient)
}

// Start fresh
func (c *Chef) ClearInventory() {
	c.inventory.Clear()
}

// Returns address of image corresponding to an Ingredient
func (c *Chef) GetImage(ingredient string) string {
	return c.ingMgr.GetImage(ingredient)
}

func (c *Chef) GenerateRecipe(maxScore int) *Recipe {
	ingreds := []string{"Bread", "Butter", "Ham", "Cheese", "Popcorn"}
	instructs := []string{"Slice cheese", "Pop popcorn", "Put Ham, Cheese and Popcorn between slices of Bread",
		"Spread Butter on outside of Bread", "Grill over medium low heat, turning once",
		"Cut in half and enjoy"}
	score := 3
	hardcoded_result := &Recipe{"Grilled Ham, Cheese and Popcorn Sandwich",
		ingreds, instructs, score}
	return hardcoded_result
}
