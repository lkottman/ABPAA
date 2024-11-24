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
        start_year = request.form['start_year']
        end_year = request.form['end_year']


        stock = yf.Ticker(ticker)
        data = stock.history(start=f"{start_year}-01-01", end=f"{end_year}-12-31")
        info = stock.info

        print('========= TEST 1 ========')
        print(info)

        return render_template('companyInfo.html', ticker=escape(ticker), data=data.to_html(), info=info)

    return render_template('index.html')



@app.route('/branchInfo', methods=['POST'])
def branch_results():


        sector_name = request.form['sectors']
        sector_name1 = request.form.get('sector_key', 'energy')
        print('========= TEST 1 ========')
        print('sector_name ' + sector_name)
        print('sector_name1 ' + sector_name1)
        sector = yf.Sector(sector_name)
        sectorList = sector.top_companies

        return render_template('branchInfo.html', sectorName=sector.name, sectorOverview=sector.overview, sectorList=sectorList.to_html())
        

if __name__ == '__main__':
    app.run(debug=True)
