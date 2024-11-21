import unittest
from unittest.mock import MagicMock, patch
import json
import random

# Assuming your script is named mqtt_script.py
from mqtt_script import on_connect, on_message, mqttc

class TestMQTTClient(unittest.TestCase):

    @patch('mqtt_script.mqtt.Client')
    def setUp(self, MockMQTTClient):
        self.client = MockMQTTClient.return_value
        self.client.subscribe = MagicMock()
        self.client.publish = MagicMock()
        self.client.loop_forever = MagicMock()

    def test_on_connect(self):
        # Simulate the on_connect callback
        on_connect(self.client, None, None, 0, None)
        self.client.subscribe.assert_called_with("ecub/tx")
        self.client.subscribe.assert_called_with("ecuf/tx")

    @patch('mqtt_script.random.randint', return_value=5)  # Mock random.randint
    def test_on_message_valid(self, mock_randint):
        # Simulate a valid MQTT message
        msg = MagicMock()
        msg.payload.decode.return_value = json.dumps({"user": "test_user", "command": "to_ecub", "data": "test_data"})
        msg.topic = "ecub/tx"

        on_message(self.client, None, msg)

        expected_data = "{\"user\":\"test_user\",\"command\":\"ecu\", \"data\":\"test_data_5\"}"
        self.client.publish.assert_called_with('ecub/rx', expected_data, qos=1)

    def test_on_message_invalid_json(self):
        # Simulate an invalid JSON message
        msg = MagicMock()
        msg.payload.decode.return_value = "invalid_json"
        msg.topic = "ecub/tx"

        with self.assertLogs(level='ERROR') as log:
            on_message(self.client, None, msg)
            self.assertIn("Error: Cannot parse:", log.output[0])

    def test_on_message_missing_key(self):
        # Simulate a message missing the 'command' key
        msg = MagicMock()
        msg.payload.decode.return_value = json.dumps({"user": "test_user", "data": "test_data"})
        msg.topic = "ecub/tx"

        with self.assertLogs(level='ERROR') as log:
            on_message(self.client, None, msg)
            self.assertIn("Error: Cannot parse:", log.output[0])

if __name__ == '__main__':
    unittest.main()