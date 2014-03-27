package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type Context struct {
	MyChef Chef
	Inglist []string
	Rec *Recipe
}

func NewContext() *Context {
	c := &Context{}
	c.Inglist = c.MyChef.GetAllIngredients()
	return c
}

func makeHandler(c *Context, fn func(http.ResponseWriter, *http.Request, *Context)) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		fn(w, r, c)
	}
}

func rootHandler(w http.ResponseWriter, r *http.Request, c *Context) {
	renderTemplate(w, "templates/add_ingredients.html", c)
}

func recipeHandler(w http.ResponseWriter, r *http.Request, c *Context) {
	// Parse form, add selected ingredients to inventory
	for _, ing := range c.Inglist {
		if r.FormValue(ing) == "on" {
			c.MyChef.AddToInventory(ing)
		}
	}

	// Generate recipe and serve page
	c.Rec = c.MyChef.GenerateRecipe(10)
	renderTemplate(w, "templates/recipe.html", c)
}

func main() {
	c := NewContext()

	http.HandleFunc("/", makeHandler(c, rootHandler))
	http.HandleFunc("/recipe", makeHandler(c, recipeHandler))

	fmt.Println("Serving webserver...")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Printf(err.Error())
	}
}

func renderTemplate(w http.ResponseWriter, tmpl string, c *Context) {
	t, err := template.ParseFiles(tmpl)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	err = t.Execute(w, c)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}
