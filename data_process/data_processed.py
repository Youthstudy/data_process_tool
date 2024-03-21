import pandas as pd
import csv
import os


# afwffw

# success
def split_list(list):
    temp = []
    index_list = []
    s_list = []
    flag = 0
    for i in list[0]:
        try :
            temp.index(i)
        except ValueError:
            temp.append(i)
            index_list.append([])

        for a in range(len(temp)):
            if temp[a] == i:
                index_list[a].append(flag)
        flag += 1

    for i in range(len(index_list)):
        s_list.append([])
        a = 0
        for j in index_list[i]:
            s_list[i].append([])
            for k in range(len(list)):
                s_list[i][a].append(list[k][j])
            a += 1
    return s_list

def get_new_filename(filename):
    basename = os.path.splitext(filename)[0]
    return basename

# exists: true !exists: false
def is_filename_exists(filename):
    return os.path.exists(filename)

def get_unique_filename(filename,counter):
    return f"{filename}_{counter}"

def chage_filename(filename,counter):
    flag = counter
    while is_filename_exists(filename):
        flag += 1
        filename = get_unique_filename(get_new_filename(filename),flag)
    return filename

def write_csv(data_write):
    for i in range(len(data_write)):
        name = f"{data_write[i][0][0]}.csv"
        with open(chage_filename(name,0),'w',newline="") as csvfile:
            a = csv.writer(csvfile)
            a.writerow(["SensorId", " TimeStamp (s)", " FrameNumber"," QuatW", " QuatX", " QuatY"," QuatZ"])
            a.writerows(data_write[i])

def main():
    data = pd.read_csv("./111-1-1.csv")
    data = pd.DataFrame(data)
    df = data[['SensorId', ' TimeStamp (s)', ' FrameNumber',' QuatW', ' QuatX', ' QuatY',' QuatZ']]

    Sensor = df['SensorId'].to_list()
    time = df[' TimeStamp (s)'].to_list()
    FrameNumber = df[' FrameNumber'].to_list()
    QuatW = df[' QuatW'].to_list()
    QuatX = df[' QuatX'].to_list()
    QuatY = df[' QuatY'].to_list()
    QuatZ = df[' QuatZ'].to_list()

    data_all = []
    data_all.append(Sensor)
    data_all.append(time)
    data_all.append(FrameNumber)
    data_all.append(QuatW)
    data_all.append(QuatX)
    data_all.append(QuatY)
    data_all.append(QuatZ)
    
    writer = split_list(data_all)
    write_csv(writer)


main()
# print(df[['SensorId', ' TimeStamp (s)', ' FrameNumber',' QuatW', ' QuatX', ' QuatY',' QuatZ']])
