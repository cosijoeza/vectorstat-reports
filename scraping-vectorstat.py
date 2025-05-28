import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

file_path = 'web-path.json'
with open(file_path, 'r') as file:
    web = json.load(file)

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the website
url = "https://vectorstat.com"
driver.get(url)
stay = 10

# Wait to url is ready
time.sleep(stay)

# Set user
inputUser = web["login"]["inputUser"]
inputElement = driver.find_element(By.XPATH, inputUser)
inputElement.send_keys(user)

# Set password
inputPassword = web["login"]["inputPassword"]
inputElement = driver.find_element(By.XPATH, inputPassword)
inputElement.send_keys(password)

# Click the login button
loginButton = web["login"]["buttonLogin"]
buttonElement = driver.find_element(By.XPATH, loginButton)
buttonElement.click()

# Wait for the page to load
time.sleep(stay)

# Click on the organizations button
buttonOrgSection = web["organizations"]["buttonOrgSection"]
buttonElement = driver.find_element(By.XPATH, buttonOrgSection)
buttonElement.click()

# Wait for the organizations page to load
time.sleep(stay)

# Search for the organization
organization_name = "Alabama A&M"
inputOrgName = web["organizations"]["inputOrgName"]
inputElement = driver.find_element(By.XPATH, inputOrgName)
inputElement.send_keys(organization_name)

# Wait for the search results to load
time.sleep(2)

# Click the searched organization
buttonFirstSearch = web["organizations"]["buttonFirstOrganization"]
buttonElement = driver.find_element(By.XPATH, buttonFirstSearch)
buttonElement.click()

# Wait for the organization page to load
time.sleep(20)

# labelList = web["organizations"]["organizationInfo"]["labelList"]
# labelListElement = driver.find_element(By.XPATH, labelList)
# print("Label list size: "+labelListElement.size)

# Read the organization information labels from the JSON file and get their text
firstLabel = web["organizations"]["organizationInfo"]["firstLabel"]
# secondLabel = web["organizations"]["organizationInfo"]["secondLabel"]
# thirdLabel = web["organizations"]["organizationInfo"]["thirdLabel"]
# fourthLabel = web["organizations"]["organizationInfo"]["fourthLabel"]
# fifthLabel = web["organizations"]["organizationInfo"]["fifthLabel"]
# sixthLabel = web["organizations"]["organizationInfo"]["sixthLabel"]

labelElement = driver.find_element(By.XPATH, firstLabel)
print(labelElement.text)
# labelElement = driver.find_element(By.XPATH, secondLabel)
# print(labelElement.text)
# labelElement = driver.find_element(By.XPATH, thirdLabel)
# print(labelElement.text)
# labelElement = driver.find_element(By.XPATH, fourthLabel)
# print(labelElement.text)
# labelElement = driver.find_element(By.XPATH, fifthLabel)
# print(labelElement.text)
# labelElement = driver.find_element(By.XPATH, sixthLabel)
# print(labelElement.text)

# Wait for the organization page to load
time.sleep(stay)

# Close the browser
driver.quit()
