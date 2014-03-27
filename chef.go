package main

type Recipe struct {
	Title        string
	Ingredients  []string
	Instructions []string
	Score        int
}

type Chef struct {
	ingMgr    *IngredientManager
	Inventory []string
}

func NewChef(ingMgr *IngredientManager, inventory []string) *Chef {
	return &Chef{ingMgr, inventory}
}

// Returns a list of all Ingredients that MunchieMadness knows about
func (c *Chef) GetAllIngredients() []string{
	return c.ingMgr.GetAllIngredients()
}

func (c *Chef) HasIngredient(ingredient string) bool {
	for _, ing := range c.Inventory {
		if ing == ingredient {
			return true
		}
	}
	return false
}

// Indicates that user actually has a given Ingredient
func (c *Chef) AddToInventory(ingredient string) {
	if c.ingMgr.VerifyIngredient(ingredient) {
		c.Inventory = append(c.Inventory, ingredient)
	}
}

// Oops, user doesn't actually have any of that Ingredient
func (c *Chef) RemoveFromInventory(ingredient string) {
	for index, ing := range c.Inventory {
		if ing == ingredient {
			// To remove the ingredient, we set it to the last element and shorten the slice by 1
			c.Inventory[index] = c.Inventory[len(c.Inventory)-1]
			c.Inventory = c.Inventory[:len(c.Inventory)-1]
		}
	}
}

// Start fresh
func (c *Chef) ClearInventory() {
	c.Inventory = c.Inventory[:0]
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
