import time
import frida
import requests


def my_message_handler(message, payload):
    print("message=>", message)
    print("payloa=>d", payload)


device = frida.get_usb_device(10)
# device = frida.get_device_manager().add_remote_device("192.168.0.102:8888")
print('设备=>', device)

session = device.attach("猿人学2022")
print('session=>', session)
#
# # load script
with open("./js/second.js", encoding="utf-8") as f:
    script = session.create_script(f.read())
#
script.on("message", my_message_handler)
script.load()


res = script.exports.invokesign("6:1645678987")
print(res)


