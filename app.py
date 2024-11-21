from flask import Flask, render_template, request
from markupsafe import escape
import yfinance as yf

app = Flask(__name__)

# Route for displaying the form
@app.route('/', methods=['GET'])
def show_form():
    return render_template('index.html')

# Route for processing form data
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Finance</title>
</head>
<body>
    <form>
        <label for="ticker">Ticker:</label>
        <input type="text" id="ticker" name="ticker" placeholder="z.B. AAPL" required><br><br>
 
        <label for="start_year">Start Year:</label>
        <input type="text" id="start_year" name="start_year" placeholder="z.B. 2020" required><br><br>
 
        <label for="end_year">End Year5:</label>
        <input type="text" id="end_year" name="end_year" placeholder="z.B. 2021" required><br><br>
 
        <button type="submit">get</button>
    </form>
</body>
</html>
            
        #input
        ticker = request.form['ticker']
        start_year = request.form['start_year']
        end_year = request.form['end_year']

        # get data from yfinance
        stock = yf.Ticker(ticker)
        data = stock.history(start=f"{start_year}-01-01", end=f"{end_year}-12-31")
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <title>Finance Data Results</title>
</head>
<body class="bg-light">
    <div class="container d-flex flex-column justify-content-center align-items-center vh-100">
        <h1 class="text-center mb-4">Results for {{ ticker }} from </h1>
        <h2 class="text-center mb-4">Basisinformation</h2>
        <ul>
            <li>Company name: {{ info['longName'] }}</li>
            <li>Market capitalization: {{ info['marketCap'] }}</li>
            <li>Sector: {{ info['sector'] }}</li>
            <li>Country: {{ info['country'] }}</li>
            <li>Website: {{ info['website'] }}</a></li>
        </ul>
        <h2 class="text-center mb-4">Financial data for {{ ticker }} from </h1>
        <div class="table-responsive">
            {{ data |safe }}
        </div>
        <a href="/">Zurück zur Eingabe</a>
    </div>
</body>
</html>

        ##sector = info.get('sector', 'Unknown')

        # Render the result page with data and stock information
        return render_template('result.html', ticker=escape(ticker), data=data.to_html())

        ##return render_template('result.html', ticker=escape(ticker), data=data.to_html(), sector=sector)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
