import logging
from flask import Flask, request, render_template_string
from datetime import datetime
import json
app = Flask(__name__)
# Logging implementation 0.5
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

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
        <input type="text" id="name" name="name" required><br><br>

        <label for="birthdate">Enter your birthdate (YYYY-MM-DD):</label>
        <input type="date" id="birthdate" name="birthdate" required><br><br>

        <button type="submit">Submit</button>
    </form>
    {% if name and day_of_week %}
        <h2>Hello, {{ name }}! You were born on a {{ day_of_week }}.</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    day_of_week = None
    error = None
    if request.method == 'POST':
        name = request.form['name']
        birthdate = request.form['birthdate']
        try:
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
            day_of_week = birthdate.strftime('%A')
            # log request and saving to json "data.json" - remember about the file
            logging.info(f"Received POST request: name={name}, birthdate={birthdate}")
            data = {'name': name, 'birthdate': birthdate.strftime('%Y-%m-%d'), 'day_of_week': day_of_week}
            with open('data.json', 'a') as f:
                json.dump(data, f)
                f.write('\n')
        except ValueError:
            error = "Invalid date format. Please enter the date in YYYY-MM-DD format."
            logging.error("Invalid date format received.")
    return render_template_string(html_template, name=name, day_of_week=day_of_week, error=error)


if __name__ == '__main__':
    app.run(debug=True)
