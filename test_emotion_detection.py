import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        for statement, expected_emotion in test_cases.items():
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
                result_dict = eval(result)  
                self.assertEqual(result_dict['dominant_emotion'], expected_emotion)

if __name__ == '__main__':
    unittest.main()