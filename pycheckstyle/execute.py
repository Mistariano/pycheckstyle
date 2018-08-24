import subprocess

__java = "java"
__jar_file = "/usr/lib/checkstyle/checkstyle.jar"
__command_line_base = [__java, "-jar", __jar_file]


def execute(*args):
    """
    底层执行接口
    当返回值非零的时候将抛出异常
    :param args: 命令行参数
    :return: 标准输出信息
    """
    command_line_args = __command_line_base + list(args)
    program = subprocess.Popen(command_line_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = program.communicate()
    return out.decode(), err.decode()
