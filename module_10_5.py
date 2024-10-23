import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line.strip())
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start_time = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
end_time = datetime.datetime.now()
print(f'{end_time - start_time} (линейный)')

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    with Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    print(f"{end_time - start_time} (многопроцессный)")
