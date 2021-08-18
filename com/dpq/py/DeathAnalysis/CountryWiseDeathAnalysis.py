import csv
import time
import multiprocessing
from com.dpq.py.DeathAnalysis.CountryWiseDeathDetails import CountryWiseDeathDetails


class CountryWiseDeathAnalysis(object):

    def __init__(self, filePath):
        self.count = 0
        self.filePath = filePath
        self.analysisDetails = []
        self.analysisDetails = self.run()

    def run(self):
        print(self.filePath)
        with open(self.filePath, newline='\n') as csvfile:
            rows = csv.DictReader(csvfile)
            # print(rows)
            for row in rows:
                self.count += 1
                if row['Value'].__contains__(" "):
                    self.analysisDetails.append(CountryWiseDeathDetails(int(row['TIME']), row['GEO'], row['SEX'],
                                                                        int(row['Value'].split(" ")[1])))
                elif not row['Value'].isnumeric():
                    self.analysisDetails.append(CountryWiseDeathDetails(int(row['TIME']), row['GEO'], row['SEX'], 0))
                else:
                    self.analysisDetails.append(CountryWiseDeathDetails(int(row['TIME']), row['GEO'], row['SEX'],
                                                                        int(row['Value'])))
            return self.analysisDetails

    def totalDeathsByCountry(self):

        x = list(map(lambda r: CountryWiseDeathDetails(r.year, r.country.upper(), r.gender.upper(), r.deaths)
                     , self.analysisDetails))
        x = list(filter(lambda e: e.deaths != 0, x))
        dictMap = {}
        for detail in x:
            if detail in dictMap:
                dictMap[detail] += detail.deaths
            else:
                dictMap[detail] = detail.deaths

        return dictMap


if __name__ == '__main__':
    current_time = time.time()
    print("no of available CPUs:", multiprocessing.cpu_count())
    print("current_time", current_time)
    details = CountryWiseDeathAnalysis("/Users/dpq/Desktop/techWorrk/inputFiles/datasets"
                                       "/worldwiseCauseOfDeaths.csv")
    print("Total rows:", details.count)
    # print(len(details.analysisDetails))
    # print(len(details.totalDeathsByCountry()))

    # for detail in details.totalDeathsByCountry(): print(detail)

    print("--- %s seconds ---" % (time.time() - current_time))
