while True:

    from urllib import request

    url = "http://192.168.0.102:8080/DDR_20210729_004311.csv"
    response = request.urlopen(url)
    line = response.read().decode('latin-1')
    outFileName="OBStime.txt"
    outFile=open(outFileName, "w")
    outFile.write(line[-7:])
    outFile.close()
