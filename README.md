# Cisco-MAC-to-PC-MAC
Converts a file with a list of Cisco formatted MAC Addresses to PC formatted MAC Addresses... <br><br>
Ex:
  ```
  abcd.efgh.ijkl
  ```
  to
  ```
  AB:CD:EF:GH:IJ:KL:
  ```
<br>
The purpose is to take a "sh ip arp" from a Cisco switch, copy out the mac address list to a file, have the file then convert this into a PC formatted MAC address list, and save the results to a new file, which when added to the existing "sh ip arp" data produces a searcharble list of data

## Output:
![image](https://user-images.githubusercontent.com/48565067/140577187-4ced615b-5f19-4ded-9f95-2c16bb29793b.png)
