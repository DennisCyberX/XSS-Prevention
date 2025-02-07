from flask import Flask, request, render_template, escape
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Secure: Escape user input to prevent XSS
        safe_input = escape(user_input)
        return render_template('result.html', user_input=safe_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
