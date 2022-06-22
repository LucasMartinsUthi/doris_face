#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16, Empty

from doris_face.srv import SetEmotion

EMOTIONS = {
    "Normal": 0,
    "Happy": 1,
    "Sad": 2,
    "Rage": 3,
    "Scared": 4,
}

class EmotionController():

    def __init__(self):
        self.publisher = rospy.Publisher('emotion', Int16, queue_size=10)
        self.set_emotion_service = rospy.Service('set_emotion', SetEmotion, self.setEmotion)

        rospy.init_node('emotion_controller')
        
        rospy.spin()
        
    def getEmotion(self):
        return self.emotion

    def setEmotion(self, emotion):
        self.emotion = emotion.emotion
        self.emotionPub()

        return self.emotion

    def emotionPub(self):
        print(self.emotion)
        self.publisher.publish(self.emotion)


if __name__ == '__main__':
    try:
        EmotionController()
    except rospy.ROSInterruptException:
        pass