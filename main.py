import CameraManager
import FlightController
import Classifier
if __name__ == "__main__":
    flight_controller = FlightController()
    camera = CameraManager.CameraManager(0)
    classifier = Classifier()
    while True:
        frame = camera.getFrame()
        height, width, channels = frame.shape
        goalCord, _ = classifier.classify(frame)
        flight_controller.moveByCord(goalCord,width,height)