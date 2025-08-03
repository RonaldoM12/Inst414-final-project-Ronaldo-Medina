# Inst414-final-project-Ronaldo-Medina

Project Overview:
Online games like Marvel Rivals, Valorant, League of Legends (LoL) and overwatch have been plagued with toxic behavior within their online communities. This can include anything from Racism, harassment, berating teammates, griefing, and many other things which drive away new players and old players as no one likes to have someone who is constantly lowering morale on their team. Toxicity is terrible and not only does it affect user experience, but it also brands most games as completely unfriendly to new players, or you have to have very thick skin in order to be able to dive into it. 
As a safety analyst at a gaming company the role is to minimize toxicity as much as possible before it is taken to a level where it cannot come back down. The client is the head of player experience who wants all of their player base to enjoy the game and be able to bring in new players. The goal for the head of player experience is to be able to identify high risk players who are likely to become toxic and thus intervene or stop their messages before they are able to be released, stopping them with either communication bans or gaming restrictions. 
Data science can help by building a model that can identify and predict whether a player will exhibit toxic behavior in future matches, based on previous gameplay or gameplay from other games which are similar, we will also use their previous chat logs, and penalty history if they have any. This will allow all companies to moderate their online communities a lot more effectively which will also prevent damage or any further damage to their reputation. 

the data sets I am using are RIOT's API which include using in game chat logs, match level statistics, reports, ban history, and account meta data. And I am also going to use GITHUB MAX-Toxic-Comment-Classifier 

The technique I will be employing is a logistic regression

my expected outputs are that the model will be able to look for possible harrasment within comments and be able to determine whether or not the player will need to be penalized or given a warning to stop using toxicicty and or suffer consequences

Setup Instructions:
in order to clone this project you will need to use the following link to find this project or search up RonaldoM12 on GITHUB: https://github.com/RonaldoM12/Inst414-final-project-Ronaldo-Medina

from here we then click on code and copy the HTTPS link and we are going to paste it into our VS Studio Or an alternative way to do this is if you have the GITHUB desktop app where you can import the project and then open it directly into VsCode and it will automatically set it up

How to run the project:

In order to run this project YOU MUST BE IN Main.py that is where the main function is which will call on all parts of the coding. Once we are in main you can either click the top left arrow to run the code or you can run it from the terminal. 

cd/path/to/my/INST-414-Final-project-Ronaldo-Medina

Code Package Structure: 
'data/: RIOT API'
'data/: GITHUB MAX-Toxic-Comment-Classifier'

