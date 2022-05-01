from flask import Flask,redirect,render_template
# Importing Flask Modules

app = Flask(__name__)
# Define App 


"""Route and Function"""
@app.route('/')
def index():
    return "Hello , World! <br> I'm <b>Numan</b> and How are You! <b>DEAR</b>"



# Excution Section
if __name__=="__main__":
    app.run(debug=True)

