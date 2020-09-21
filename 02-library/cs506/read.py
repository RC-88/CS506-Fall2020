def read_csv(csv_file_path):
    data=[]
    f=open(csv_file_path)
    ln=f.readline()
    while ln:
        string=[str(x).replace('"', "") for x in ln.strip().split(",")]
        print(string)
        for i in range(len(string)):
            if string[i].isdigit():
                string[i] = int(string[i])
            else:
               string[i] = str(string[i])

        data.append(string)
        ln = f.readline()
    return data


#print(read_csv("/Users/reinachau/CS506-Fall2020/02-library/tests/test_files/dataset_2.csv"))





