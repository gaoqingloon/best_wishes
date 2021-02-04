# coding: utf-8

# ### 1 读文件并完成解析
import gpxpy.parser as parser

file_name = "跑步20210131154035.gpx"


with open('./' + file_name, 'r', encoding="utf-8") as fr:
    with open("./r_" + file_name, 'w', encoding="utf-8") as fw:
        for line in fr:
            line = line.replace("<metadata>", "").replace("</metadata>", "").replace("type", "desc")
            fw.write(line)

gpx_file = open("./r_" + file_name, 'r', encoding="utf-8")
gpx_parser = parser.GPXParser(gpx_file)
gpx = gpx_parser.parse()  # 文件解析
gpx_file.close()


"""
<metadata>
</metadata>
type -> desc

"""
# ### 2 读文件并完成解析
print('======================')
print(gpx.time)
print('======================')

# ### 3 打印解析的轨迹数据
for track in gpx.tracks:
    i = 0
    print(track.name)
    print(track.description)

    for segment in track.segments:
        for point in segment.points:
            print(str(point.latitude) + ", " +
                  str(point.longitude) + ", " +
                  str(point.time) + ", " + str(point.elevation))

            for ele in point.extensions:
                print(ele)
            i += 1
            if i == 3:
                break

# ### 6 其他方法
# print("*" * 50)
# print('GPX:', gpx.to_xml())


