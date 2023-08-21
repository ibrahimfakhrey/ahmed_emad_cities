from flask import Flask,render_template,request,redirect
app=Flask(__name__)

data={"ahmed":"1"}

cities={
"ahmed":[ {"paris":3,"cairo":2 }]

}
pricies={
    "paris":20,
    "cairo":10,
    "usa":100,"canada":200
}
@app.route("/")
def start():

    return render_template("index.html")


@app.route("/login",methods=["GET","POST"])
def log ():
    if request.method =="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        print(data)
        for i in data:
            if i ==name and data[i]==password:
                for c in cities:
                    if c==name:
                        cities_visited=cities[c][0]


                        return render_template("loggedin.html",user_name=i,city=cities_visited)
        else:
            return "sorry but somthing went wrong"
    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request. method =="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        data[name]=password
        return redirect("/login")
    return render_template("register.html")

if __name__==("__main__"):
    app.run(debug=True)