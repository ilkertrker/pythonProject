#begin####

print("hello world")
print("hello AI Era")

# Numbers and String (Sayılar ve Karakter Dizileri) #
print(9)

#Let's find the type of object#
type(9)
type(9.2)
type("Oiii")

#Assigments & Variables (Atamalar ve Değişkenler)#
#If you want to assing a value to an object you should use "=" #

a = 9
a
b = "Hi mate, I'm AI"
b
c = 10
a*c #you can make some math with it#

#virtual Environment#
#conda create -n myenv
#conda activate mynev
#conda activate myenv
#conda deactivate myenv
#conda list

#package_management
#conda install numpy
#conda install numpy scipy panda
#conda install scipy pandas
#conda remove package_name

#for_specific_version
#conda install numpy=1.20.1

#for_upgrade_ver
#conda upgrade numpy
#conda upgrade -all

#pip: pypi(python package index)
#upload package
#pip install pandas
#pip install panda==1.2.1

#transfer_for_packages
#conda env export > environment.yaml
#dir
#conda env remove -n myenv
#conda env create -f environment.yaml
#conda avtiate


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

