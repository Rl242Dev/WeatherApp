from flask import Flask, render_template, request
from csv import reader

#TODO: If we can't find the city then return error message

def parse_data(city: str) -> list:
    with open('data.csv', "r") as data:
        readers = reader(data)
        for row in readers:
            if row[7] == city:
                return row
        return None

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/", methods=['POST', 'GET'])
def index():
    if(request.form.get("city-input") == None or request.form.get("city-input") == ""):
        pass
        return render_template("index.html", temperature="--", wind_speed="--", visibility="--", humidity="--", error="")
    else:
        data = parse_data(request.form.get("city-input"))
        if data == None:
            data = ["0", "0", "0", "0", "0","City was not found"]
        return render_template("index.html", temperature=data[0]+"°C", wind_speed=data[3]+" km/h", visibility=data[4]+" km", humidity=data[2]+"%", error=data[5])

if __name__ == "__main__":
    app.run()