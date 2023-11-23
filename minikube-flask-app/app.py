import pickle
from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route("/", methods=["GET"])
def say_hello():
    return render_template("prediction.html")


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        Stock_Price = float(request.form['Stock_Price'])
        Profit = float(request.form['Profit'])
        Revenue = float(request.form['Revenue'])
        Budget_Allocation = float(request.form['Budget_Allocation'])
        Market_Demand = request.form['Market_Demand']
        Sales_Forecast = request.form['Sales_Forecast']
        Strategic_Initiatives = request.form['Strategic_Initiatives']
        Employee_Attrition = request.form['Employee_Attrition']
        Workload = request.form['Workload']
        input_data = pd.DataFrame({
            'Stock_Price': [Stock_Price],
            'Profit': [Profit],
            'Revenue': [Revenue],
            'Budget_Allocation': [Budget_Allocation],
            'Market_Demand': [Market_Demand],
            'Sales_Forecast': [Sales_Forecast],
            'Strategic_Initiatives': [Strategic_Initiatives],
            'Employee_Attrition': [Employee_Attrition],
            'Workload': [Workload]
        })

        prediction = model.predict(input_data)

        return render_template('prediction.html', prediction=int(prediction[0]))
    
    return render_template('prediction.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)