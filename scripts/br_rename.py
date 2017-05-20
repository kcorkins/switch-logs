#!/usr/bin/python

"""
This script renames files from the naming scheme provided by the customer, to
something that makes a bit more sense.

 ***WARNING*** this script will rename files without prompting!
 ***DO NOT RUN ON RENAMED FILES!*****

Origininal file name format:
CH1-EXT1_IOMOdule1-20171605_1554.txt
Chassis-port-module-data_time

New format;
CHx-IOMx-ports_br_date_time.txt

Translations;
Chassis:
CHx (should stay the same)

IO Module:
IOMOduleX = IOMx  (2 choices, 1 or 2, drop 'Odule')

Port:
 After digging through the files, the following is an accurate description
 of the contents of the files;
  EXT1 = EXT1-2
  EXT2 = EXT3-4
  EXT3 = INTA1-7
  EXT4 = INTA8-14

Insert filetype:
 br for bitrate = _br_

Date_Time:
 leave as is, including .txt file extension
 remove any spaces in filenames

"""
import os

def  main():
    # roll through files in folder
    mydir = os.getcwd()
    for filename in os.listdir(mydir):
        if filename.endswith('.txt'):  # only process text files. may need .log too
            tmp = filename.split("-")
            # "-" returns: ['CH9', 'EXT4_IOMOdule2', '20171605_1554.txt']
            chassis = tmp[0]  # Chassis ID

        # work on middle section ex. EXT4_IOMOdule2
            mod = tmp[1]  # port and module
            tmp_mod = mod.split("_")
    
            # now lets transform the port names
            port_id = tmp_mod[0]  # ex. EXT4
            # make the changes to port names base on decoder ring
            if port_id == "EXT1":
                port_id = "EXT1-2"
            elif port_id == "EXT2":
                port_id = "EXT3-4"
            elif port_id == "EXT3":
                port_id = "INTA1-7"
            elif port_id == "EXT4":
                port_id = "INTA8-14"

            # Rename module section. Only two choices 1 or 2
            mod_id = tmp_mod[1]  # ex. IOMOdule2
            if mod_id == "IOMOdule1":
                mod_id = "IOM1"
            elif mod_id == "IOMOdule2":
                mod_id = "IOM2"
            date = tmp[2]  # takes the last portion of filename, including ext
            # print chassis, mod, date
            new_name = chassis + "_" + mod_id + "_" + port_id + "_br_" + date

            # rename files
            print "renaming " + filename + " to: " + new_name
            os.rename(filename, new_name)

if __name__ == '__main__':
    main()
