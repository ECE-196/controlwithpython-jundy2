### How does the DevBoard handle received serial messages? How does this differ from the naïve approach?

For the devboard to handle recieve messages it performs the following steps .

- First, it uses the `USBSerial.onEvent(ARDUINO_HW_CDC_RX_EVENT, on_receive);` function, to trigger the callback `on_recieve` when a byte over serial is received from entering the `ARDUINO_HW_CDC_RX_EVENT` command. 
  
- When `on_recieve` is triggered, it will take an incoming serial message and handle it. 

- If the incoming signal is neither a `LOW` or `HIGH`  signal it will send an error, otherwise it will trigger the corresponding LED state. 

- This differs from the naïve approach of simply recieving a signal constantly in the `void loop()` function because it gives our code the option to listen for an event that occurs and perform a given function when needed, and not coninously run.

### What does `detached_callback` do? What would happen if it wasn't used? 

If detached_callback was not used, then what would happen is we would not be able to pass the `update_led()` function into our decorator, `detached_callback`. The implication of this is that we would not be able to spin up our thread on the `update_led()` function.

### What does `LockedSerial` do? Why is it _necessary_?
LockedSerial is a wrapper function for the serial class and its necessary because it performs a lock on threads. More specifically, it grants a LockedSerial object ownership of the lock, and stop other threads from reading and writing bytes until it has finished doing so to avoid intermingling of data.