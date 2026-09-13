from flask import Flask, render_template, request

app = Flask(__name__)

answers = {
    "q1" : "a",
    "q2" : "c",
    "q3" : "b",
    "q4" : "d",
    "q5" : "a",
    "q6" : "c",
    "q7" : "d",
    "q8" : "b"
}

@app.route("/", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template("page.html")
    
    score = 0

    for question, cor_ans in answers.items():
        usr_ans = request.form.get(question)
        if usr_ans == cor_ans:
            score += 1

    percentage = score / len(answers) * 100
    return render_template("result.html", percentage=percentage, score=score)
