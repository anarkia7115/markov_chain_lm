#!/usr/bin/env python
import logger
import os

def exec_cmd(cmd: str):
    logger.info("executing command: [%s]" % cmd)
    os.system(cmd)

def main(args):
    action = "run_" + args[0]
    if is_func(action):
        globals()[action]()
    else:
        print("%s not in actions" % action[4:])
        actions = ", ".join(list_all_run_func())
        logger.info("please choose an action from [{}]".format(actions))

def is_func(func_name: str):
    return func_name in globals() and callable(globals()[func_name])

def list_all_run_func():
    # logger.info("checking items: " + globals().__str__())
    for key, value in globals().items():
        if key.startswith("run_") and \
                callable(value) and \
                value.__module__ == __name__:

            yield key[4:]

import data_utils
from analyzer import text_generator

def run_markov_o1():
    title_text = data_utils.get_title_text()
    generated_text = text_generator.markov_o1(title_text, 100)
    print(generated_text)

if __name__ == "__main__":

    import sys
    args = sys.argv[1:]

    main(args)