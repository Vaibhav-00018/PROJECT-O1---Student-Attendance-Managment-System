from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    return conn

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]

        conn = get_db()
        conn.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template("add_student.html")

@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()

    if request.method == "POST":
        for student in students:
            status = request.form.get(str(student[0]))

            conn.execute(
                "INSERT INTO attendance (student_id, status) VALUES (?, ?)",
                (student[0], status)
            )

        conn.commit()
        conn.close()
        return redirect("/dashboard")

    return render_template("attendance.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)