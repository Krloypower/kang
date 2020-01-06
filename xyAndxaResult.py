if __name__ == '__main__':

    xiaoya = open("/Users/xmly/Desktop/xiaoya_num3_result.txt")
    result = ''
    while True:
        readline = xiaoya.readline()
        if not readline:
            break
            pass
        result = result + readline[:-2]
        xiaoai = open("/Users/xmly/Desktop/xiaoai_num3_result.txt")
        while True:
            xiaoai_readline = xiaoai.readline()
            if not readline:
                break
                pass
            split = xiaoai_readline.split("\t")
            split_ = split[0]
            if split_ in readline:
                result = result + xiaoai_readline.replace(split_, "|")
                break
        print(result)
    f = open("/Users/xmly/Desktop/xiaoai_and_xiaoya_num3_result.txt", 'w')
    f.write(result)
    f.close()

