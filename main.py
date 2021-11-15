from flask import Flask, json, jsonify, make_response, render_template
import helper
import datetime
app = Flask(__name__,  template_folder='./')

@app.route('/')
def main_page():
    bitcoin_response = helper.generate_response('bitcoin')
    ethereum_response = helper.generate_response('ethereum')
    current_time = datetime.datetime.now().strftime('%m-%d-%y %H:%M:%S')
    print(current_time)
    return render_template('table_view.html', bitcoin_response = bitcoin_response, ethereum_response = ethereum_response, current_time=current_time)

@app.route('/about')
def about_page():
    return render_template('about_page.html')

if __name__ == '__main__':
    app.run(debug=True)
