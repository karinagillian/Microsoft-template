# Microsoft Movie Studios Pitch
Author: Karina

![Microsoft Movie](https://github.com/karinagillian/Microsoft-template/assets/152271088/1ed5c865-fabb-4044-a93e-bc9bfdf8cef5)

## Overview

Microsoft is looking to break into the movie industry by creating their own production company. While this is an exciting new opportunity for the company, they do not have a background in this industry so want to ensure they are giving themselves the best chance of success out of the gates. This project aims to go through and highlight what genres performed the best critically, and also to make reccomendations on what intellectual properties they should be looking into. 

Being new into the film industry a key factor that Microsoft will want to look into what are the common factors between the movies with the highest Box Office success and the IMDB ratings. This is important from a business perspective as it is only helpful to focus on the factors within their control. Movie production companies will receive a wide array of scripts with different stories, characters, settings etc so it is not quantifiable to choose solely based on the scripts themselves.

I would also make a further recommendation for Microsoft to acquire existing intellectual properties such as popular books, movie franchises and older properties that may be viable for remakes. These movies come with an existing audience fan so have a lower risk of underperforming at the box office so would be a smart area to invest in. 

Key learnings 
Run time does not have a correlation with high or low ratings
Exisiting Source Material makes for a sound investment with an assured audience base for higher ROI
Genres with the highest scores included Action, Adventure & documentary.

## Data

The data analysed came from IMDb & The Numbers webite, both of these databases contain detailed information on movie production, ratings, gross income, actors, and more making it a valuable resrouce to draw on for this project. 
The data initially needing cleaning by removing null values, reordering where needed, removing columns that were not relavent and also merging data sets. This made the data easier to work from and also easier to share the findings in a succinct and clear manner. 

***

## Methods

After checking the information on each table to see column names and null values, I joined the two datasets, df_titles_basic_info and df_ratings together using the 'tconst' column as it was a unique identifier creating a new dataframe called df3_imdb_rating. The new joined dataframe contained the information needed to work with the IMDB ratings and movie genres. I used this to find out which genres rated the highest when making my reccomendations to Microsoft. I also used this dataframe to see if there was any correlation between audience ratings and the movie length. 

The Numbers budget dataframe contained the production costs & box office gross. I added an additional column that contained the total profit once you removed production costs from the total gross, this allowed me to explore the benefits of using exisiting intellectual materials and make reccomendations to Microsoft based on my findings. 
***

## Results & Conclusions

Highest Rated Genres
![Top Rated Genres](https://github.com/karinagillian/Microsoft-template/assets/152271088/0f76f471-c289-477b-90d7-ccd42b260fb1)
The above graph indicated the highest rated genres based on their IMDB scores. I would reccomend Microsoft choose from this list when selecting the movies they should make 
1   Action,Documentary	8.0
2   Animation,Crime,Documentary	8.0
3	Animation,Fantasy,Mystery	8.0
4	Comedy,Musical,Sci-Fi	8.0
5	Documentary,Romance	8.1
6	Animation,Documentary,Mystery	8.2
7	Animation,Crime,Mystery	8.2
8	Animation,History	8.3
9	Documentary,Music,War	8.9
10	Adventure,Drama,War	8.9

Benefits of investing in exisiting franchises & intellectual properties
![Harry Potter](https://github.com/karinagillian/Microsoft-template/assets/152271088/64dd6122-4b76-42ff-9fd7-3731af8e2333)
This graph clearly indictaes that across all the Harry Potter movies there was very little variation in production costs and with multiple movies staying within a similar budget. However, the profits increased. This shows that the movie series was extremely popular and continued to draw a growing audience but Warner Brothers did not necessarily need to invest more money into the production of the films meaning a higher profit margin and ROI. 



![giphy-5](https://github.com/karinagillian/Microsoft-template/assets/152271088/5ac224ca-49d5-4132-b50c-2f8c3818d6e8)




## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── README.md                           <- The top-level README for reviewers of this project
├── DSC-phase1-project-microsoft.py   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
