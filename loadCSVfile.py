import sys
import csv
import pandas as pd
import numpy as np

fn = sys.argv[1:]

print('Save CSVFileName')
fileName = input('>>')

android_x_array = []
android_y_array = []
android_z_array = []

acce_x_array = []
acce_y_array = []
acce_z_array = []

for read_file in fn:
    csv_reader = pd.read_csv(read_file, header=None, skiprows=1 ,usecols=[1,2,3,4,5,6], sep=',', names=['acc_x', 'acc_y','acc_z','and_x','and_y','and_z'])
    android_x_array.extend(csv_reader.iloc[:,3])
    android_y_array.extend(csv_reader.iloc[:,4])
    android_z_array.extend(csv_reader.iloc[:,5])
    acce_x_array.extend(csv_reader.iloc[:,0])
    acce_y_array.extend(csv_reader.iloc[:,1])
    acce_z_array.extend(csv_reader.iloc[:,2])

# print("android_y_array\n", android_y_array)
# print("acce_y_array\n", acce_y_array)

acceCSV = np.c_[acce_x_array, acce_y_array, acce_z_array, android_x_array , android_y_array, android_z_array]
#データフレームを作成
df_y = pd.DataFrame(acceCSV, columns=['Acce_X', 'Acce_Y', 'Acce_Z', 'Android_X', 'Android_Y', 'Android_Z'])
#CSVファイルとして出力
print('write CSVFile')
df_y.to_csv(fileName, index=False)
