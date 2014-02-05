package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type Context struct {
	foo int
}

func rootHandler(w http.ResponseWriter, r *http.Request, c *Context) {
	renderTemplate(w, "index.html")
}

func makeHandler(c *Context, fn func(http.ResponseWriter, *http.Request, *Context)) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		fn(w, r, c)
	}
}

func main() {
	c := &Context{42}

	http.HandleFunc("/", makeHandler(c, rootHandler))

	fmt.Println("Serving webserver...")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Printf(err.Error())
	}
}

func renderTemplate(w http.ResponseWriter, tmpl string) {
	t, err := template.ParseFiles(tmpl)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	err = t.Execute(w, nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}
