from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<h1>HELLO FLASK</h1>"

# GET /hello/<name> -> <h1>Hello Name</h1>
@app.route("/hello/<name>")
def hello_someone(name):
    return {"name": name, "message": f"Hello {name}", "country": "TW"}

# GET /hello_2?name=Allen&dep_id=001
@app.route("/hello_2")
def hello_2():
    name = request.args.get("name")
    dep_id = request.args.get("dep_id")

    return {
        "name": name,
        "department": dep_id,
        "message": f"Hello {name}"
    }


@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <html>
    <form action="/hello_post" method="POST">
        <label>What is your name?</label>
        <br>
        <input type="textbox" name="username">
        <button type="submit">Submit</button>
    </form>
    <div>
    %s
    </div>
    </html>
    """
    if request.method == 'GET':
        return outStr%('')
    elif request.method == 'POST':
        username = request.form.get('username')
        return outStr%('Hello %s'%(username))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
