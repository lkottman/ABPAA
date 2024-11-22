from flask import Flask, render_template, request
from markupsafe import escape
import yfinance as yf

app = Flask(__name__)

# Route for displaying the form
@app.route('/', methods=['GET'])
def show_form():
    return render_template('index.html')

# Route for processing form data
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
          
        #input
        ticker = request.form['ticker']
        start_year = request.form['start_year']
        end_year = request.form['end_year']

        # get data from yfinance
        stock = yf.Ticker(ticker)
        data = stock.history(start=f"{start_year}-01-01", end=f"{end_year}-12-31")
        info = stock.info

        ##sector = info.get('sector', 'Unknown')

        # Render the result page with data and stock information
        return render_template('result.html', ticker=escape(ticker), data=data.to_html(), info=info)

        ##return render_template('result.html', ticker=escape(ticker), data=data.to_html(), sector=sector)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
