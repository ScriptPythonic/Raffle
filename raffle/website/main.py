from flask import Flask, render_template, request, redirect, url_for,jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = 'huuyufyuhfuygyfg hufuuouuyfgyuguiu'  
# Store the admin's winning number
admin_winning_number = 0

@app.route('/raffle', methods=['GET'])
def raffle():
    global admin_winning_number  
    return render_template('raffle.html', winning_number=admin_winning_number)

@app.route('/spin', methods=['GET'])
def spin():
 
    return render_template('index.html')

@app.route('/winning_page')
def winning_page():
    return render_template('winning.html')  # Adjust this route and template as needed

@app.route('/sorry_page')
def sorry_page():
    return render_template('sorry.html') 

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global admin_winning_number  # Access the global admin number

    if request.method == 'POST':
        admin_winning_number = int(request.form['winning_number'])
        redirect(url_for("admin"))

    return render_template('admin.html', winning_number=admin_winning_number)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)

