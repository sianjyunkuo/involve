# API design
A simple web tool (API) using Python Flask. It connect to a MongoDB database and work with the OpenAI API. It do something helpful for people in sales, marketing, or customer service. For example, API could accept a brief description of a product from a user, use the OpenAI API to generate a compelling sales pitch for that product, store this sales pitch in the MongoDB database, and then present the generated sales pitch back to the user.

### Three parts of the API:
A GET part to get data from the MongoDB database.
A POST part to take a user's question, ask the OpenAI API, save the answer in the database, and give the answer back to the user.
A DELETE part to remove certain data from the MongoDB database.