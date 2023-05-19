# API design
A simple web tool (API) using Python Flask. It connect to a MongoDB database and work with the OpenAI API. It do something helpful for people in sales, marketing, or customer service. For example, API could accept a brief description of a product from a user, use the OpenAI API to generate a compelling sales pitch for that product, store this sales pitch in the MongoDB database, and then present the generated sales pitch back to the user.

### Three parts of the API:
* A GET part to get data from the MongoDB database.
* A POST part to take a user's question, ask the OpenAI API, save the answer in the database, and give the answer back to the user.
* A DELETE part to remove certain data from the MongoDB database.

## Start
1. Clone the code to local and install Flask, openai, and pymongo.
2. Get MongoDB cloud link and replace into code line#9
3. Get OpenAI API keys and replace into code line#14
4. Run python app.py
5. Open postman and play around with http://127.0.0.1:5000/

### GET
Get data from the MongoDB database
After run python app.py, you can get data from the MongoDB in two ways.
1. Query with product id (http://127.0.0.1:5000/product/ with GET function)
<img width="1744" alt="截圖 2023-05-19 11 55 36" src="https://github.com/sianjyunkuo/involve/assets/23247251/d205a76a-a7e3-4c8d-8241-b53af96433ed">
2. Query with product name (http://127.0.0.1:5000/product_name/ wtih GET function)
<img width="1745" alt="2" src="https://github.com/sianjyunkuo/involve/assets/23247251/1cdb870d-dfd3-45df-924a-a8fd4dbeadeb">


### POST
Take a user's question, ask the OpenAI API, save the answer in the database, and give the answer back to the user.
After run python app.py, you can take a user's question by modify the query in request body.
In the postman change link to http://127.0.0.1:50000/product_post with POST function
{
    "question":"query"
}
<img width="1362" alt="post" src="https://github.com/sianjyunkuo/involve/assets/23247251/c57ae0c5-ddc4-4571-abce-c93787d79a7e">
Refresh the mongoDB cloud and check for the new added query.
<img width="1440" alt="mongo" src="https://github.com/sianjyunkuo/involve/assets/23247251/e3e1bb81-0b85-441c-bf99-91ef0f10ab5c">

### DELETE
Remove certain data from the MongoDB database.
After run python app.py, you can remove data from the MongoDB in two ways.
1. Remove data with product id (http://127.0.0.1:5000/product_delete_by_id/ with DELETE function)
<img width="1358" alt="delete1" src="https://github.com/sianjyunkuo/involve/assets/23247251/8473ebf2-1f23-434c-9142-4010d71627c0">
Before delete with product id: 3 (MongoDB screen shot)
<img width="1556" alt="before" src="https://github.com/sianjyunkuo/involve/assets/23247251/a0b15765-a503-444a-a701-d689de43cc32">
After delete with product id: 3 (MongoDB screen shot)
<img width="1567" alt="after" src="https://github.com/sianjyunkuo/involve/assets/23247251/15d5de29-c6cb-45dd-9e9b-9831ca307932">


2. Remove data with product name (http://127.0.0.1:5000/product_delete_by_name/ wtih DELETE function)
<img width="1367" alt="deletebyname" src="https://github.com/sianjyunkuo/involve/assets/23247251/d409cfe9-a695-4d3d-a5e2-c31794def824">
Before delete data with product name: pen (MongoDB screen shot)
<img width="1567" alt="after" src="https://github.com/sianjyunkuo/involve/assets/23247251/7597ad01-16d2-40a0-b687-b5796d568c5c">
After delete data with product name: pen (MongoDB screen shot)
<img width="1151" alt="after2" src="https://github.com/sianjyunkuo/involve/assets/23247251/29acde98-da14-4d94-8439-5b4fbdb251ae">
