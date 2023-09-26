# Simple flask app for price prediction
This is a flask server app for predicting real estate
price using machine learning. Project for end to end simple ML project in GSOM.

## Model
The predicting model is a gradient boosting using [catboost](https://catboost.ai/) 
lib. It has the best fit among other methods: linear regression and random forest.

Used hyperparameters for this model
```
num_trees=500
random_seed=42
depth=5
```

Other hyperparameters are set to default values.

## Setup

You can set up a server either using virtual env or docker container. 
Just follow the instruction.

### Using virtual env

First step: create virtual env

```
python -m venv venv
```

Then activate this 

```
source venv/bin/activate
```

Install requirements

```
pip install -r requirements.txt
```

Start the app on port 80 (default value)

```
python src/main.py
```

If you want to use custom argument try this:

```
python src/main.py --port <port> --model-path <path_to_mode>
```

###  Using docker

You can use existing Dockerfile in this repo. 
It has all necessary commands to run this server. It uses `80` as default.

Build docker

```angular2html
sudo docker build . -t server
```

Start docker and pass 80 port

```angular2html
sudo docker run -p 80:80 -t server
```

Congratulations! Your application is running on port 80

## Request

Consider your flask app is running on a remote host on a specific port.

Request example:

```
curl "http://<remote_host_ip>:<port>/predict_price?rooms=3&area=32"
```

List of supported arguments: 

|      Name     | Type  |
|:-------------:|-------|
| floor         | int   |
| category_type | int   |
| open_plan     | bool  |
| rooms         | int   |
| studio        | bool  |
| area          | float |
| kitchen_area  | float |
| living_area   | float |
| agent_fee     | float |
| renovation    | bool  |
| offer_type    | int   |

## Open port on a remote machine

```angular2html
sudo ufw allow 80
```
