# Certificates validator code
BY: RAFAEL CASTRO GARCIA PLATA (rafacast)
1. This script has the goal to reduce the engineers work of checking the customers code, once the customer executes the code on the machine it will let the engineer know if the customer has all the required certicates for Secure Client to work properly
   + What this code does is to execute a PowerShell command via Python and will compare the output obtained with the fixed cisco certificate list
   + It will check if all the certificates match and will output all of the ones that are found, if a certificate is missing it will let the engineer know which one is it so that the ATS engineer can make a better and faster diagnosis
   + It was all done with python, the customer should run this on the cmd when the engineer provide the code
   + It was challenging to at first know how to manipulate the output of the PowerShell command, in addition and as a best practice the certificates list and output was transformed in a manner that the ATS engineer as well as the client are able to see which are the certificates the client has, the scope is that in a near future the customer is able to only provide the debug bundle and BORG being able to analyze the logs
2. How to run this program
   + Provide the customer the .zip file, the customer should unzip the file and execute the .py file, once the customer does this, the desired output should be obtained

Special Thanks to:
Juventino Macias (jmaciasc)
Vibhor Amrodia (vamrodia)
For being a guidance and assisting me on this project

DO NOT RUN THIS ON POWERSHELL, THE CUSTOMER SHOULD RUN THIS ON CMD OR VISUAL STUDIO
