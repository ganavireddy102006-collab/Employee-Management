from flask import Flask,request,jsonify
app=Flask(__name__)
Employee=[{"id":1,
           "name":"Rahul"},
           {"id":2,
            "name":"Ravi"}]

@app.route("/Employee",methods=["GET"])
def get_employees():
    return jsonify(Employee)
@app.route("/Employee",methods=["POST"])
def add_employees():
    data=request.get_json()
    new_employee={"id":len(Employee)+1,"name":data["name"]}
    Employee.append(new_employee)
    return jsonify(new_employee),201
if __name__=="__main__":
    app.run(debug=True)