# Data Science Assignment 



## _News Category Classification Model_



### Repository Content
```
├── static
│   ├──css 
│         ├── style.css         >CSS file
├── templates   
│            ├──index.html      >HTML file
├── .gitattributes              > to track the  large saved  model files using git-lfs
├── Dockerfile
├── news_classification.ipynb  >news classification model trained using  DistilBERT
├── app.py                     >flask  application main file
├── dockerfile                 >DockerFile to automate process of building a Docker image    
└── requirements.txt               > Stores the python  modules
```
### Reason for Choosing DistilBERT for Transfer Learning

_I chose DistilBERT for finetuning and transfer learning for my task due to several compelling reasons that make it the preferred choice over BERT, RoBERTa, and XLNet, especially considering the limited training time:_ 

1. **Faster Inference Speed**: DistilBERT offers faster inference speed compared to BERT, RoBERTa, and XLNet. This is a critical advantage for my task, as it involves real-time or low-latency processing. The faster inference speed of DistilBERT ensures that I can obtain results quickly and efficiently.
2. **Efficient Resource Utilization**: DistilBERT is a smaller network that retains 95% of BERT's language understanding capabilities while using 60% fewer parameters. This parameter efficiency makes it more suitable for tasks with limited computational resources, enabling me to achieve comparable performance with reduced memory and computational requirements.
3.  **Acceptable Trade-off in Prediction Metrics**: While DistilBERT may have a slight compromise on prediction metrics compared to BERT, RoBERTa, and XLNet, the difference in performance is minor. Given the gains in inference speed and resource efficiency, this trade-off is well justified for my task.
4. **Transfer Learning Benefits**: DistilBERT benefits from pretraining on a large corpus, which provides it with a strong language understanding foundation. This makes it well-suited for transfer learning, allowing me to fine-tune the model on my specific task with potentially less labeled data.
5. **Training Time Limitation**: Since I have limited training time, DistilBERT's faster training speed compared to BERT, RoBERTa, and XLNet becomes a crucial factor. It allows me to efficiently fine-tune the model within my time constraints while still achieving satisfactory performance.

_Considering these reasons, DistilBERT emerges as the most practical and efficient choice for my task. Its faster inference, resource efficiency, and transfer learning benefits make it well-suited to meet the requirements and constraints of my specific scenario, especially when training time is limited._



## Dockerize and deploy the model as REST API using Flask


### Build the docker image manually by cloning the Git repo. 
```
$ git clone https://github.com/Parthkh28/DataScience.git
$ docker build -t myimage .
```
### Download precreated image
You can also just download the existing image from DockerHub.
```
docker pull parthkh28/news
```
### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 5000:5000 myimage
```
In the above example we are running a docker container with the name my-container in detached mode and mapping port 5000 of the host to port 5000 of the container. The image we are using is myimage.

Now visit http://localhost:5000


## This flask app allows users to submit input requests either through an **API** or a **web application form**.

### Through Web Application Form

[![IMAGE ALT TEXT]("")

### Through API using POSTMAN

[![IMAGE ALT TEXT]("")


And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## To source and distribute data for building a text classification model from the internet, I would adopt several methods as a data scientist. Some of the methods are:

1. Web Scraping: I would use Python libraries like Beautiful Soup or Scrapy to extract data from websites that are relevant to my problem. These libraries help me to parse HTML and XML documents and get the information I need. 
2. APIs: I would use APIs (Application Programming Interfaces) offered by various websites, such as sports websites, science websites, etc. These APIs provide structured data that I can easily use for training my model. 3. 
3. Crowdsourcing: I would collect labeled data from a large number of contributors using platforms like Amazon Mechanical Turk, Google Forms, or other similar platforms. This method can help me when I need a lot of data and I cannot collect it myself. 4. 
4. Public Datasets: I would look for public datasets that are related to my problem and use them to train and test my model. Public datasets are often provided by government agencies, research institutions, or other organizations that give open access to their data. 5. 
5. Data Licensing: If I need data that is not publicly available, I would license data from reliable data providers. This method can help me when I need high-quality, proprietary data that I cannot find elsewhere. 6. 
6. Active Collection: I would gather data from various sources, such as social media, forums, and other online platforms, using tools like Twitter APIs, Reddit APIs, or other similar APIs.
7. Data Augmentation: After collecting the data, I would use techniques like data augmentation to create more data from the existing data. This method can help me when I need a bigger dataset to train my model. 
8. Transfer Learning: I would use pre-trained models and transfer learning to use the knowledge learned from other related tasks and adjust the models to my specific task. This method can help me when I have limited data and computational resources.

## Leveraging the  data and trained classification model to inform companies about supply chain disruptions

One possible way to leverage the data and the model is to create a **dashboard** that displays the distribution of news articles by category and time, and highlights articles related to supply chain disruptions, can be a powerful tool for companies to monitor and reduce supply chain risks.
Description of the dashboard and its features:
- Bar Chart: The dashboard could display a bar chart that shows the number of news articles by category for each month. The categories could be represented by different colors, with the categories related to supply chain disruptions (e.g. "Delays", "Commodities", "Environmental") colored in red. This would give the user a quick overview of the distribution of news articles by category and the trends over time.
- Filtering: The dashboard could allow the user to filter the news articles by category and date range. For example, the user could select to view only the articles related to "Delays" in the last quarter, or view all the articles related to "Commodities" for the past year. This would allow the user to focus on specific areas of interest and identify trends and patterns.
- Sorting: The dashboard could allow the user to sort the news articles by event timestamp, category, or other relevant criteria. This would allow the user to view the most recent articles related to specific categories or topics.
- Clickable Titles: The dashboard could display the titles of the news articles in a table, with a link to read the full article. This would allow the user to quickly view the details of the article and take action if necessary.
- Alerts: The dashboard could be set up to send alerts to the user when certain conditions are met, such as when a certain number of articles are published related to a specific category or when a specific event occurs. This would allow the user to stay informed and take proactive actions to mitigate supply chain risks.
- Trend Analysis: The dashboard could include trend analysis tools, such as a moving average or a rolling sum, to help the user identify long-term trends and patterns in the data. This would allow the user to make more informed decisions about their supply chain strategies.
- Data Export: The dashboard could allow the user to export the data for further analysis or to share with other stakeholders. This would be useful for companies that need to analyze the data in more detail or present the information to other teams or stakeholders.

Another way is to use **word maps**. Word maps are visual representations of the frequency and importance of words in a text. They can help us identify the main topics and themes in the news articles and see how they relate to each other. 

>> For example, a word map of the news category “Commodities” might show words like “oil”, “gas”, “price”, “demand”, “supply”, etc. This can give us a quick overview of the factors that affect the commodity market and how they might impact the supply chain.




