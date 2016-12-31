# CP2104 to serLCD test
Just a simple python sketch to test [Silicon Labs CP2104](https://www.silabs.com/products/interface/Pages/cp2104-mini.aspx).

The CP2104 is a USB to UART bridge.  This allows serial communication over USB.  When the device is attached to a USB port, it will appear as a serial interface. _In my case `/dev/ttyUSB0`._  

### What do I do?
To test this device, connect the TX pin of the CP2104 to the RX pin of a [sparkfun serLCD backpack](https://www.sparkfun.com/products/258) that was driving a 16x2 LCD display. Connect the CP2104 to the computer via USB verify that it appears as `/dev/ttyUSB0`.  
This python sketch will send keypress characters via serial communication to be rendered on the LCD.  You will need the pySerial and Curses modules installed.  

---
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Some python and a serLCD to get familiar with <a href="https://twitter.com/siliconlabs">@siliconlabs</a> CP2104 USB bridge. <a href="https://t.co/lfhpHADruB"><img src="https://pbs.twimg.com/ext_tw_video_thumb/814962230852612096/pu/img/7YcFwOSKrUJtmyJK.jpg" /></a></p>&mdash; R̸y̧an͝ ͝Ol҉es (@rho_) <a href="https://twitter.com/rho_/status/814962356681842688">December 30, 2016</a></blockquote>
