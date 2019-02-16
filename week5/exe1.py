from __future__ import print_function, unicode_literals
import pyeapi
import six


def pyeapi_result(output):
    """Return the 'result' value from the pyeapi output."""
    return output[0]['result']


def main():
    """Use Arista's eAPI to obtain 'show interfaces' from the switch."""
    eapi_conn = pyeapi.connect_to("switch1")

    interfaces = eapi_conn.enable("show interfaces")
    interfaces = pyeapi_result(interfaces)

    # Strip off unneeded dictionary
    interfaces = interfaces['interfaces']

    # inOctets/outOctets are fields inside 'interfaceCounters' dict
    data_stats = {}
    for interface, int_values in interfaces.items():
        int_counters = int_values.get('interfaceCounters', {})
        data_stats[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))

    # Print output data
    print("\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets"))
    for intf, octets in sorted(data_stats.items()):
        print("{:20} {:<20} {:<20}".format(intf, six.text_type(octets[0]),
                                           six.text_type(octets[1])))

    print()


if __name__ == '__main__':
    main()
