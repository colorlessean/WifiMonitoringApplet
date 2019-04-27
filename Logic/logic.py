# Modules to be imported for usage
import subprocess

# Constants for conversion
MSEC_TO_SEC = 1000000
SYMETRY_CONVERSION = 2
B_TO_MB = 1024

# Main function of the Logic Package responsible for returning ping information
# Runs function to ping the websites and packages data into Matplotlib readable format to return on
def logic(filename):

    for i in range(0, 100):
        if i % 10 == 0:
            print(pingWebsites())
            
        
    

    return

# Function that runs over all of the websites to ping and packages data into list of sitename speed pairs
def pingWebsites():
    # "Constants" to be used in execution
    sitesToPing = ["google.com", "yahoo.com", "bing.com", "learn.uwaterloo.ca"]

    # Array of pairs of sitename and speed of connection to site
    output = []

    # Runs the pingWebsite function on each site in list
    for site in sitesToPing:
        output.append([site, pingWebsite(site)])

    return output

# Function to ping website address passed in a single time
# *param    address value of the website to ping
# *returns  number value of the speed
def pingWebsite(websiteAddr, debug=False):
    args = ['ping', websiteAddr, '-n', '1', '-w', '100']
    process = subprocess.Popen(args,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    stdout, stderr = process.communicate()
    cmdReturn = str(stdout)
    
    # Print to console the command output
    if cmdReturn is not None:
        if debug:
            print(stdout)
    if stderr is not None:
        if debug:
            print(stderr)
        return -1

    # Analyze stdout string to get valuable information
    byteStr = "bytes="
    byteStart = cmdReturn.find(byteStr)
    byteEnd = cmdReturn.find(" ", byteStart)
    packetSizeStr = cmdReturn[byteStart+len(byteStr):byteEnd]

    timeStr = "time="
    timeStart = cmdReturn.find(timeStr)
    timeEnd = cmdReturn.find("ms" , timeStart)
    roundTripTimeStr = cmdReturn[timeStart+len(timeStr):timeEnd]

    try:
        packetSize = int(packetSizeStr)
        roundTripTime = int(roundTripTimeStr)
    except Exception as ex:
        if debug:
            print(ex)
        return -1

    # print(packetSize, roundTripTime)

    # Calculate the throughput speed
    # Multiply by 2 to give an average value for up/down (usually not symetrical however)
    speed = (packetSize * MSEC_TO_SEC * SYMETRY_CONVERSION) / (roundTripTime * B_TO_MB**2)
    if debug:
        print(str(speed) + " B/s Up and Down Averaged")

    return speed

def outputToFile(filename):


    return