
E24 = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]

magnitude = ["R", "K" , "M"]

package = ["0402" , "0603" , "0805" , "1206" ]


def write_component(value , package):

    if package == "0402":
        footprint   = "F2 \"Resistor_SMD:R_0402_1005Metric\" -150 0 50 V I C CNN\n"
        gr_val      = "GR_0402_"+value
        description = "D Generic 0402 resitor "+value+" 1% 63mW 50V" +"\n"
    if package == "0603":
        footprint   = "F2 \"Resistor_SMD:R_0603_1608Metric\" -150 0 50 V I C CNN\n"
        gr_val      = "GR_0603_"+value
        description = "D Generic 0603 resitor "+value+" 1% 100mW 75V" +"\n"
    if package == "0805":
        footprint   = "F2 \"Resistor_SMD:R_0805_2012Metric\" -150 0 50 V I C CNN\n"
        gr_val      = "GR_0805_"+value
        description = "D Generic 0805 resitor "+value+" 1% 125mW 150V" +"\n"
    if package == "1206":
        footprint   = "F2 \"Resistor_SMD:R_1206_3216Metric\" -150 0 50 V I C CNN\n"
        gr_val      = "GR_1206_"+value
        description = "D Generic 1206 resitor "+value+" 1% 250mW 200V" +"\n"

    # generic definition in dcm file
    file_dcm.write("#"+"\n")
    file_dcm.write("$CMP "+ gr_val +"\n")
    file_dcm.write(description)
    file_dcm.write("F ~" +"\n")
    file_dcm.write("$ENDCMP" +"\n")

    # component - symbol and parameters
    file_lib.write("#\n")
    file_lib.write("# " + gr_val +"\n")
    file_lib.write("#\n")
    file_lib.write("DEF " + gr_val + " R 0 0 N Y 1 F N\n")
    file_lib.write("F0 \"R\" -70 0 50 V V C CNN\n")
    file_lib.write("F1 \""+gr_val+"\" 0 0 50 V I C CNN\n")
    file_lib.write(footprint)
    file_lib.write("F3 \"\" -195 -50 50 V I C CNN\n")
    file_lib.write("F4 \""+value+"\" 75 0 50 V V C CNN \"Resistance\"\n")
    file_lib.write("F5 \"Generic\" -150 0 50 V I C CNN \"Manufacturer\"\n")
    file_lib.write("F6 \""+gr_val+"\" -150 0 50 V I C CNN \"Man Part No\"\n")
    file_lib.write("DRAW\n")
    file_lib.write("S -40 -100 40 100 0 1 10 N\n")
    file_lib.write("X ~ 1 0 150 50 D 50 50 1 1 P\n")
    file_lib.write("X ~ 2 0 -150 50 U 50 50 1 1 P\n")
    file_lib.write("ENDDRAW\n")
    file_lib.write("ENDDEF\n")


def write_headers():
    file_dcm.write("EESchema-DOCLIB  Version 2.0 \n")

    file_lib.write("EESchema-LIBRARY Version 2.4 \n")    


# main program

file_dcm = open("k-lib_resistors_generic.dcm", "w")
file_lib = open("k-lib_resistors_generic.lib", "w")

write_headers()


for pack in package:
    for mag in magnitude:
        for x in E24:
            y=x/10          #1 to 9.1

            if (x == 10) or (x == 20) or (x == 30 ):
                y = int(y)
            value=str(y)+mag
            write_component(value,pack)

        for x in E24:
            y=x             # 10 to 91              
            if mag != "M":  # Megs only to 9.1  - don't generate if M                
                value=str(y)+mag
                write_component(value,pack)

        for x in E24:
            y=x*10          # 100 to 910           
            if mag != "M":  # Megs only to 9.1  - don't generate if M
                value=str(y)+mag
                write_component(value,pack)


file_dcm.close()
file_lib.close()