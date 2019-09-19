from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/home")    
def indexy():
    return("this helps u in all ways")
@app.route("/contact")    
def indexys():
    return("")    


if(__name__=="__main__"):
    app.run(debug=True)