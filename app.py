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
def get_code_html(text):
    temp_text=""
    for temp in text.split(","):
        temp_text+='<span class="wrap-word">'+temp+'</span>, '
    return temp_text[:-2]
@app.route("/get_question/<int:_type>",methods=["GET"])
def get_question(_type):
    if not _type:
        rand_int=np.random.randint(1,len(df))
        # print(df.head())
        if df.iloc[rand_int,3] is np.nan:
            if df.iloc[rand_int,2] is np.nan :
                print(get_code_html(df.iloc[rand_int, 1]))
                resp = {"result": df.iloc[rand_int, 0].capitalize(),"ans":get_code_html(df.iloc[rand_int, 1]),"desc":"",
                        "synonym": "_"}
            else:
                resp = {"result": df.iloc[rand_int, 0].capitalize(), "ans": get_code_html(df.iloc[rand_int, 1]), "desc": df.iloc[rand_int, 2],
                        "synonym":"_"}
        elif df.iloc[rand_int,2] is np.nan:
            if df.iloc[rand_int,3] is np.nan :
                print(get_code_html(df.iloc[rand_int, 1]))
                resp = {"result": df.iloc[rand_int, 0].capitalize(),"ans":get_code_html(df.iloc[rand_int, 1]),"desc":"",
                        "synonym": "_"}
            else:
                resp = {"result": df.iloc[rand_int, 0].capitalize(), "ans": get_code_html(df.iloc[rand_int, 1]), "desc": df.iloc[rand_int, 2],
                        "synonym":get_code_html(df.iloc[rand_int,3])}

        else:
            resp={"result":df.iloc[rand_int,0].capitalize(),"ans":get_code_html(df.iloc[rand_int,1]),"desc":df.iloc[rand_int,2],"synonym": get_code_html(df.iloc[rand_int,3])}

        # print(resp)
        return jsonify(resp),200

    else:
        rand_int = np.random.randint(1, len(df))
        if df.iloc[rand_int, 3] is np.nan:
            if df.iloc[rand_int, 2] is np.nan:

                resp = {"result": df.iloc[rand_int, 1].capitalize(), "ans": get_code_html(df.iloc[rand_int, 0]), "desc": "",
                        "synonym": "_"}

            else:
                resp = {"result": df.iloc[rand_int, 1].capitalize(), "ans": get_code_html(df.iloc[rand_int, 0]),
                        "desc": df.iloc[rand_int, 2],
                        "synonym": "_"}
        elif df.iloc[rand_int, 2] is np.nan:
            if df.iloc[rand_int, 3] is np.nan:

                resp = {"result": df.iloc[rand_int, 1].capitalize(), "ans": get_code_html(df.iloc[rand_int, 0]),
                        "desc": "",
                        "synonym": "_"}

            else:
                resp = {"result": df.iloc[rand_int, 1].capitalize(), "ans": get_code_html(df.iloc[rand_int, 0]),
                        "desc": "",
                        "synonym": get_code_html(df.iloc[rand_int, 3])}
        else:
            resp = {"result": df.iloc[rand_int,1].capitalize(), "ans": get_code_html(df.iloc[rand_int, 0]),
                    "desc": df.iloc[rand_int, 2], "synonym": get_code_html(df.iloc[rand_int, 3])}

        # print(resp)
        return jsonify(resp), 200



if __name__=="__main__":
    # app.run("localhost","2100",debug=True)
    app.run()