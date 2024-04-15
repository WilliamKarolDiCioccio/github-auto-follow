# GitHub Auto Follow

GitHub Auto Follow is a utility python script that uses the GitHub API to automatically follow back users who follow you. This script can be useful for managing your followers and maintaining a reciprocal relationship with them.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed on your machine
- An access token with user permissions from GitHub. This token should be stored in an environment file named `.env` with the variable name `ACCESS_TOKEN`. The token can be set to never expire.

## Installation

To use GitHub Auto Follow, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/DiCioccioWilliamKarol/github-auto-follow.git
    ```

2. Create an environment file named `.env` in the root directory of the cloned repository.

3. Open the `.env` file and add the following line, replacing `YOUR_ACCESS_TOKEN` with your actual access token:

    ```bash
    ACCESS_TOKEN=YOUR_ACCESS_TOKEN
    ```

4. Save the `.env` file.

## Usage

To run the script, navigate to the root directory of the cloned repository in your terminal and execute the following command: `poetry run main.py`
