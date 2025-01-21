from flask import Flask, render_template, request, redirect, send_file
import csv
import os

app = Flask(__name__)

CSV_FILE = "data/professions.csv"

@app.route('/')
def index():
    professions = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            professions.append({'name': row[0], 'selected': row[1] == 'True'})
    return render_template('index.html', professions=professions)

@app.route('/update', methods=['POST'])
def update():
    selected = request.form.getlist('selected')
    updated_rows = []

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row[1] = 'True' if row[0] in selected else 'False'
            updated_rows.append(row)

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(updated_rows)

    return send_file(CSV_FILE, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
