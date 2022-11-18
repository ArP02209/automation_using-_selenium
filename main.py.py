#!/usr/bin/env python
# coding: utf-8

# In[105]:


#Before going forward we first need to install selenium package and chromedriver having same version as your chrome browser

from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Taking user input as name of trailer of web series/movies
trailer= input()

#Loading chromedriver 
driver = webdriver.Chrome()
driver.maximize_window()

#Go to google.com
driver.get("https://www.google.com/")
time.sleep(3)

#Finding google search box and sending the name of trailer as input
driver.find_element(By.NAME, "q").send_keys(trailer + Keys.RETURN)

#driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[3]/div/div/div/div/div/div/div/div[1]/div/a/h3").send_keys(Keys.RETURN)
#Finding the link of trailer having keyword Netflix and go to that link
driver.find_element(By.PARTIAL_LINK_TEXT," Netflix Official Site").click()

#Play trailer using its Xpath
driver.find_element(By.XPATH,"//*[@id='section-additional-videos']/div[2]/ul/li[1]/div/button/span[2]").click()

#print(driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]").text)

descript=driver.find_element(By.XPATH, "/html/body").text

print("ALL DETAILS:\n"+ descript)


# In[102]:


print(driver.title)


# In[16]:


driver


# In[ ]:




