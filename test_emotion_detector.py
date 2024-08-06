from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    ''' unit testing class for emotion detector '''

    def test_emotion_detector(self):
        ''' unit test method for emotion detector '''

        test_data_list = [
            {'input' : 'I am glad this happened', 'output' : 'joy'},
            {'input' : 'I am really mad about this', 'output' : 'anger'},
            {'input' : 'I feel disgusted just hearing about this', 'output' : 'disgust'},
            {'input' : 'I am so sad about this', 'output' : 'sadness'},
            {'input' : 'I am really afraid that this will happen', 'output' : 'fear'}
        ]

        for test_data in test_data_list:
            self.assertEqual(emotion_detector(test_data['input'])['dominant_emotion'],test_data['output'])

unittest.main()