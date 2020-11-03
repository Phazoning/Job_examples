import time
import pythonping as pyping
import json as js
from datetime import datetime as dati
from CustomExceptions import WrongFormatString, WrongFormatInt, IncorrectJSONLoadException, UndefinedThresholdError


class PingProbe:

    class Threshold:

        def __init__(self, lower_level_number, higher_level_number):
            """
            This method is the constructor method. The meaning of the parameters is explained below.

            :param lower_level_number: Int. The lowest number in the threshold.
            :param higher_level_number: Int.The highest number in the threshold.
            """
            if not isinstance(lower_level_number, int):
                raise WrongFormatInt("Lower lever number ", lower_level_number)
            elif not isinstance(higher_level_number, int):
                raise WrongFormatInt("Higher level number ", higher_level_number)
            self.lower = lower_level_number
            self.higher = higher_level_number

        def numberinthreshold(self, number):
            if self.lower <= number <= self.higher:
                return True
            else:
                return False

    def __init__(self, probename, probedominion, probeaddress, proberatio, probestatus="Inactive"):
        """
        This method is the constructor method. The meaning of the parameters is explained below

        :param probename: String. The name of the probe
        :param probedominion: String. The dominion the probe belongs to
        :param probeaddress: String. The address the probe is going to ping to
        :param proberatio: Int. How many seconds does the probe wait between pings
        :param probestatus: String. The status of the probe, "Inactive" by default. This is merely informative
        """
        if not isinstance(probename, str):
            raise WrongFormatString("Probe name", probename)
        self.name = probename

        if not isinstance(probedominion, str):
            raise WrongFormatString("Probe dominion", probedominion)
        self.dominion = probedominion

        if not isinstance(probeaddress, str):
            raise WrongFormatString("Probe address", probeaddress)
        self.address = probeaddress

        if not isinstance(proberatio, int):
            raise WrongFormatInt("Probe ratio", proberatio)
        self.ratio = proberatio

        if not isinstance(probestatus, str):
            raise WrongFormatString("Probe status", probestatus)
        self.status = probestatus

        self.dumpcsv = f"{self.dominion}_{self.name}_dump_csv.csv" #csv the information is dumped into

    def probetarget(self, timeout=300):
        """
        Method to continuously probe the address. It must be forcefully terminated via server interaction"

        :param timeout: Int. How many seconds does it wait before declaring a connection timeout. Set by default at 300
        :return: None
        """
        def averageping(responses):
            """
            Function to get the average ping of the set of 4 ping responses object

            :param responses: List. List of the ping responses (which are Response objects)
            :return: Int. Average of the pings in the responses
            """
            k = 0
            for e in responses:
                k += e.time_elapsed_ms
            return round(k/len(responses))

        if not isinstance(timeout, int):
            raise WrongFormatInt("Timeout", timeout)

        if timeout < self.ratio:
            tout = self.ratio
        else:
            tout = timeout

        start = int(time.time())

        self.status = "active"

        with open(self.dumpcsv, "w+") as file: #Need to create a way to know if there is a backup file of the data
            file.write("Dumpdate;Dumptime;Address;Ping;Status;Code")

        while True:
            current = dati.now()
            timediff = int(time.time()) - start

            if timediff % self.ratio > 0:
                pass
            else:
                try:
                    pyng = pyping.ping(self.address, tout)
                    avgping = averageping(pyng._responses)
                    status, code = self.__compareping__(avgping, pyng)

                except RuntimeError:
                    status = "Connection error"
                    code = "Blue"
                    avgping = 0

                chkdate = "-".join([str(current.day), str(current.month), str(current.year)]) #ISO format SQL datetype format
                chktime = ":".join([str(current.hour), str(current.minute), str(current.second)])

                line = ";".join([chkdate, chktime, self.address, str(avgping), status, code])
                with open(self.dumpcsv, "a+") as file:
                    file.write(line + "\n")
                time.sleep(self.ratio - 1)

    def getprobefortable(self):
        """
        Method to export the probe parameters as a JSON file. It doesn't return it, it just dumps the data into a file

        :return: None
        """
        outdict = {"Probe_name": self.name,
                   "Dominion": self.dominion,
                   "Address": self.address,
                   "Ratio": self.ratio,
                   "Status": self.status
                   }

        with open("_".join([self.name, self.dominion, self.address]) + "_tosql.json", "w+") as targetjson:
            js.dump(outdict, targetjson)

    def clearcsvdumpfile(self):
        """
        Method to clear the csv file where the information is being dumped into.
        Checks if there's a backup before deleting and, if there isn't, it creates it.

        :return: None
        """
        current = dati.now()
        chkdate = f"{current.year}/{current.month}/{current.day}"
        filename = f"backup_dump_{chkdate}.csv"
        with open(filename, "r+") as file:
            if len(list(file)) < 1:
                inp = input("There is no backup, are you sure you want to clear the dump csv? (Y/N)\n")
                if inp.lower() == "yes" or inp.lower() == "y":
                    with open(self.dumpcsv, "r+") as orifile:
                        orifile.truncate()
                elif inp.lower() == "no" or inp.lower() == "n":
                    print("Aborting csv clearing")
                    return None
                else:
                    print("Unrecognized choice, aborting")
                    return None

    def createbackupcsv(self):
        """
        Method to create a backup for the csv where the information is dumped into

        :return: None
        """
        current = dati.now()
        chkdate = chkdate = f"{current.year}/{current.month}/{current.day}"
        filename = f"backup_dump_{chkdate}.csv"
        with open(self.dumpcsv, "r") as file:
            with open(filename, "a+") as target:
                if len(list(target)) > 0:
                    print("There was already a backup, it'll be overwritten\n")
                for e in file:
                    target.write(e)

    def getinsertqueries(self, tablename):
        """
        Method to generate the queries to insert the data from the dump csv into a third

        :param tablename: String. Name of the table the data is to be inserted into
        :return: None
        """
        if not isinstance(tablename, str):
            raise WrongFormatString("Table name", tablename)

        ret = []
        with list(open(self.dumpcsv)) as flist:
            for e in flist[1:]:
                values = e.replace(";", ", ")
                names = flist[0].replace(";", ", ")
                sentence = f"insert into table {tablename} (Dominion, Probe_name, {names}) " \
                           f"values ({self.dominion}, {self.name}, {values})"
                ret.append(sentence)

        return ret

    def __compareping__(self, ms, pingobject):
        """
        Method to compare if the ping is inside a threshold.
        Said threshold is a Threshold nested object for the sake of simplicity. Also, thresholds are loaded from
        the file "thresholds.json". More information on the documentation.

        :param pingobject PingObject. The object which pings the address.
        :param ms Int. The (average) ping to be analyzed.

        :returns status, code String, String. The first is the status of the connection, the second is the
                 code denomitation of the former

        :except UndefinedThresholdError, if there isn't a threshold the value belongs into
        """
        pg = pingobject
        status = "foo"
        code = "foo"
        with open("thresholds.json", "r") as file:
            jsdic = js.load(file)
            found = False
            index = 0

            while not found:
                currentitem = jsdic[str(index)]
                thre = self.Threshold(currentitem["lower"], currentitem["higher"])

                if pg.success() and thre.numberinthreshold(ms):
                    status = currentitem["status"]
                    code = currentitem["code"]
                    found = True

                elif index >= len(jsdic):
                    raise UndefinedThresholdError

        return status, code

    @classmethod
    def openprobe(cls, jsonfile):
        """
        Method to create a PingProbe object from a json file. Made as a quick way to start up the probe
        :param jsonfile: String. Name of the .json file which we are to use to create our PingProbe object
        :return: PingProbe. A pingprobe object  using the parameters in the json
        """
        if not isinstance(jsonfile, str):
            raise IncorrectJSONLoadException(jsonfile)

        with open(jsonfile, "r") as file:

            jfile = js.load(file)
            return PingProbe(jfile["name"], jfile["dominion"], jfile["address"], jfile["ratio"])

    @staticmethod
    def changeaddress(jsonfile, value):
        """
        Method to reconfigure the address of a probe. This is made to, along with the ChangeProbeAddress.py file,
        change from the outside the contents of the probe (e.g. by using a jython script call from a java script)

        :param jsonfile: String. The json file we use to load our probe
        :param value: String. The new value we want to change the address to
        :return: None
        """
        if not isinstance(jsonfile, str):
            raise IncorrectJSONLoadException(jsonfile)

        if not isinstance(value, str):
            raise WrongFormatString("New address ", value)

        jdict = {}

        with open(jsonfile, "r") as json:
            jdict = js.load(json)
            jdict["address"] = value

        with open(jsonfile, "w") as json:
            js.dump(jdict, json)

    @staticmethod
    def changeratio(jsonfile, value):
        """
                Method to reconfigure the ratio of a probe. This is made to, along with the ChangeProbeRatio.py file,
                change from the outside the contents of the probe (e.g. by using a jython script call from a java script)

                :param jsonfile: The json file we use to load our probe
                :param value: The new value we want to change the ratio to
                :return: None
                """
        if not isinstance(jsonfile, str):
            raise IncorrectJSONLoadException(jsonfile)

        if not isinstance(value, int):
            raise WrongFormatInt("New address ", value)

        jdict = {}

        with open(jsonfile, "r") as json:
            jdict = js.load(json)
            jdict["ratio"] = value

        with open(jsonfile, "w") as json:
            js.dump(jdict, json)