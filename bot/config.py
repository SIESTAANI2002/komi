#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default=15681388, cast=int)
    API_HASH = config("API_HASH", default="446b56944f74f6b7688175d48cdfa881")
    BOT_TOKEN = "6249960795:AAHBC233MxzMDnrtTiBP8FcmfltympbBpiE"
    DEV = 5074446156
    OWNER = config("OWNER", default="5074446156")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -map 0:v? -map 0:a? -map 0:s? -c:v libx265 -pix_fmt yuv420p10le -preset medium -s 1920:1080 -crf 21.2 -x265-params frame-threads=4:bframes=8:psy-rd=1:aq-mode=3:aq-strength=0.8:deblock=1,1 -c:a aac -b:a 128k -c:s copy -metadata title="Presented By Ani Animesh | Anime Sakura" -metadata author="AnimeSakura.co" -metadata copyright="Copyright 2023 Me" -metadata encoded_by="Lolikiller #Sakura_Gang" -metadata:s:0 title="Episode Unknown xD" -metadata:s:a:0 title="Ani Animesh" -metadata:s:a:1 title="AnimeSakura.co" -metadata:s:s:0 title="AnimeSakura.co" -metadata:s:s:1 title="@Ani_Animesh" "{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/a615291ef3f9f361e9b12.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
