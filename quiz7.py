for i in range(1,51):
    with open("{0}주차.txt".format(i),"w",encoding = "utf8") as file:
        file.write("- {0} 주차 주간 보고 -".format(i))
        file.write("\n부서 : ")
        file.write("\n이름 : ")
        file.write("\n업무 요약 : ")