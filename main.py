from gpiozero import MCP3008

from time import sleep



# MCP3008?ch0????

adc = MCP3008(channel=0)



while True:

    # ??0.0?1.0?????????

    value = adc.value

    print("value: {:.3f}".format(value))

    sleep(1)  # 1???
