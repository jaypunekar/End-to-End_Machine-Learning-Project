# California House Price Predictor
This regression model is based on a Kaggle [Dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices). You will get more information about the attributes of the dataset from the link I have provided.

LINK: https://www.kaggle.com/datasets/camnugent/california-housing-prices

## Contents
- [Requirements](#software-and-account-requirement)
- [Deploying Model](#running-the-model-locally)
- [Adding to GIT](#add-files-to-git)
- [Making Docker Image](#build-docker-image)
- [Screenshots](#screenshots)


### Software and account Requirement

1. [Github Account](https://github.com)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)





## Running the Model locally

Clone the project.
```
git clone https://github.com/jaypunekar/HousingPricePredictor.git
```
```
cd HousingPricePredictor
```
#### Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To run the model locally:
```
python application.py
```

OR 
```
python3 application.py
```

#### Onece the model is running, go to localhost:5000 to view the project



### Add files to git

#### To do so you will first have to fork the project into your github and clone it from there.

```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```


### Build Docker Image
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift


To Run the Application
```
python3 application.py
```
## Screenshots

[![img2.png](https://i.postimg.cc/tgcbjKkb/img2.png)](https://postimg.cc/Mc1N0rg3)

[![img1.png](https://i.postimg.cc/d0kRWCSB/img1.png)](https://postimg.cc/wtzsM1zy)

[![img-3.png](https://i.postimg.cc/fR30ZNjW/img-3.png)](https://postimg.cc/VJ8NB2V2)
