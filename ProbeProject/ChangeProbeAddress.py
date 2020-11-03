from PingProbe import PingProbe as probe
import sys
from CustomExceptions import IncorrectJSONLoadException, WrongFormatString


def changeprobeaddress(value, probejson):
    """
    Function to change the value of the address of a probe via command
    (e.g., "python ChangeProbeRatio '0.0.0.0', 'myprobe.json'). Probe information on the database
    will be updated on next startup.

    :param value: String. The value to change the address into
    :param probejson: String. The quick-reference json from which we start the probe
    :return: None
    """
    if not isinstance(probejson, str):
        raise IncorrectJSONLoadException(probejson)

    if not isinstance(value, str):
        raise WrongFormatString("New address", value)

    myprobe = probe.openprobe(probejson)
    myprobe.changeaddress(probejson, value)

changeprobeaddress(sys.argv[1], sys.argv[2])