from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


def top5():
    return render_template('top5.html')
app.add_url_rule("/top5","top5", top5)

def top4():
    return render_template('top4.html')
app.add_url_rule("/top4","top4", top4)

def top3():
    return render_template('top3.html')
app.add_url_rule("/top3","top3", top3)

def top2():
    return render_template('top2.html')
app.add_url_rule("/top2","top2", top2)

def top1():
    return render_template('top1.html')
app.add_url_rule("/top1","top1", top1)

def agradecimentos():
    return render_template('agradecimentos.html')
app.add_url_rule("/agradecimentos","agradecimentos", agradecimentos)


if __name__ == "__main__":
    app.run(debug=True)