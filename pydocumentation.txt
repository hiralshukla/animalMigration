# import pandas as pd
# import plotly_express as px
#
# import folium
# from folium.plugins import HeatMap

import webbrowser
import ctypes
import html
import time
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def maximize_console_window():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        ctypes.windll.user32.ShowWindow(hwnd, 3)  # 3 = SW_MAXIMIZE


def generate_html_from_multiple_txt(txt_files, output_html):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Code Documentation</title>
        <style>
            body {
                font-family: monospace;
                line-height: 1.5;
                background-color: #f4f4f4;
                margin: 20px;
            }
            pre {
                background: #222;
                color: #f8f8f2;
                padding: 15px;
                border-radius: 5px;
                overflow: auto;
                margin-bottom: 20px;
            }
            h2 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Code Documentation</h1>
    """

    for txt_file in txt_files:
        file_name = os.path.basename(txt_file)
        try:
            with open(txt_file, "r", encoding="utf-8") as file:
                raw_content = file.read()
                escaped_content = html.escape(raw_content)  # Escape special characters
            html_content += f"<h2>{file_name}</h2><pre>{escaped_content}</pre>"
        except Exception as e:
            html_content += f"<h2>{file_name} (Error Loading File)</h2><pre>{str(e)}</pre>"

    html_content += """
    </body>
    </html>
    """

    with open(output_html, "w", encoding="utf-8") as file:
        file.write(html_content)

    os.system(f"start {output_html}")  # Open in the default browser


# Call this function at the beginning of script
maximize_console_window()


# ascii art attribution: https://www.asciiart.eu/text-to-ascii-art
# additional attribution: https://onlinetools.com/ascii/convert-text-to-ascii-art
def main():
    clear_screen()
    # print(f'\033[1;1HWelcome to the Federal Aviation Administration Migratory Bird Visualizer')
    print('''\033[1;1H o      o        8                                  o             o  8
\033[2;1H 8      8        8                                  8             8  8
\033[3;1H 8      8 .oPYo. 8 .oPYo. .oPYo. ooYoYo. .oPYo.    o8P .oPYo.    o8P 8oPYo. .oPYo.
\033[4;1H 8  db  8 8oooo8 8 8    ' 8    8 8' 8  8 8oooo8     8  8    8     8  8    8 8oooo8
\033[5;1H `b.PY.d' 8.     8 8    . 8    8 8  8  8 8.         8  8    8     8  8    8 8.
\033[6;1H  `8  8'  `Yooo' 8 `YooP' `YooP' 8  8  8 `Yooo'     8  `YooP'     8  8    8 `Yooo'
\033[7;1H
\033[8;1H
\033[9;1H  ooooo             8                     8        .oo         o          o   o
\033[10;1H  8                 8                     8       .P 8                    8
\033[11;1H o8oo   .oPYo. .oPYo8 .oPYo. oPYo. .oPYo. 8      .P  8 o    o o8 .oPYo.  o8P o8 .oPYo. odYo.
\033[12;1H  8     8oooo8 8    8 8oooo8 8  `' .oooo8 8     oPooo8 Y.  .P  8 .oooo8   8   8 8    8 8' `8
\033[13;1H  8     8.     8    8 8.     8     8    8 8    .P    8 `b..d'  8 8    8   8   8 8    8 8   8
\033[14;1H  8     `Yooo' `YooP' `Yooo' 8     `YooP8 8   .P     8  `YP'   8 `YooP8   8   8 `YooP' 8   8
\033[15;1H
\033[16;1H
\033[17;1H      .oo      8          o        o          o                 o   o
\033[18;1H     .P 8      8                              8                 8
\033[19;1H    .P  8 .oPYo8 ooYoYo. o8 odYo. o8 .oPYo.  o8P oPYo. .oPYo.  o8P o8 .oPYo. odYo.
\033[20;1H   oPooo8 8    8 8' 8  8  8 8' `8  8 Yb..     8  8  `' .oooo8   8   8 8    8 8' `8
\033[21;1H  .P    8 8    8 8  8  8  8 8   8  8   'Yb.   8  8     8    8   8   8 8    8 8   8
\033[22;1H .P     8 `YooP' 8  8  8  8 8   8  8 `YooP'   8  8     `YooP8   8   8 `YooP' 8   8
\033[23;1H
\033[24;1H o     o  o                       o                         .oPYo.  o            8
\033[25;1H 8b   d8                          8                         8   `8               8
\033[26;1H 8`b d'8 o8 .oPYo. oPYo. .oPYo.  o8P .oPYo. oPYo. o    o   o8YooP' o8 oPYo. .oPYo8
\033[27;1H 8 `o' 8  8 8    8 8  `' .oooo8   8  8    8 8  `' 8    8    8   `b  8 8  `' 8    8
\033[28;1H 8     8  8 8    8 8     8    8   8  8    8 8     8    8    8    8  8 8     8    8
\033[29;1H 8     8  8 `YooP8 8     `YooP8   8  `YooP' 8     `YooP8    8oooP'  8 8     `YooP'
\033[30;1H                 8                                    .8
\033[31;1H              ooP'                                  ooP'.
\033[32;1H o     o  o                      8  o
\033[33;1H 8     8                         8
\033[34;1H 8     8 o8 .oPYo. o    o .oPYo. 8 o8 .oooo. .oPYo. oPYo.
\033[35;1H `b   d'  8 Yb..   8    8 .oooo8 8  8   .dP  8oooo8 8  `'
\033[36;1H  `b d'   8   'Yb. 8    8 8    8 8  8  oP'   8.     8
\033[37;1H   `8'    8 `YooP' `YooP' `YooP8 8  8 `Yooo' `Yooo' 8
''')

    print('''\033[1;97H            .:----:.
\033[2;97H         -+++++++*###=
\033[3;97H       -++==-==++*##++.
\033[4;97H     :+*++===●====+*-...
\033[5;97H    .*++++====++*****++.
\033[6;97H    .**+++++++*#%%#*+#*
\033[7;97H    -*++++====+#%#   :
\033[8;97H    +*+++===----=-
\033[9;97H    =++++++++====-
\033[10;97H   :+**+++*+=======+.
\033[11;97H  .+=+++++====+++=====.
\033[12;97H  =+===++++++++=+*==++=:
\033[13;97H -#*==---=====+==#+*+++=:
\033[14;97H *##*+========----*:**++=:
\033[15;97H .*##*+**+++=====-=**:#*++=:
\033[16;97H .+%###*****+===---=#*=#++=-.
\033[17;97H +#%###*****+=:-----##*+++=-
\033[18;97H +#%#*****++==-----===##+=--.
\033[19;97H :*%%********+==+==-++=#*++=:     -*
\033[20;97H  *#####***##*++++==++-=**++=.   =%*
\033[21;97H   ###**##**##*+++++##+=--+*=-:=+.
\033[22;97H    =%*###########**##+-::-+++*-
\033[23;97H     .############*####=::-=**=.
\033[24;97H       -*#######%###*-:-=*%#%%#-
\033[25;97H         +**##########=*@%+-=%%=
\033[26;97H         .++***++***%@#%%#*=-+%*.
\033[27;97H        .:-==+*##%%%%%%%%##*=-+#.
\033[28;97H       -==+%%@++%%%%@%@@@%%*==-+:
\033[29;97H       -%**-..   :##%%%@@@@%*+==.
\033[30;97H         .         .+#%%%%%%#*++-
\033[31;97H                     :%%%##%%##**-
\033[32;97H                       +%####***##=
\033[33;97H                        #%#******##-
\033[34;97H                        .%%#*****##*-
\033[35;97H                         :####*###***-
\033[36;97H                          -##*+=*##***:
\033[37;97H                           =**+=+*##**+
\033[38;97H                            =**++*****+:
\033[39;97H                             -+*++***+:  ''')

    print("\033[11;140H\033[1;4;36m=== Map Selection by Record ID ===\033[0m")
    print("\033[12;140H \t1: 608242-617791")
    print("\033[13;140H \t2: 617792-627341")
    print("\033[14;140H \t3: 627342-636891")
    print("\033[15;140H \t4: 636892-646441")
    print("\033[16;140H \t5: 646442-655991")
    print("\033[17;140H \t6: 655992-665541")
    print("\033[18;140H \t7: 665542-675091")
    print("\033[19;140H \t8: 675092-684641")
    print("\033[20;140H \t9: 684642-694191")
    print("\033[21;140H \t10:  694192-703741")
    print("\033[22;140H \t11:  703742-718915")
    print("\033[23;140H \t12:  608242-617241")

    print("\033[2;135H\033[1;4;33m*** How to Use the Visualizer ***\033[0m")
    print("\033[3;135H \t exit: end program")
    print("\033[3;135H \t docs: shows faa documentation")
    print("\033[4;135H \t faa: FAA website")
    print("\033[5;135H \t profHVZ: get to know Dr. Hannah Vander Zanden")
    print("\033[6;135H \t pydocs: shows python documentation")
    print("\033[7;135H \t animalMigration: thank you message")
    print("\033[8;135H \t hiral: get to know me!")
    print("\033[9;135H \t 1-12: displays heatmap/visualization")

    print("\033[27;145H\033[1;4;95m--- About the Visualizer ---\033[0m")
    print("\033[28;140H   This visualizer prototype uses Python")
    print("\033[29;140H to create heatmaps!")
    print("\033[30;140H   Maps 1-11 are all 9000 data points each,")
    print("\033[31;140H to ensure it is less memory intensive.")
    print("\033[32;140H   Each contains data from 1990 - 2011.")
    print("\033[33;140H   The FAA organizes their datasets using IDs")
    print("\033[34;140H per incident, which also have been used here!")
    print("\033[35;140H   Map 12 contains 45000+ data points")
    print("\033[36;140H mapping the lat. & long. of bird strikes.")
    print("\033[37;140H   I hope this project encourages")
    print("\033[38;140H avian conservation & research <3!")

    print('''\033[35;55H         _,--',   _._.--._____
\033[36;55H  .--.--';_'-.', ";_      _.,-'
\033[37;55H .'--'.  _.'    {`'-;_ .-.>.'
\033[38;55H       '-:_      )  / `' '=.
\033[39;55H         ) >     {_/,     /~)
\033[40;55H         |/               `^ .''')

    while True:
        count = 0
        choice = input('\033[25;140H\033[1;4;32m>>> Enter a selection:\033[0m ')

        if choice == "exit":
            clear_screen()
            print("\a")
            break

        if choice == "docs":
            file_path = r"C:/Users/singu/Downloads/NWSD/fieldlist.pdf"
            file_path = os.path.abspath(file_path)
            webbrowser.open('file:///' + file_path)
            print("\033[25;140H" + " " * 40)
            print("\a")

        if choice == "profHVZ":
            file_path = r"https://people.clas.ufl.edu/hvz/people/"
            webbrowser.open(file_path)
            print("\033[25;140H" + " " * 40)
            print("\a")

        if choice == "faa":
            file_path = r"https://wildlife.faa.gov/home"
            webbrowser.open(file_path)
            print("\033[25;140H" + " " * 40)
            print("\a")

        if choice == "animalMigration":
            count += 1
            if count == 1:
                print("\033[36;87HThank you to my classmates")
                print("\033[37;85H       of Fall 2024 Animal Migration")
                print("\033[38;85H       and to Professor Vander Zanden")
                print("\033[39;85H          for an inspiring semester.")
                print("\033[40;85H                     ~ Hiral Shukla")
            print("\033[25;140H" + " " * 40)
            print("\a")

        if choice == "hiral":
            file_path = (r"https://docs.google.com/document/d/"
                         r"1xEl3T2zJyEhXkI6hE5laduhFugNRIlN-mSVoM34J3gs/edit?usp=sharing")
            webbrowser.open(file_path)
            print("\033[25;140H" + " " * 40)
            print("\a")

        if choice == "pydocs":
            txt_files = [
                r"C:\Users\singu\PycharmProjects\animalMigration\pydocumentation.txt",
                r"C:\Users\singu\PycharmProjects\animalMigration\map_generator_11.txt"
            ]
            output_html = "documentation.html"
            generate_html_from_multiple_txt(txt_files, output_html)
            print("\033[25;140H" + " " * 40)
            print("\a")

        if choice.isdigit():
            if int(choice) == 12:
                file_path = r"C:\Users\singu\Downloads\NWSD\combined_heatmap_with_bird_info.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 11:
                file_path = r"C:\Users\singu\Downloads\NWSD\final11.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 10:
                file_path = r"C:\Users\singu\Downloads\NWSD\final10.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 9:
                file_path = r"C:\Users\singu\Downloads\NWSD\final9.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 8:
                file_path = r"C:\Users\singu\Downloads\NWSD\final8.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 7:
                file_path = r"C:\Users\singu\Downloads\NWSD\final7.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 6:
                file_path = r"C:\Users\singu\Downloads\NWSD\final6.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 5:
                file_path = r"C:\Users\singu\Downloads\NWSD\final5.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 4:
                file_path = r"C:\Users\singu\Downloads\NWSD\final4.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 3:
                file_path = r"C:\Users\singu\Downloads\NWSD\final3.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 2:
                file_path = r"C:\Users\singu\Downloads\NWSD\final2.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")

            if int(choice) == 1:
                file_path = r"C:\Users\singu\Downloads\NWSD\final1.html"
                file_path = os.path.abspath(file_path)
                webbrowser.open('file://' + file_path)
                print("\033[25;140H" + " " * 40)
                print("\a")


if __name__ == "__main__":
    main()
