Why: I was thinking of making a separate project that would install the datasets from Hugging Face to a place in my laptop where projects working on different python environments and anywhere in my local laptop can access that.

Research:
When you download a dataset from HF using dataset = load_dataset("ylecun/mnist") it goes Hugging Face’s cache folder under your Mac user account: /Users/abc/.cache/huggingface/

All the datasets go to: /users/abc/.cache/huggingface/datasets
--> Downloaded nultiple datasets and checked if they went here and they did.

So I want to make a seperate project whose sole purpose is to download the Datasets from HF.

I want this project to be assebibly called by other projects by just inputing the Dataset ID and be able to access the dataset.

Access the dataset: All downloaded datasets go to one location so can be accessed by different projects.

Being able to be called by other projects: maybe API??

Because 


What I want to do is lets say I have written the code that will download the dataset from HF using the ID. I want the other project to just call this function lets say and download 

Download the dataset, put it in a variable, print that variable

Libraries used: datasets


User Stories: 
a. As a user, I want to input the Dataset ID
b. As a user, I should be able to get access to that dataset using a different python environment