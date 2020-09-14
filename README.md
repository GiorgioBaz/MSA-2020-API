# MSA-2020-API

## Project Description

### Home Page

The home page is quite simplistic, with a singular button which toggles a modal that asks for your **Steam ID which is a 17-digit code you can find on your steam profile**. After entering that ID, you will be able to see the top 5 most played games on that account. 
The fetch statement calls the Steam API using the documentation in the link below. After the API is called my program takes that data and runs it through the script which determines your top 5 most played games. https://developer.valvesoftware.com/wiki/Steam_Web_API#GetOwnedGames_.28v0001.29. **Valid Credentials for all API calls are referenced at the bottom of this README**

### Game Statistics Page
This page is where most of the work was completed, it features both the Fortnite and Apex Legends API calls. I styled this page using bootstrap’s modal, table and button features, which allowed me to structure all of the data which I received from the different APIs. The select game modal uses conditional rendering to display the enter Fortnite and/or Apex Legends details buttons. 

#### Fortnite Statistics
The Fortnite Details modal requires you to enter in your platform (kbm, gamepad or touch) and your Epic Username. Once both these fields are populated the API is called and the data is displayed in a table. Documentation for the Fortnite API can be found at https://fortnitetracker.com/site-api **Valid Credentials for all API calls are referenced at the bottom of this README.** 

#### Apex Legends Statistics
The Apex Details modal has a similar function, it requires two fields platform (origin, xbl or psn) and origin username (either originid, xbox gamertag or PSN ID). Once the fields are populated the data is also displayed in a table. Documentation for the Apex Legends API can be  **Valid Credentials for all API calls are referenced at the bottom of this README.** 

## Running the Project
In a windows terminal run the following commands on the repository folder
1. `python -m venv venv`
2. `venv\Scripts\activate`
3. `flask run`

**If need be install flask with:** 
* `pip install flask`

## Tech Stack
* Frontend: HTML, CSS, Bootstrap and JavaScript
* Backend: Python with Flask

## Testing Credentials 
**Disclaimer: These are all my personal accounts, if you would like to add in your own id for steam make sure you don’t have a custom url on your profile.**

#### Steam Credentials
* Steam 17-digit Key: 76561198188867330
#### Fortnite Credentials
* Gaming platform: kbm
* Epic username: AssassinOCE
#### Apex Legends Credentials
* Gaming platform: origin
* Origin username: fully_assassin
