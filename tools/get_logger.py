# 导包
import logging.handlers

# 定义类
import os

from config import BASE_PATH


class GetLogger:
    # 定义日志器变量
    __logger = None

    # 获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器为空：
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 设置日志器默认级别
            cls.__logger.setLevel(logging.INFO)
            file_path = BASE_PATH + os.sep + 'log' + os.sep + 'hmtt.log'
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=file_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger


if __name__ == '__main__':
    log = GetLogger.get_logger()
    log.info('info级别测试')
    log.error('error级别测试')