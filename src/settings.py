import logging
from enum import Enum
import os


class CalcType(Enum):
    SingleThread = 0
    MultiThread = 1
    MultiProcess = 2
    Coroutine = 3


# 日志类型
logging_level = logging.INFO
# 日志格式
logging_format = '%(asctime)s - %(levelname)s - %(processName)s/%(threadName)s - %(message)s'

# 默认的请求类型
default_calc_type = CalcType.SingleThread

# 下载数量
download_count = 50

# 存储路径
storage_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

# 线程或进程数
multi_count = 8

images = ['https://img0.baidu.com/it/u=1110451881,249059187&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=487427121,2419154511&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=494894085,752224283&fm=253&fmt=auto&app=138&f=JPEG?w=684&h=684',
          'https://img2.baidu.com/it/u=298337870,1549143155&fm=253&fmt=auto&app=138&f=JPEG?w=380&h=380',
          'https://img2.baidu.com/it/u=4180632206,4252311125&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img0.baidu.com/it/u=3483452876,1221895514&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=667',
          'https://img0.baidu.com/it/u=1825101012,2392413104&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=666',
          'https://img1.baidu.com/it/u=3150642553,1721766004&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=688056095,2661831008&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400',
          'https://img0.baidu.com/it/u=931420816,2003024850&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=4014618819,3497659980&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400',
          'https://img1.baidu.com/it/u=2218944448,3064005596&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img1.baidu.com/it/u=3167882900,2160713771&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=2394299961,2127399828&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img0.baidu.com/it/u=579910585,4042610108&fm=253&fmt=auto&app=138&f=JPEG?w=667&h=500',
          'https://img1.baidu.com/it/u=2304365426,2266291318&fm=253&fmt=auto&app=120&f=JPEG?w=640&h=637',
          'https://img0.baidu.com/it/u=337684678,565504341&fm=253&fmt=auto&app=138&f=JPEG?w=512&h=500',
          'https://img2.baidu.com/it/u=1356301676,259883368&fm=253&fmt=auto&app=138&f=JPEG?w=511&h=500',
          'https://img0.baidu.com/it/u=2065011677,2033132951&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=3266392871,597935839&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=1976773655,297553467&fm=253&fmt=auto&app=120&f=JPEG?w=240&h=240',
          'https://img1.baidu.com/it/u=4133777788,644860169&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=2996316162,4163558640&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img0.baidu.com/it/u=1302468710,3819881832&fm=253&fmt=auto&app=138&f=JPEG?w=360&h=360',
          'https://img1.baidu.com/it/u=2971123675,3744361194&fm=253&fmt=auto&app=120&f=JPEG?w=439&h=439',
          'https://img2.baidu.com/it/u=1659423051,358624857&fm=253&fmt=auto&app=138&f=JPEG?w=200&h=200',
          'https://img2.baidu.com/it/u=3758538069,3190220697&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img1.baidu.com/it/u=3153728337,1731756480&fm=253&fmt=auto&app=138&f=JPEG?w=313&h=313',
          'https://img0.baidu.com/it/u=760525230,183424185&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=1806845053,2339269437&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img0.baidu.com/it/u=1214064415,2597776514&fm=253&fmt=auto&app=138&f=JPEG?w=450&h=450',
          'https://img2.baidu.com/it/u=3093342629,654514380&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img1.baidu.com/it/u=196795814,3626945670&fm=253&fmt=auto&app=138&f=PNG?w=400&h=400',
          'https://img2.baidu.com/it/u=1438665237,3228344235&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img1.baidu.com/it/u=2371671630,615792089&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400',
          'https://img1.baidu.com/it/u=3007043777,248367526&fm=253&fmt=auto&app=138&f=JPEG?w=360&h=360',
          'https://img1.baidu.com/it/u=3804797672,2729674533&fm=253&fmt=auto&app=138&f=JPEG?w=502&h=500',
          'https://img0.baidu.com/it/u=2464399262,3969891995&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400',
          'https://img0.baidu.com/it/u=799930638,2690447852&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=2681028238,3016244527&fm=253&fmt=auto&app=138&f=JPEG?w=440&h=440',
          'https://img2.baidu.com/it/u=1170729866,396501516&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img1.baidu.com/it/u=2433947497,1997019056&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=579690441,1646331460&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img1.baidu.com/it/u=3505678876,545666397&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=2344451272,2206293105&fm=253&fmt=auto&app=138&f=JPEG?w=821&h=800',
          'https://img1.baidu.com/it/u=3934696941,4210439264&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=496',
          'https://img0.baidu.com/it/u=2468474661,3923176274&fm=253&fmt=auto&app=138&f=JPEG?w=517&h=500',
          'https://img2.baidu.com/it/u=2627439259,1948620750&fm=253&fmt=auto&app=138&f=JPEG?w=380&h=380',
          'https://img1.baidu.com/it/u=3695690513,3065315233&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img0.baidu.com/it/u=3992066725,2379971241&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=501',
          'https://img0.baidu.com/it/u=2226630510,461838410&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=521',
          'https://img1.baidu.com/it/u=1770129246,4226131342&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img1.baidu.com/it/u=1759945042,4290767561&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',
          'https://img2.baidu.com/it/u=1852078667,1285597720&fm=253&fmt=auto&app=138&f=JPEG?w=360&h=360',
          'https://img2.baidu.com/it/u=1386922620,2177741996&fm=253&fmt=auto&app=138&f=JPEG?w=400&h=400',
          'https://img0.baidu.com/it/u=687811600,3166843387&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=499',
          'https://img0.baidu.com/it/u=2777880357,1216908469&fm=253&fmt=auto&app=138&f=JPEG?w=300&h=300',
          'https://img0.baidu.com/it/u=767636438,1982452134&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=628',
          'https://img1.baidu.com/it/u=2205111871,634694943&fm=253&fmt=auto&app=138&f=JPEG?w=684&h=684',
          'https://img0.baidu.com/it/u=1835287934,275488642&fm=253&fmt=auto?w=690&h=461'
          ]
