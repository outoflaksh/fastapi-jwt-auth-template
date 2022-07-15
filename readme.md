<div id="top"></div>

<h2 align="center">FastAPI Authentication Template</h2>
<h4 align="center">
  Implementing user login with OAuth2 Password-flow & JWT
</h4>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Implementing a user model in your application always seems like a painful task, at least to me. It's always the exact same code with minor configurations but it still takes a lot of time to build and add to the codebase. That's why, I decided to put all the core user model code in one place so that all it takes to integrate one in your existing application, is just a few quick changes.

This template implements a complete, secure, fast, and easy-to-add user sign in and sign up model code that works on the OAuth2 password-based-auth-flow and preserves and authorises the user on the basis of JWT tokens, for FastAPI-based applications.

All you need to do is to modify the database schemas according to your needs (or leave it the same depending upon what you want), and add your database handling code to the file, that connects and handles the queries from whatever database engine your application is using.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [passlib](https://pypi.org/project/passlib/)
- [python-jose](https://pypi.org/project/python-jose/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/outoflaksh/fastapi-jwt-auth-template.git
   ```
2. Change your working directory to the cloned repo.
   ```sh
   cd fastapi-jwt-auth-template
   ```
3. Install the dependencies.
   ```sh
   python3 -m pip install -r ./requirements.txt
   OR
   pip install -r ./requirements.txt
   ```
4. Start the FastAPI server with Uvicorn.
   ```sh
   uvicorn main:app
   ```

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [The absolutely beautiful official FastAPI Documentation](https://fastapi.tiangolo.com/)
