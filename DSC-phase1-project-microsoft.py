#!/usr/bin/env python
# coding: utf-8

# ![Microsoft%20Movie.png](attachment:Microsoft%20Movie.png)

# # Microsoft Movie Studios Pitch
# 
# **Author: Karina**

# ## Overview
# 
# Microsoft is looking to break into the movie industry by creating their own production company. While this is an exciting new opportunity for the company, they do not have a background in this industry so want to ensure they are giving themselves the best chance of success out of the gates. This project aims to go through and highlight what genres performed the best critically, and also to make reccomendations on what intellectual properties they should be looking into. 
# 
# Being new into the film industry a key factor that Microsoft will want to look into what are the common factors between the movies with the highest Box Office success and the IMDB ratings. This is important from a business perspective as it is only helpful to focus on the factors within their control. Movie production companies will receive a wide array of scripts with different stories, characters, settings etc so it is not quantifiable to choose solely based on the scripts themselves.
# 
# I would also make a further recommendation for Microsoft to acquire existing intellectual properties such as popular books, movie franchises and older properties that may be viable for remakes. These movies come with an existing audience fan so have a lower risk of underperforming at the box office so would be a smart area to invest in. 
# 
# Key learnings 
# Run time does not have a correlation with high or low ratings
# Exisiting Source Material makes for a sound investment with an assured audience base for higher ROI
# Genres with the highest scores included Action, Adventure & documentary.
# 

# ## Data 
# By focusing on what genres perform the best Microsoft will have a clear idea of what movies to look into making as they start in this new industry and it is important to focus factors that would be in the client’s control. This is why the below data focuses around ratings, gross box office income and what genres these are in. 
# 
# 

# In[1]:


# Import standard packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df1_budget = pd.read_csv ('tn.movie_budgets.csv.gz')
df2_imdb_title = pd.read_csv ('imdb.title.basics.csv.gz')
df3_imdb_rating = pd.read_csv ('imdb.title.ratings.csv.gz')


# In[3]:


#check for null values
df1_budget.info()
df2_imdb_title.info()
df3_imdb_rating.info()


# In[4]:


#merge IMDB movie info & movie rating data
df3_imdb_rating = df3_imdb_rating.merge(df2_imdb_title, on='tconst', how='left')
df3_imdb_rating.info()


# In[5]:


#clean out null values
df3_imdb_rating.dropna(subset=['genres'], inplace=True)
df3_imdb_rating.dropna(subset=['runtime_minutes'], inplace=True)

df3_imdb_rating.info()


# 
# # Most popular movie genres based on audience rating
# 
# In order to get a more accurate reading of the audience rating it is important to consider the amount of votes the movie has recieved. Some movies may have a relatively high rating but the number of votes is low which indicates this is not an accurate representation of the wider movie viewing community. So we will be focusing on IMDB ratings with more than 500 votes.
# 

# In[6]:


df3_imdb_rating2 = df3_imdb_rating[(df3_imdb_rating['numvotes'] >= 500)] 
df3_imdb_rating2


# In[7]:


#cleaning the table to get rid of redundant columns
df3_imdb_rating2.drop('original_title', axis=1)


# In[8]:


df3_imdb_rating2.rename(columns={"primary_title": "title"})


# In[9]:


# Caculate the averagerating for each genre and find out the top 10
df_rating_grouped = df3_imdb_rating2.groupby('genres')['averagerating'].mean()
df_rating_sort = df_rating_grouped.sort_values(ascending=False)
df_rating_sorted = df_rating_sort.reset_index()
df_rating_sorted.columns = ['genres', 'averagerating']
df_rating_sorted.head(10)

df_rating_sorted.head(10).set_index('genres', inplace=True)
df_ratings = df_rating_sorted.head(10)
df_ratings_by_genre = df_ratings.sort_values(by='averagerating')

# Check the final data for visulisation
df_ratings_by_genre


# In[10]:


df_ratings_by_genre.groupby('genres')['averagerating'].mean().plot(kind='bar', color='skyblue')
plt.xlabel('genres')
plt.ylabel('averagerating')
plt.title('Movie Genres with Highest IMDB Rating')
plt.show()
 


# 
# # Movie Run Time in relation to audience ratings
# 
# Production and editing time is an upfront costly expense for companies in the film industry which is why we chose to see if there was any correlation between the audience ratings and the length of the film. As it is clear from the below, there are high ratings across a wide variety of run times. While this is an important leaning given the costs involoved in production it is not an area Microsoft should focus on when making selections of what movies to make. 

# In[20]:


df3_imdb_rating3 = df3_imdb_rating2.sort_values(by='runtime_minutes', ascending=False)
df3_imdb_rating3


# In[27]:


# Caculate the averagerating for each genre and find out the top 10
df_rate_run_grouped = df3_imdb_rating3.groupby('runtime_minutes')['averagerating'].mean()
df_rate_run_sort = df_rate_run_grouped.sort_values(ascending=False)
df_rate_run_sorted = df_rate_run_sort.reset_index()
df_rate_run_sorted.columns = ['runtime_minutes', 'averagerating']
df_rate_run_sorted.head(10)

df_rate_run_sorted.head(10).set_index('runtime_minutes', inplace=True)
df_rate_runs = df_rate_run_sorted.head(10)
df_ratings_by_minutes = df_rate_runs.sort_values(by='averagerating')
df_ratings_by_minutes

#Line Graph and Box Plot
df_ratings_by_minutes.groupby('runtime_minutes')['averagerating'].mean().plot(kind='bar', color='purple')
plt.xlabel('runtime_minutes')
plt.ylabel('averagerating')
plt.title('Movie Run Times with Highest IMDB Rating')
plt.show()




# 
# # ROI Benefits from using exisiting intellectual property
# 
# Movie production is very costly and can be high risk as to whether it will perform well at the Box Office. This is why it can be beneficial to look into aquiring th rights to exisiting franchises or book series. Exisiting properties have a built in fan base which means there is more likely to be a higher ROI from the beginning.
# 
# A great example of this is the Harry Potter series. Prior to these being adapted into films, this was a very successful book series so there was an audience built in before the first movie aired. And it is clear from the data that production costs for the films stayed relatively level across the 8 movies, but the total profits rose. 

# In[11]:


#converting the domestic gross & worldwide gross into int64
df1_budget_prod = df1_budget['production_budget'].str.replace('[\$,]', '', regex=True).astype('int64')
df1_budget_wor = df1_budget['worldwide_gross'].str.replace('[\$,]', '', regex=True).astype('int64')


# In[12]:


#adding a column to the movie budgets spreadsheet to show the total profit or loss the movie made and converting into dollars

df1_budget['total_profit'] = df1_budget_wor - df1_budget_prod
df1_budget['total_profit'] = df1_budget['total_profit'].map('${:,.2f}'.format)
df1_budget = df1_budget[(df1_budget['domestic_gross'] != 0) & (df1_budget['worldwide_gross'] != 0) & (df1_budget['production_budget'] != 0)]



# In[ ]:





# In[13]:


# Select rows where the "Movie Title" column contains 'Harry Potter'
# Select rows where the "Title" column contains "Harry Potter"
# and the length of the title is longer than two words
selected_rows = df1_budget.loc[df1_budget['movie'].str.contains('Harry Potter') & (df1_budget['movie'].str.count(' ') > 1)]


# Display the selected rows
print("Rows with 'Harry Potter' in the title and length > 2 words:")
print(selected_rows)
# Create a new table (DataFrame) with the selected rows
new_table = selected_rows[['movie', 'release_date', 'production_budget', 'worldwide_gross', 'total_profit']]

# Display the new table
print("\nNew Table:")
print(new_table)


# In[19]:


# Plotting a line graph for 'Production_Cost' and 'Profit'
plt.plot(selected_rows['movie'], selected_rows['production_budget'], label='production_budget', marker='o')
plt.plot(selected_rows['movie'], selected_rows['total_profit'], label='total_profit', marker='o')

# Customize the plot
plt.xlabel('movie')
plt.ylabel('Amount (USD)')
plt.title('Production Cost vs Profit for Harry Potter Movies')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()


# 

# ## Conclusion
# For Microsoft to enter the movie production field it is key to make sound investments from the beginning. 
# 
# My Final reccomendations are as follows:
# 
# The top 10 genres based on the IMDB scores in descending order are listed below, these would be my reccomendations of the types of films Microsoft should be looking to make. I would reccomend Microsoft chose from among the below genres.
# 1   Action,Documentary	8.0
# 2   Animation,Crime,Documentary	8.0
# 3	Animation,Fantasy,Mystery	8.0
# 4	Comedy,Musical,Sci-Fi	8.0
# 5	Documentary,Romance	8.1
# 6	Animation,Documentary,Mystery	8.2
# 7	Animation,Crime,Mystery	8.2
# 8	Animation,History	8.3
# 9	Documentary,Music,War	8.9
# 10	Adventure,Drama,War	8.9
# 
# Investing in exisiting intellectual property such as book series, remakes and childhood characters is a sound investment due to the reduced risk in ROI. I would reccomend Microsoft invest time and money into sourcing and auriring such commodities. These not only have a higher ROI initially but also usually have higher audience ratings meaning that the movies will be rewatched resuilting in continuing ROI.
# 

# In[ ]:




