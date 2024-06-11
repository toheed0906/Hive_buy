# Buy Hive - E-Commerce PlatForm

## Description
Buy-hive is a ecommerce platform which is built using django, django-rest-framework , postgreSQL, Vue3,  and Vuex
The features of the project include
1. Filtering the products based on the category , sub cateory , minimum price, maximum price, minimum order quantity and location of the manufactuer
2. Searching Based on the product name
3. Ordering based on the relevance, price high to low, price low to high, minimum order qunatity low to high , latest and supplier rating
4. Pagination based on the page numebr and cursor

## User Interface
   ![Main - Product - Page](https://github.com/toheed0906/Hive_buy/assets/171033097/1050399b-b493-4b3f-b72b-74946537cbca)
   ![2](https://github.com/toheed0906/Hive_buy/assets/171033097/e7be332a-7054-4c23-8b12-105dad2697b6)


## How to run the project
  ###  1. clone the project 
  ###  2. install the dependencies using requirements.txt

         pip install -r requirements.txt
  ### 3. Setup the env file (backend)
         #Chnage the db_name , db_user and db_password according to yours
         DB_NAME = 'buyhive_db'
         DB_USER = 'myprojectuser'
         DB_PASSWORD = 'password'

  ### 4. Setup the env file (frontend)
         VUE_APP_ROOT_API= http://127.0.0.1:8000/products/
         CATEGORY_URL = http://127.0.0.1:8000/categories/
  ### 5. Open the folder in code editor
  ### 6. Cd into backend and run command
         python3 manage.py runserver
  ### 7. Cd into frontend and run command 
         npm run serve

  

