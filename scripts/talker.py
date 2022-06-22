#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16

EMOTIONS = {
    "Normal": 0,
    "Happy": 1,
    "Sad": 2,
    "Rage": 3,
    "Scared": 4,
}
class emotionController():

    def __init__(self):
        self.emotion = EMOTIONS["Normal"]
        self.emotion_pub()

    def emotion_pub(self):
        rospy.init_node('emotion_talker', anonymous=True)

        pub = rospy.Publisher('emotion', Int16, queue_size=10)
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            rospy.loginfo(self.emotion)
            pub.publish(self.emotion)
            
            rate.sleep()

    def getEmotion(self):
        return self.emotion

    def setEmotion(self, emotion):
        self.emotion = emotion

if __name__ == '__main__':
    try:
        emotionController()
    except rospy.ROSInterruptException:
        pass