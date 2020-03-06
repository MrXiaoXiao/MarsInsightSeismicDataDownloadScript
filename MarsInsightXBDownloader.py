# A simple script for downloading Mars Insight Seismic Data from IRIS
import obspy
import os
import argparse
from obspy.clients.fdsn import Client
from obspy.clients.fdsn.mass_downloader import CircularDomain, Restrictions, MassDownloader

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mars Insight Data Download Script')
    parser.add_argument('--folder', dest='download_folder', type=str, help='Download Folder')
    args = parser.parse_args()

    if os.path.exists(args.download_folder):
        pass
    else:
        os.makedirs(args.download_folder)
    
    client = Client("IRIS")
    # download station inventory
    inv = client.get_stations(network='XB',startafter='2015-01-01')
    inv.write(args.download_folder+'/'+'XB_stations.xml',format='STATIONXML')
    # set domain
    domain = CircularDomain(latitude=4.502384, longitude=135.623447,
                            minradius=0.0, maxradius=90.0)
    # set restrictions
    restrictions = Restrictions(
    # start & end time
    starttime=obspy.UTCDateTime(2018, 12, 20, 0, 0, 0),
    endtime=obspy.UTCDateTime(2019, 10, 1, 0, 0, 0),
    # chunklength (86400s = 1 day)
    chunklength_in_sec=86400,
    reject_channels_with_gaps=False,
    minimum_length=None,
    network="XB",
    channel_priorities=["???"],
    location_priorities=["??"])

    # start download
    mdl = MassDownloader(providers=["IRIS"])
    mdl.download(domain, restrictions, mseed_storage=args.download_folder+'/'"waveforms",
                 stationxml_storage=args.download_folder+'/'"stations")