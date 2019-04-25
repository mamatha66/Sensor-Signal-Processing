# BMF055
Read and store sensor data into csv files

BMF055

usage: __main__.py [-h] [--file_path FILE_PATH] [--sensor {Acc,Gyr,Mag}] [--rate RATE] [--number NUMBER]

optional arguments:
 * -h, --help              show this help message and exit
 * --file_path FILE_PATH   Path to the output file
 * --sensor {Acc,Gyr,Mag}  Select the Sensor
 * --rate RATE             Rate
 * --number NUMBER         number of samples

command: python -m BMF055.__main__ --file_path FILE_PATH --sensor {Acc,Gyr,Mag} --rate RATE --number NUMBER
