from PingProbe import PingProbe as probe
import sys
from CustomExceptions import IncorrectJSONLoadException, WrongFormatInt

def changeproberatio(value, probejson):
    """
    Function to change the value of the ratio of a probe via command (e.g., "python ChangeProbeRatio 16, 'myprobe.json')
    Probe information on the database will be updated on next startup

    :param value: Int. The value to change the address into
    :param probejson: String. The quick-reference json from which we start the probe
    :return: None
    """
    if not isinstance(probejson, str):
        raise IncorrectJSONLoadException(probejson)

    if not isinstance(value, int):
        raise WrongFormatInt("New ratio", value)

    myprobe = probe.openprobe(probejson)
    myprobe.changeratio(probejson, value)

changeproberatio(sys.argv[1], sys.argv[2])