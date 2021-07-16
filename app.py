import time

from flask import Flask,render_template,jsonify
import pandas as pd
import numpy as np
import warnings
# warnings.filterwarnings(action="ignore")
app = Flask(__name__)
df=pd.read_excel("assets/Words_dictionary.xls",header=0)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/get_question/<int:_type>",methods=["GET"])
def get_question(_type):
    if not _type:
        rand_int=np.random.randint(1,len(df))
        # print(df.head())
        if df.iloc[rand_int,2] is np.nan or df.iloc[rand_int,3] is np.nan:
            if df.iloc[rand_int,2] is np.nan :
                resp = {"result": df.iloc[rand_int, 0].capitalize(),"ans":df.iloc[rand_int, 1],"desc":"",
                        "synonym": df.iloc[rand_int,3]}
            else:
                resp = {"result": df.iloc[rand_int, 0].capitalize(), "ans": df.iloc[rand_int, 1], "desc": df.iloc[rand_int, 2],
                        "synonym":"_"}

        else:
            resp={"result":df.iloc[rand_int,0].capitalize(),"ans":df.iloc[rand_int,1],"desc":df.iloc[rand_int,2],"synonym": df.iloc[rand_int,3]}
        time.sleep(1)
        # print(resp)
        return jsonify(resp),200

    else:
        rand_int = np.random.randint(1, len(df))
        # print(df.head())
        if df.iloc[rand_int, 2] is np.nan or df.iloc[rand_int, 3] is np.nan:
            if df.iloc[rand_int, 2] is np.nan:
                resp = {"result": df.iloc[rand_int, 1].capitalize(), "ans": df.iloc[rand_int, 0], "desc": "",
                        "synonym": df.iloc[rand_int, 3]}

            else:
                resp = {"result": df.iloc[rand_int, 1].capitalize(), "ans": df.iloc[rand_int, 0],
                        "desc": df.iloc[rand_int, 2],
                        "synonym": "_"}


        else:
            resp = {"result": df.iloc[rand_int,1].capitalize(), "ans": df.iloc[rand_int, 0],
                    "desc": df.iloc[rand_int, 2], "synonym": df.iloc[rand_int, 3]}
        time.sleep(1)
        # print(resp)
        return jsonify(resp), 200



if __name__=="__main__":
    # app.run("localhost","2100",debug=True)
    app.run()