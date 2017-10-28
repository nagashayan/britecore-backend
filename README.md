# britecore-backend

# Environment 

Flask 0.12.2
Python 3.6.1 |Anaconda 4.4.0 (x86_64)| (default, May 11 2017, 13:04:09) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]

#Running the program is quiet simple. 

I have used anaconda to maange packages and virutal environment and migrations are handled alembic

#For backend 

#Create virutal environment automatically from below file
conda env create -f environment.yml

#Activate your environment

Windows: activate myenv
macOS and Linux: source activate myenv

#Load some variables 

macos and linux: source .env

#Finally run 
flask run --host=0.0.0.0

