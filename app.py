from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        phNumber = request.form.get('phno')
        message = request.form.get('msg').title()
        return redirect(f'https://api.whatsapp.com/send/?phone=91{phNumber}&text={message}')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
