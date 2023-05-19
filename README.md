# API design
A simple web tool (API) using Python Flask. It connect to a MongoDB database and work with the OpenAI API. It do something helpful for people in sales, marketing, or customer service. For example, API could accept a brief description of a product from a user, use the OpenAI API to generate a compelling sales pitch for that product, store this sales pitch in the MongoDB database, and then present the generated sales pitch back to the user.

### Three parts of the API:
* A GET part to get data from the MongoDB database.
* A POST part to take a user's question, ask the OpenAI API, save the answer in the database, and give the answer back to the user.
* A DELETE part to remove certain data from the MongoDB database.

## Start
1. Clone the code to local
2. Get MongoDB cloud link and replace into code line#9
3. Get OpenAI API keys and replace into code line#14
4. Run python app.py
5. Open postman and play around with http://127.0.0.1:50000/

### GET
Get data from the MongoDB database
After run python app.py, you can get data from the MongoDB in two ways.
1. Query with product id (http://127.0.0.1:5000/product/ with GET function)
2. Query with product name (http://127.0.0.1:5000/product_name/ wtih GET function)


### POST
Take a user's question, ask the OpenAI API, save the answer in the database, and give the answer back to the user.
After run python app.py, you can take a user's question by modify the query in request body.
In the postman change link to http://127.0.0.1:50000/product_post with POST function
{
    "question":"query"
}

### DELETE
Remove certain data from the MongoDB database.
After run python app.py, you can remove data from the MongoDB in two ways.
1. Remove data with product id (http://127.0.0.1:5000/product_delete_by_id/ with DELETE function)
2. Remove data with product name (http://127.0.0.1:5000/product_delete_by_name/ wtih DELETE function)