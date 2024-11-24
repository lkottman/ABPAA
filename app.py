from flask import Flask, render_template, request
from markupsafe import escape
import yfinance as yf

app = Flask(__name__)

# Route for displaying the form
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Route for processing form data
@app.route('/companyInfo', methods=['POST', 'GET'])
def company_results():
    if request.method == 'POST':
          
        #input
        ticker = request.form['ticker']
        start_year = request.form['start_year']
        end_year = request.form['end_year']

        # get data from yfinance
        stock = yf.Ticker(ticker)
        data = stock.history(start=f"{start_year}-01-01", end=f"{end_year}-12-31")
        info = stock.info

        print('========= TEST 1 ========')
        print(info)
       
        #print('info dir ' + dir(info))
        ##sector = info.get('sector', 'Unknown')

        # Render the result page with data and stock information
        return render_template('companyInfo.html', ticker=escape(ticker), data=data.to_html(), info=info)

        ##return render_template('result.html', ticker=escape(ticker), data=data.to_html(), sector=sector)
    return render_template('index.html')



@app.route('/branchInfo', methods=['POST'])
def branch_results():

            #sector_key = request.form.get('sector_key', 'technology')
            #sector = yf.Sector(sector_key)
            #branch = yf.Sector('technology')
            #print('========= TEST ========')
            #print(branch)

        sector_name = request.form['sectors']
        sector_name1 = request.form.get('sector_key', 'energy')
        print('========= TEST 1 ========')
        print('sector_name ' + sector_name)
        print('sector_name1 ' + sector_name1)
        sector = yf.Sector(sector_name)
        software = yf.Industry('software-infrastructure')

        # Common information
        #tech.key
        #tech.name
        #tech.symbol
        #tech.ticker
        sectorN = sector.name
        sectorO = sector.overview
        sectorList = sector.top_companies
        #sectorD = sectorO['description']
        sectorD = 'Wildcard'
        #tech.research_reports

        # Sector information
        #tech.top_etfs
        #tech.top_mutual_funds
        #tech.industries

        #print('========= TEST 2 ========')
        #äprint(sectorN)
        #print(f"Name: {techo['description']}")
        return render_template('branchInfo.html', sectorName=sector.name, sectorOverview=sector.overview, sectorList=sectorList.to_html())
        

if __name__ == '__main__':
    app.run(debug=True)
