import pexpect
from server import logger

""" 
This class is a wrapper for the Seefood AI. It wraps the functions of the AI into 
an easily interactable class that the API can call upon.
"""

class SeefoodWrapper:

    # Constructor
    def __init__(self):
        self.ready = False
        # Spawns subprocess
        try:
            self.process = pexpect.spawn("python  find_food.py", timeout=60)
            print("SeefoodWrapper: Starting Seefood AI")
            logger.write_info("SeefoodWrapper: Starting Seefood AI")
            self.process.expect("Setup Complete")
            logger.write_info("Setup Complete")
        except:
            logger.write_error("Setup Failed: {}".format(self.process.before))

    # Getter
    def isReady(self):
        return self.ready

    # Polls the AI for the ready signal, which is "Enter file path to food: "
    def pollForReady(self):
        try:
            print("SeefoodWrapper: Polling seefood for readiness")
            logger.write_info("SeefoodWrapper: Polling seefood for readiness")
            self.process.sendline("ready")
            self.process.expect("Enter file path to food: ")
            print("SeefoodWrapper: Seefood AI is ready")
            logger.write_info("SeefoodWrapper: Seefood AI is ready")
            self.ready = True
        except:
            print("SeefoodWrapper: Couldn't poll for AI readiness")
            logger.write_error("SeefoodWrapper: Couldn't poll for AI readiness")

    # Takes in a path to an image, sends it to the Seefood AI, checkpoints each step of the conversion and returns
    # two floats which are the two confidence ratings of the Seefood AI.
    # the first float is how confident the AI is that the image is food and the second float is how confident the
    # AI is that the image isn't food
    def sendImage(self, string):
        try:
            print("SeefoodWrapper: Scanning image " + string + " for food")
            logger.write_info("SeefoodWrapper: Scanning image " + string + " for food")
            
            # send over image path
            self.process.send(string + "\n")
            
            # wait for checkpoint to telling us the image is being scanned
            print (self.process.before)
            print(self.process.after)
            self.process.expect("looking for food in " + string)
            print (self.process.before)
            print(self.process.after)
            print ("SeefoodWrapper: Hit 'looking for food' checkpoint")
            logger.write_info("SeefoodWrapper: Hit 'looking for food' checkpoint")
            # wait for checkpoint telling us image has completed scanning
            self.process.expect("Scanning Complete")
            print (self.process.before)
            print(self.process.after)
            print ("SeefoodWrapper: Hit 'Scanning Complete' checkpoint")
            logger.write_info("SeefoodWrapper: Hit 'Scanning Complete' checkpoint")
            # parse confidence ratings 
            confidences = self.process.before
            for char in '[]\n\r':
                confidences = confidences.replace(char, '')

            confidencesArr = confidences.split(" ")
            finalArr = []
            for string in confidencesArr:
                if string != '':
                    finalArr.append(string)

            self.ready = False
            print ("SeefoodWrapper: Confidence rating is: " + finalArr[0] + " " + finalArr[1])
            logger.write_info("SeefoodWrapper: Confidence rating is: " + finalArr[0] + " " + finalArr[1])
            
            return finalArr
        except:
            print ("SeefoodWrapper: Error, Cannot process image for food")
            logger.write_error("SeefoodWrapper: Error, Cannot process image for food")




    
