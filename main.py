from dotenv import load_dotenv
import os
from github import Github

# Load variables from the .env file
load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")

g = Github(access_token)

# Get the authenticated user
user = g.get_user()

# Get the authenticated user's followers
followers = [follower.login for follower in user.get_followers()]

# Get the users that the authenticated user is following
following = [follow.login for follow in user.get_following()]

# Find users who are not following back
to_follow = list(set(followers) - set(following))

# Follow users who are not following back
for username in to_follow:
    username = g.get_user(username)
    user.add_to_following(username)
    print(f"Followed: {username}")
