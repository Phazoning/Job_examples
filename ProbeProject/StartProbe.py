from PingProbe import PingProbe as probe
import sqlite3 as lite
import atexit as atex
import json as js


def startprobe():
    """
    This function exists as a way to start in-server the probing. It must be terminated manually via server interaction
    IMPORTANT: The database used here is a local sqlite one, oneself has to modify the code and imports according to
    their needs (e.g. by using an external MySQL database to coordinate all the probes). Nonetheless, it's recommended
    only to change the connection object because the cursors and queries are usually common

    :return: None
    """
    def checkprobe():
        """
        This function checks if the probe exists in the database
        :return: Boolean. True if it has found the probe in the database, False if it hasn't
        """
        query = f"select * from Probes where Probe_name = {mainprobe.name} and Dominion = {mainprobe.dominion};"
        cur.execute(query)
        if len(cur.fetchall()) > 0:
            return False
        else:
            return True

    def deactivate():
        """
        Cleanup function executed when the script is terminated. It sets the probe as inactive,
        then dumps the data in the csv to the database, then it backups the csv dump file,
        cleans it and terminates the connection.
        :return:
        """
        query = f"update table Probes set Status = 'Inactive' where Name = {mainprobe.name} and " \
        f"Dominion = {mainprobe.dominion};" #this query should go to an exteral db
        cur.execute(query)
        for qry in mainprobe.getinsertqueries("Registries"):
            cur.execute(qry)
        conn.commit()
        mainprobe.createbackupcsv()
        mainprobe.clearcsvdumpfile()
        conn.close()

    def checkdbinformation():
        """
        Function to know if the address, the ratio, or both have been altered from the originals in the database

        :return: ret, list. Parameters which have been altered
        """
        ret = []
        querybase = f"select * from Probes where Dominion = {mainprobe.dominion} and Probe_name = {mainprobe.name}"
        ex1 = cur.execute(f"{querybase} and Address = {mainprobe.address};")
        if len(ex1.fetchall()) < 1:
            ret.append("Address")
        ex2 = cur.execute(f"{querybase} and Ratio = {mainprobe.ratio};")
        if len(ex2.fetchall()) < 1:
            ret.append("Ratio")
        return ret

    mainprobe = probe.openprobe("probeparameters.json")
    conn = lite.connect("Probe.db")
    cur = conn.cursor()

    if checkprobe(): #This creates the probe in-database just in case it hadn't been created before
        dic = js.load(mainprobe.getprobefortable())
        values = ", ".join([dic["name"], dic["dominion"], dic["address"], dic["ratio"], dic["status"]])
        query = f"insert into Probes (Probe_name, Dominion, Address, Ratio, Status) values ({values});"
        cur.execute(query)
        conn.commit()

    elif len(checkdbinformation()) > 0: #This updates the registries in the database where them to differ
        dic = {
            "Address": mainprobe.address,
            "Ratio": mainprobe.ratio
        }
        values = f""
        for e in checkdbinformation():
            values += f"{e} = {dic[e]}"
            if checkdbinformation().index(e) != len(checkdbinformation()) - 1:
                values += ", "

        query = f"update table Probes set {values} where Dominion = {mainprobe.dominion} and Probe_name = {mainprobe.name};"
        cur.execute(query)
        conn.commit()

    else:
        pass

    atex.register(deactivate) #This code will be executed when the script is terminated

    mainprobe.probetarget()
