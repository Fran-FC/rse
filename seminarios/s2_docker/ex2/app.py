from flask import Flask, render_template
import random

app = Flask(__name__)

# Breakfast Pizzas That Want To Wake Up Next To You
# https://www.buzzfeed.com/rachelysanders/good-morning-pizza
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-07/22/13/enhanced/webdr10/enhanced-buzz-12910-1406051649-8.jpg","https://img.buzzfeed.com/buzzfeed-static/static/2014-07/22/14/enhanced/webdr02/enhanced-buzz-1275-1406053174-20.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    # 'flask run --host=0.0.0.0' tells your operating system to listen on all public IPs.
    app.run(host="0.0.0.0")

    
