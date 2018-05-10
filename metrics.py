#!/usr/bin/python

import argparse
import psutil


class System:

    @staticmethod
    def cpu_times():
        cpu_times = psutil.cpu_times()
        form = ' %.1f'
        cpu_str = 'system.cpu.'
        print(cpu_str + 'idle' + form % cpu_times.idle)
        print(cpu_str + 'user' + form % cpu_times.user)
        print(cpu_str + 'guest' + form % cpu_times.guest)
        print(cpu_str + 'iowait' + form % cpu_times.iowait)
        print(cpu_str + 'stolen' + form % cpu_times.stolen)
        print(cpu_str + 'system' + form % cpu_times.system)

    @staticmethod
    def virtual_mem():
        mem = psutil.virtual_memory()
        total_str = 'total'
        used_str = 'used'
        free_str = 'free'
        mem_str = 'virtual'
        print(mem_str, total_str, mem.total)
        print(mem_str, used_str, mem.used)
        print(mem_str, free_str, mem.free)
        print(mem_str, 'shared', mem.shared)

        swap = psutil.swap_memory()
        swap_str = 'swap'
        print(swap_str, total_str, swap.total)
        print(swap_str, used_str, swap.used)
        print(swap_str, free_str, swap.free)


parser = argparse.ArgumentParser(description='CPU and RAM metrics')
parser.add_argument('metrics', help='Place \'cpu\' or \'mem\' parameter')

args = parser.parse_args()
if args.metrics == 'cpu':
    System.cpu_times()
elif args.metrics == 'mem':
    System.virtual_mem()
