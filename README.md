# Streamcollage
Spotcollage is web application that enables you to generate a 3x3, 4x4, or 5x5 collage of your top played Spotify albums within a specified time range.

# Try Out Spotcollage
The web application is hosted here:
http://spotcollage.herokuapp.com

Note that this application requires authentcation with your Spotify account.

# How to set up
Use PIP to install everything in ```requirements.txt```

Go to ```developer.spotify.com``` and create a new Spotify application.

Create a file called ```.env``` in the ```/spotcollage``` dictionary and create the following variables.

```
SPOTIFY_CLIENT_ID="Your Spotify Client ID"
SPOTIFY_CLIENT_SECRET="Your Spotify Client Secret"
SPOTIFY_REDIRECT_URI="Your Spotify Redirect URL"
```
