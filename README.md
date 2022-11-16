# ✨ Haystack based QA system 🚀 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A simple Question Answering system built on a corpus of documents of different formats using Haystack and Streamlit

![demo](https://user-images.githubusercontent.com/29462447/202132911-1c761b9f-b19f-463a-9ac5-927776e207c1.gif)


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

If you run into any issues with installation of haystack, please refer [this.](https://github.com/deepset-ai/haystack)


## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Place your documents in the **docs** folder and simply run the following command in order to do bulk conversion of the documents to plain text: 
```
python data.py
```
![1](https://user-images.githubusercontent.com/29462447/202132627-bbe70c9a-b0f3-43b4-9f06-6d35fab28ef0.png)

3. We will convert the text documents into the haystack supported format and apply Preprocessor to clean and split the document into sensible units. We will store these preprocessed texts in a SQL document store. Run the following command to perform the indexing:
```
python index_pipeline.py
```
![2](https://user-images.githubusercontent.com/29462447/202132735-eb509cf1-3608-4667-bfb3-0bfb658a21f5.png)


4. We will download our reader (a pre-trained transformer model on QA task) and also initialize our retriever to search top k relevant documents in document store.For a given question, the retriever will search for the top ‘k’ documents relevant to the question and reader will predict answers using those ‘k’ documents instead of searching the whole document store. In order to test this, you can run the following script:
```
python search_pipeline.py
```
![3](https://user-images.githubusercontent.com/29462447/202132813-db68111c-7f62-499f-9e5c-fe5c672bed05.png)


## Web App
Here is our web app built using streamlit which is compatible with haystack and also it is easy to use. You can run the app by:
```
streamlit run app.py
```

![4](https://user-images.githubusercontent.com/29462447/202132497-256d3b05-70d1-40e0-96f8-6cb35a598772.png)

![5](https://user-images.githubusercontent.com/29462447/202132512-7397f209-0cf4-4412-b3b1-95d8250e420d.png)



### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
