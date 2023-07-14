## HealthGPT

HealthGPT is a personal health assistant that uses your data to give helpful advice and reflections. It analyzes your data to determine trends and can make recommendations for how you can improve your health and fitness.

Interaction with HealthGPT happens through use of a large language model, such as ChatGPT, but this project is best used with a model running locally on your machine to ensure that your sensitive health data is kept private and not accessed by any third parties.

The first version of this project will only look at Apple Health data collected by an Apple Watch. Future iterations will include additional information such as nutrition, weather, and unstructured data such as personal journal entries.

## Setup

`bitsandbytes` is a required dependency for running Falcon-8B on a GPU. It has an issue with locating the CUDA runtime in the Python virtual environment. We need to add this runtime to the PATH so `bitsandbytes` can find it. Here is how to do that:

`sudo apt install mlocate` - this adds the `locate` command
`export CUDA_RUNTIME=locate libcudart.so` to find the CUDA runtime
`export PATH=$PATH:$CUDA_RUNTIME`