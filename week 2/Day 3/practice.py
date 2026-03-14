import requests
import json

def practice():

    # response = requests.get("https://jsonplaceholder.typicode.com/users")

    # if response.status_code == 200:
    #     print("Success")
    #     data = response.json()
    #     with open("Week 2/Day 3/response.json", "w") as file:
    #         writer = json.dump(data, file, indent = 4)
    #     print(data[0]['name'])

    # else:
    #     print(f"Error status: {response.status_code}")

    #Exercise 1.1: First API Call

 
# # Use JSONPlaceholder (fake API for testing)
#     url = "https://jsonplaceholder.typicode.com/posts/1"
 
# # # YOUR TASK:
# # # 1. Make a GET request
#     response = requests.get(url)
#     if response.status_code == 200:
# # # 2. Print the status code
#         print(f"Success: {response.status_code}")
# # # 3. Print the JSON response
#         data = response.json()
#         print(data)
# # # 4. Access and print the 'title' field
#         print(data['title'])

# #Exercise 1.2: Get Multiple Items
 
#     url = "https://jsonplaceholder.typicode.com/posts"
 
# # # YOUR TASK:
# # # 1. Get all posts
#     response = requests.get(url)
#     if response.status_code ==200:
#         data = response.json()
# # # 2. Print how many posts there are
#         print(len(data))
# # # 3. Print titles of first 5 posts
#         for row in data:
#             if row['id'] <=5:
#                 print(row)
# # # 4. Find the post with id=10
#             if row['id'] == 10:
#                 print(row)
# Exercise 1.3: Using Parameters
# import requests
 
#     url = "https://jsonplaceholder.typicode.com/comments"
 
# # # YOUR TASK:
# # # 1. Get comments for postId=1 using params
#     params = {
#         "postId": 1
#     }

#     response = requests.get(url, params = params)
#     if response.status_code == 200:
#         print(f"Success: {response.status_code}")
#         data = response.json()
#         print(data)
# # # 2. Print how many comments
#         print(len(data))
# # # 3. Print email of each commenter
#         for email in data:
#             print(email['email'])
# Exercise Set 2: Error Handling (20 minutes)
# Exercise 2.1: Handle 404
# import requests
 
#     url = "https://jsonplaceholder.typicode.com/posts/99999"
 
# # # YOUR TASK:
# # # 1. Try to get this post (doesn't exist)
#     response = requests.get(url)
# # # 2. Check the status code
#     try:
#         if response.status_code == 200:
#             print("Post found!")
#         else:
#             print(f"Error: {response.status_code}")
#     except requests.exceptions.HTTPError as e:
#         print(f"Data not found : {e}")

# # 3. Print appropriate message for 404
# Exercise 2.2: Timeout Handling
# import requests
 
    #url = "https://jsonplaceholder.typicode.com/posts"
 
# YOUR TASK:
# 1. Make request with timeout=0.001 (very short)
    #response = requests.get(url, timeout = 0.001)
# 2. Handle the timeout exception
# 3. Retry with longer timeout
    # try:
    #     response = requests.get(url, timeout=0.001)
    
    # # Check if successful
    #     response.raise_for_status()  # Raises exception for 4xx/5xx
    
    #     data = response.json()
    #     print(data)
    
    # except requests.exceptions.Timeout:
    #     print("Request timed out!")
# Exercise 2.3: Complete Error Handler
# import requests
 
#     def safe_api_call(url):
#         """Make API call with complete error handling"""
#         try:
#             response = requests.get(url, timeout=10)
        
#         # 1. Check if the HTTP status is 200-299 FIRST
#             response.raise_for_status()
        
#         # 2. Only if successful, try to parse the JSON
#             return response.json()

#         except requests.exceptions.Timeout:
#             print("Timeout error: The server took too long.")
#         except requests.exceptions.ConnectionError:
#             print("Connection error: DNS issue or no internet.")
#         except requests.exceptions.HTTPError as e:
#             print(f"HTTP error: {e}")
#         except Exception as e:
#             print(f"Unexpected error: {e}")

#     # 3. If any exception happened, we fall through to here
#         #return None
#     # YOUR TASK:
#         # try:
#         #     response = requests.get(url,timeout=10)
            
#         #     response.raise_for_status()

#         #     return response.json()
            
#     # Handle: Timeout, ConnectionError, HTTPError
#         # except requests.exceptions.ConnectionError as e:
#         #     print(f"Connection not established: {e}")
#         # except requests.exceptions.HTTPError as e:
#         #     print(f"HTTP error: {e}")
#         # except requests.exceptions.Timeout as e:
#         #     print(f"Timout error: {e}")
#     # Return data or None
#         #return None
        
 
# # # Test it
#     result = safe_api_call("https://jsonplaceholder.typicode.com/users")
# Exercise Set 3: Working with Real APIs (30 minutes)
# Exercise 3.1: Free Weather API
# import requests
 
# # Using wttr.in (no API key needed!)
    #url = "https://wttr.in/Boston?format=j1"
 
# # YOUR TASK:
# # 1. Get weather for your city
   
 
# # YOUR TASK:
# # 1. Get weather for your city
#     try:
#         response = requests.get(url)
#         response.raise_for_status()

# # # 2. Parse the JSON
#         data = response.json()
# # # 3. Print current temperature
#         for row in data:
#             print(row)
# # # 4. Print weather description
#     except Exception as e:
#         print(f"Error found: {e}")
# Exercise 3.2: Exchange Rates
# import requests
 
# # Using exchangerate-api (free, no key needed for basic)
#     url = "https://api.exchangerate-api.com/v4/latest/USD"
 
# # # YOUR TASK:
# # # 1. Get exchange rates
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         if response.status_code == 200:
#             data = response.json()
#             #print(data['rates'])
                
# # # 2. Print rate for EUR, GBP, JPY
#         content = data['rates']
#         target = ["EUR", "GBP", "JPY"]
#         for k in content:
#             if k in target:
#                 print(content[k])
# # # 3. Convert $100 to EUR
#     except Exception as e:
#         print(f"Error: {e}")
# #Exercise 3.3: Random User Generator
# import requests
 
    url = "https://randomuser.me/api/"
 
# # YOUR TASK:
# # 1. Get 5 random users (hint: ?results=5)
    try:
       response = requests.get(url)
       response.raise_for_status()
       if response.status_code == 200:
           data = response.json()
           content = data['results']
           target = ['email']
           for k in content:
               print(f"NAME: {k['name']['first']} {k['name']['last']}\nEMAIL: {k['email']}")
# # 2. Print name and email of each
        
# # 3. Count how many are male vs female
    except Exception as e:
         print(f"Error: {e}")

practice()