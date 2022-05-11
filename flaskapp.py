from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Contact": "9876543210",
        "Name": "Bella",
        "done": False, 
        "id" : 1
    },
    {
        "Contact": "6475364873",
        "Name": "Harry",
        "done": False,
        "id": 2
    }
]

@app.route("/add-contact", methods = ["POST"])

def add_contact():
    if(not request.json):
        return jsonify({
            "status": 'error',
            'message': 'Please provide data'
        }, 400)
    contact_list = {
        "id": contacts[-1]["id"] + 1,
        "Name": request.json['Name'],
        "Contact": request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact_list)
    return jsonify({
        "status": "success",
        "message": "task added successfully"
    })

@app.route("/get-contact")
def get_contact():
    return jsonify({
        "data": contacts
    })

if(__name__ == "__main__"):
    app.run(debug = True)