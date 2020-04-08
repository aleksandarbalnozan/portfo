from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_database_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'


def save_database_csv(data):
    with open('./database.csv', mode='a', newline='\n') as db_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db_csv, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# def save_database(data):
#     with open('./database.txt', 'a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         db.write(
#             f'Email from: {email}\nSubject: {subject}\nMessage:\n\t{message}\n')
