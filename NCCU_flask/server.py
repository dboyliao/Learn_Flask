from flask import Flask, render_template, request

app = Flask("todo-list")
app.debug = True

@app.route("/")
def hello():
    name = request.args.get("name", "World") # get field name or return "World"
    todo_list = ["Todo 1", "Todo 2"]
    return render_template("todo.html", todo_list = todo_list, name = name)

@app.route("/dict")
def dictionary():
    dictionary = {"apple":"a fruit", "calculus": "a subject", "name": "Dboy"}
    key = request.args.get("key") # get field name or return "World"
    # request.args is a dictionary like object.
    # You can use request.args.keys() to get all available keys in one request.
    # ex: /dict?key1=value1&key2=value2
    # then request.args.keys() will return a list of keys: ["key1", "key2"].
    if key in dictionary.keys():
        value = "  " + dictionary[key]
    else:
        key = "  error"
        value = "  Word not found."
    return render_template("dictionary.html", key = key, value = value)

if __name__ == "__main__":
    app.run(port = 8889) # host="0.0.0.0" will let outer user to access your computer.