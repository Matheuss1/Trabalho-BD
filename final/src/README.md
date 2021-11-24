# How to run the scripts?

To execute this project python scripts, you should use the [virtual environment](../bin) available in project bin folder.

To activate this virtual environment, go to the [bin](../bin) folder and execute the command ```source ./bin/activate```. After that, you should be able to run the scripts using our venv.

If you want to recreate the dataset and download all the data again, you have to run the [make_dataset.py](./data/make_dataset.py) script. 

There are certain conditions to execute this script with success. The first one is that you have to execute the file inside a folder called "data", otherwise the script will fail. 

Another important point is that we use the https://www.investing.com/ to get indices data in a free way. But there is a limit of requisitions that can be sent to the server before you have your ip blocked to make new requests. We recommend to execute the script one time, and to comment the lines of make_dataset.py that calls the investapi and was already executed. This will guarantee that no repeated requests will be made.

If you get blocked to send requisitions to https://www.investing.com, just restart your internet connection and you'll probably get a new IP adress, what will allow you to send new ones.

## Jupyter notebooks

You should also use our venv to run this project jupyter notebooks. To do this, you can follow this [tutorial](https://janakiev.com/blog/jupyter-virtual-envs/) of how to run jupyter using virtual environments.