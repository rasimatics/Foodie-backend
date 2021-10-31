# Foodie-backend
  
This is example of food ordering system.

  **P.S**: This website is not for a real company. Inspired from different ecommerce projects to design and build it.

  ### Website Features:
  
  - User register/login with JWT token
  - Foods with different categories
  - User create/update/delete an order for products
  - Permission checking for modifying orders
    
    
  ### Technologies used in developement
   Back-end Rest Api:
   - Django
   - Django Rest Framework
  
    
  
  ### Installation
  
   In order to run the application in local environment follow instructions below:
  
  ```bash
  # clone
  git clone https://github.com/rasimatics/Foodie-backend.git
  
  cd Foodie-backend
  
  virtualenv venv
  
  source venv/bin/activate
  
  pip install -r requirements.txt
  
  python manage.py migrate
  
  python manage.py runserver

  ```
  
