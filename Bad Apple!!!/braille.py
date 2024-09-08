import cv2

def image_to_braille(frame, size):
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    small_grey_frame = cv2.resize(grey_frame, size)
    _, binary_frame = cv2.threshold(small_grey_frame, 127, 255, cv2.THRESH_BINARY)
    return binary_image_to_braille(binary_frame, size)

def binary_image_to_braille(image, size):
    string = '⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿'
    num = ''
    output = ''

    if size[0] % 3 != 2 or size[1] % 6 != 4:
        raise ValueError('Invalid size!')

    for y in range(0, size[1], 6):
        for x in range(0, size[0], 3):

            for j in range(y,y+3):
                for i in range(x,x+2):
                    if image[j][i] == 0:
                        num = '0' + num
                    elif image[j][i] == 255:
                        num = '1' + num
                    else:
                        raise ValueError('Invalid image!')
            
            for i in range(x,x+2):
                if image[y+3][i] == 0:
                    num = '0' + num
                elif image[y+3][i] == 255:
                    num = '1' + num
                else:
                    raise ValueError('Invalid image!')

            output += string[int(num, 2)]
            num = ''
        output += '\n'
    return output[:-1]
