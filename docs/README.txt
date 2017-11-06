INTRODUCTION
  The application contained in this project intends to solve the problem presented in the file "PV Simulator Challenge".
  Some assumptions were made during the development of this projet, they are explained in the file ASSUMPTIONS.txt.

OVERVIEW
  If run with the default parameters, the application will generate a random value between 0-900 Watts every 2 seconds
for the meter and send it in a queue named 'pv_queue' in the local rabbitMQ broker. Every time the RabbitMQ consumer
receives the meter value it will read a value from the file ./input/default.yaml, which is indexed by the time of the day
and consider it as the photovoltaic (PV) power value generated. In sequence, a line containing both the meter and PV
values, the sum of the powers and a timestamp will be generated and output to a file.

HOW TO RUN
  This program was developed and tested in Ubuntu 14.04.5 LTS and Python version 3.4.3.
  To run this program just execute the file run.sh in the root of the project. It will install all the libraries
required to run (according to the file requirements.txt) and start the program with the default parameters.
  If you want to run the program with a different set of arguments just execute the program passing '--help' and a help
will be shown explaining how to do so.
