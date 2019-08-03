from flask import Flask, render_template, request, redirect, url_for, flash
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# firebase connection
cred = credentials.Certificate({
  #key files firebase.json
})

firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
#settings
app.secret_key = "mysecretkey"
 

@app.route("/")
def home():
    contact_directoriy= []
    
    contact_list = db.collection(u'contacts')
    data = contact_list.get()

    #iterate on documents and their different values
    for index in data:
        save = index.to_dict()
        contact_directoriy.append(save)

    #print("\n diccionary list: {}".format(contact_directoriy) ,"\n")
    return render_template("index.html", contacts_html = contact_directoriy )


@app.route("/add", methods = ["POST"])
def add_contact():

    fullname = request.form["fullname"]
    phone = request.form["phone"]
    email = request.form["email"]

    data = {
    u'name': fullname,
    u'phone': phone,
    u'email': email
    }

    try:
      db.collection(u"contacts").document(fullname).set(data)
      flash("Contact successfuly added")
    except:
      flash("The name field was not entered")
      return redirect(url_for("home"))

    print("\n Contact {} successfully added \n".format(data["name"]))
    return redirect(url_for("home"))


@app.route("/del/<id>")
def delete_contact(id):

    db.collection(u'contacts').document(id).delete()

    flash("Contact successfuly delete")

    print("\n Contact {} successfully delete\n".format(id))
    return redirect(url_for("home"))


@app.route("/edit/<id>")
def get_contact(id):

    contact_directoriy= []
    
    id_save = db.collection(u'contacts').document(id)
    doc = id_save.get().to_dict()

    contact_directoriy.append("{}".format(doc["name"]))
    contact_directoriy.append("{}".format(doc["phone"]))
    contact_directoriy.append("{}".format(doc["email"]))

    return render_template("update.html", contact = contact_directoriy)


@app.route("/update/<id>", methods = ["POST"])
def update_contact(id):

    fullname = request.form["fullname"]
    phone = request.form["phone"]
    email = request.form["email"]

    data = {
    #u'name': fullname, #error no es posible actualizar la id del documento firebase  
    u'phone': phone,
    u'email': email
    }

    db.collection(u"contacts").document(id).update(data)

    flash("Contact successfuly update")

    print("\n Contact {} successfully update \n".format(id))
    return redirect(url_for("home"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(port = 3000, debug=True)