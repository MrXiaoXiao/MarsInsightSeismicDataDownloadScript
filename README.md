# MarsInsightSeismicDataDownloadScript
This is a simple script to automatically download Mars Insight seismic data from IRIS.

The script is for convenience of those not familiar with FDSN web service.

For information on SEIS raw data, Insight Mission

Please see http://datacenter.ipgp.fr/networks/detail/XB_2016/

and

https://www.iris.edu/hq/sis/insight

To use script, you need to have Python3(https://www.python.org) and Obspy(https://github.com/obspy/obspy) installed.

Then, run

python MarsInsightXBDownloader.py --folder SAVE_PATH  

![Example Image](https://github.com/MrXiaoXiao/MarsInsightSeismicDataDownloadScript/blob/master/example_waveform_image.png)
