#required modules
from flask import Flask, render_template, request
import main

#initialize object of Flask class
app = Flask(__name__)

#new route for entering point of application
@app.route("/scraper", methods=['GET','POST'])
def welcome():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        keyword = request.form['keyword']
        azn_df = main.azn_product_df(keyword)
        fpt_df = main.fpt_product_df(keyword)
        print(azn_df)
        print(fpt_df)

        if azn_df.empty == False and fpt_df == False:
            azn_name1 = azn_df.iloc[0,0]
            azn_price1 = azn_df.iloc[0,1]
            azn_image1 = azn_df.iloc[0,2]
            azn_name2 = azn_df.iloc[1,0]
            azn_price2 = azn_df.iloc[1,1]
            azn_image2 = azn_df.iloc[1,2] 
            

            fpt_name1 = fpt_df.iloc[0,0]
            fpt_price1 = fpt_df.iloc[0,1]
            fpt_image1 = fpt_df.iloc[0,2]
            fpt_name2 = fpt_df.iloc[1,0]
            fpt_price2 = fpt_df.iloc[1,1]
            fpt_image2 = fpt_df.iloc[1,2]

            return render_template('prices.html', azn_p1_image = azn_image1, azn_p1_name = azn_name1, azn_p1_price = azn_price1, azn_p2_image = azn_image2, azn_p2_name = azn_name2, azn_p2_price = azn_price2,fpt_p1_image = fpt_image1, fpt_p1_name = fpt_name1, fpt_p1_price = fpt_price1, fpt_p2_image = fpt_image2, fpt_p2_name = fpt_name2, fpt_p2_price = fpt_price2)
        else:
            return render_template('service.html')

if __name__=="__main__":
    app.run(debug=True)