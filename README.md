# simple-transmitter-model

## Task      
Implement Transmit-Receive model:          
__"alphabet -> bits -> complex numbers(signal)"__           
--> __"complex numbers(signal) -> bits -> alphabet"__    

## Work
### encoder
Is responsible for user input:
* encoding
* message
* message to bits
* bits to signal by QPSK
### decoder
Is responsible for receiving signal and translating it to readable message
### Catches
- There is _packet_ and _depacket_ packages for _decoder_ to understand in which encode _encoder_ send message:
    - __4 bits__ -- constant part
    - __2 bits__ -- encoding
- There is 3 versions of _main.py_ :
    - __decoder main__ -- don't receive anything by self, in code need to paste _list[complex]_ (signal) into _mess_ variable
    - __encoder main__ -- take user input and writes in console -- bit message, packet bit message and signal
    - __workspace main__ -- unite _decoder_ and _encoder_ parts into one working model
