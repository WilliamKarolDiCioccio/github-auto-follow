from dotenv import load_dotenv
import os
from github import Github

# Load variables from the .env file
load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
whitelist = os.getenv("WHITELIST", "").split(',')  # Comma-separated usernames

g = Github(access_token)

# Get the authenticated user
user = g.get_user()

# Get the authenticated user's followers
followers = {follower.login for follower in user.get_followers()}

# Get the users that the authenticated user is following
following = {follow.login for follow in user.get_following()}

# Convert whitelist to a set
whitelist = set(whitelist)

# Determine users to follow (followers who are not followed back)
to_follow = followers - following

# Determine users to unfollow (people followed but who are not followers, excluding whitelisted users)
to_unfollow = (following - followers) - whitelist

# Follow users who are following me
for username in to_follow:
    try:
        user.add_to_following(g.get_user(username))
        print(f"Followed: {username}")
    except Exception as e:
        print(f"Failed to follow {username}: {e}")

# Unfollow users who do not follow back and are not whitelisted
for username in to_unfollow:
    try:
        user.remove_from_following(g.get_user(username))
        print(f"Unfollowed: {username}")
    except Exception as e:
        print(f"Failed to unfollow {username}: {e}")
