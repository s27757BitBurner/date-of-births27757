from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the web page
html_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Greeting App</title>
</head>
<body>
    <h1>Greeting App</h1>
    <form method="post" action="/">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Say Hello</button>
    </form>
    {% if name %}
        <h2>Hello, {{ name }}!</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template_string(html_template, name=name)

if __name__ == '__main__':
    app.run(debug=True)
