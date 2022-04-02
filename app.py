from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        phno = request.form.get('phno')
        msg = request.form.get('msg').title()
        return redirect(f'https://api.whatsapp.com/send/?phone=91{phno}&text={msg}')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
