import pymongo
import openai
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection initialize
db = cluster["store"]
collections = db["pitch"]

# openai gpt-3.5 API initialize
openai.api_key = OpenAI_API_KEY
model_id = 'gpt-3.5-turbo'
query = ""
conversation = []

@app.route("/")
def home():
    return "home page"

#--POST--
# A POST part to take a user's question, ask the OpenAI API, save the answer in the database, and give the answer back to the user.
@app.route('/product_post', methods=["POST"])
def product_post():
    # get user question
    req_Json = request.json
    question = req_Json['question']

    # request to openAI gpt-3.5
    query = "how to sale: " + question
    conversation.append({'role': 'system', 'content': query})
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation
    )
    # get the answer and save to pitch
    pitch = response.choices[-1].message.content

    # save answer in MongoDB
    name = question
    descript = query
    post_to_db = {"name": name, "description": descript, "pitch": pitch}
    collections.insert_one(post_to_db)

    # give answer back to customer
    return jsonify({"response": pitch})

# --GET--
# A GET part to get data from the MongoDB database.
# Get data by query product id
@app.route("/product/<int:product_id>")
def product_page(product_id):
    results = collections.find({"_id":product_id})
    return jsonify(results[0])

# Get data by query product name
@app.route("/product_name/<string:product_name>")
def product_name(product_name):
    results = collections.find({"name":product_name})
    return jsonify(results[0])

# --DELETE--
# A DELETE part to remove certain data from the MongoDB database.
# Delete data by product id
@app.route("/product_delete_by_id/<int:product_id>", methods=["DELETE"])
def product_delete_id(product_id):
    results = collections.delete_one({"_id":product_id})
    return jsonify({"response": "delete product success"})

# Delete data by product name
@app.route("/product_delete_by_name/<string:product_name>", methods=["DELETE"])
def product_delete_name(product_name):
    results = collections.delete_one({"name":product_name})
    return jsonify({"response": "delete product success"})



if __name__ == '__main__':
    app.run(port=5000)
