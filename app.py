from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note is None or not note.strip():  # Check if note is None or empty after stripping whitespace
            notes.append('None')  # Append 'None' if no text is entered
        else:
            notes.append(note)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
