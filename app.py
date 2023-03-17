import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        place = request.form.get("place")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(place),
            temperature=0.4,
        )        
        return redirect(url_for("index", result=response.choices[0].text, place=place ))
    
    place = request.args.get("place") 
    result = request.args.get("result")

    return render_template("index.html", result=result, place=place)


def generate_prompt(place):
    return """Cool hangout locations in Kenya:
Amboseli National Park,Lake Victoria,Nairobi,
MtKenya National Park,Mombasa,Malindi
""".format(
        place.capitalize()
    )
