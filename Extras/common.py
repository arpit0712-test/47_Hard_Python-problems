import subprocess


def command_executes(cmd):
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out.decode(encoding='utf-8'), err.decode(encoding='utf-8')
