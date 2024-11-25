from flask import Flask, render_template, request
from markupsafe import escape
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/companyInfo', methods=['POST', 'GET'])
def company_results():
    if request.method == 'POST':
          

        ticker = request.form['ticker']
        startYear = request.form['start_year']
        endYear = request.form['end_year']


        stock = yf.Ticker(ticker)
        #start = str(startYear) + "-01-01"

        data = stock.history(start=f"{startYear}-01-01", end=f"{endYear}-12-31")
        info = stock.info


        return render_template('companyInfo.html', ticker=escape(ticker), data=data.to_html(), info=info)

    return render_template('index.html')



@app.route('/branchInfo', methods=['POST'])
def branch_results():


        sectorName = request.form['sectors']
        print('========= TEST 1 ========')
        print('sector_name ' + sectorName)
        sectorInfo = yf.Sector(sectorName)
        #sectorList = sectorInfo.top_companies

        return render_template('branchInfo.html', sectorName=sectorInfo.name, sectorOverview=sectorInfo.overview, sectorList=(sectorInfo.top_companies).to_html())
        

if __name__ == '__main__':
    app.run(debug=True)
