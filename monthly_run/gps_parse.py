# coding: utf-8

import gpxpy.parser as parser

file_name = "跑步20210131154035.gpx"

# with open('./' + file_name, 'r', encoding="utf-8") as fr:
#     with open("./r_" + file_name, 'w', encoding="utf-8") as fw:
#         for line in fr:
#             line = line \
#                 .replace("<metadata>", "") \
#                 .replace("</metadata>", "") \
#                 .replace("<extensions>", "") \
#                 .replace("</extensions>", "") \
#                 .replace("type", "desc").replace("heartrate", "magvar").replace("distance", "geoidheight")
#             fw.write(line)

gpx_file = open("./r_" + file_name, 'r', encoding="utf-8")
gpx_parser = parser.GPXParser(gpx_file)
gpx = gpx_parser.parse()  # 文件解析
gpx_file.close()

"""
<metadata>
</metadata>
type -> desc

"""
print('======================')
print(gpx.time)

# 打印解析的轨迹数据
for track in gpx.tracks:
    i = 0
    print(track.name)
    print(track.description)
    print('======================')

    for segment in track.segments:
        for point in segment.points:
            time = point.time
            latitude = point.latitude
            longitude = point.longitude
            heart_rate = point.magnetic_variation
            distance = point.geoid_height
            elevation = point.elevation
            print(str(time) + "," +
                  str(latitude) + "," +
                  str(longitude) + "," +
                  str(heart_rate) + "," +
                  str(distance) + "," +
                  str(elevation))

            # i += 1
            # if i == 300:
            #     break

