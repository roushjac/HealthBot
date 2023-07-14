## HealthBot

HealthBot is a personal health assistant that uses your data to give helpful advice and reflections. It analyzes your data to determine trends and can make recommendations for how you can improve your health and fitness.

Interaction with HealthGPT happens through use of a large language model, such as ChatGPT, but this project is best used with a model running locally on your machine to ensure that your sensitive health data is kept private and not accessed by any third parties. The default LLM is [Falcon 7B instruct](https://huggingface.co/tiiuae/falcon-7b-instruct).

If your machine has at least 85-100GB of memory you can run [Falcon 40B instruct](https://huggingface.co/tiiuae/falcon-40b-instruct)

The first version of this project will only look at Apple Health data collected by an Apple Watch. Future iterations will include additional information such as nutrition, weather, and unstructured data such as personal journal entries.

## Setup

We are using Docker to simplify the dependency management required for this project.

Run these commands to create a docker image and then use the image to run a container.

```
docker build -t healthbot .
docker run -p 5000:5000 --gpus all -it healthbot
```
