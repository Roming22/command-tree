#!/usr/local/bin/python

'''
Main program
'''


import os
import sys

import utils.plugin_manager as plugin_manager


def parse_args(plugins):
    '''
    Create the base argparser
    '''
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate ACS delivrables from ULAM delivrables.')

    # Main program options
    parser.add_argument('-c', '--config_dir', nargs='?', dest='config_dir',
                        help='path to the directory holding the configuration')

    subparsers = parser.add_subparsers(dest='command1')
    plugin_manager.get_argparser(subparsers, plugins)

    # Parse command line
    return vars(parser.parse_args(sys.argv[1:]))


def run():
    '''
    main function
    '''

    print __name__, 'Hello'

    context = {}

    # Load plugins
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    plugins = plugin_manager.load_for(os.path.abspath(__file__))
    context["plugins"] = plugins

    # Parse args
    context['args'] = parse_args(plugins)

    # Setup plugins
    plugin_list = []
    level = 1
    while 'command' + str(level) in context['args']:
        command = 'command' + str(level)
        plugin = plugins[context['args'][command]]
        plugin_list.append(plugin)
        plugins = plugin.plugins
        level += 1

    for plugin in plugin_list:
        context = plugin.pre(context)

    # Run the bottom plugin
    plugin = plugin_list.pop()
    context = plugin.run(context)

    # Teardown the plugins in reverse order
    context = plugin.post(context)
    while plugin_list:
        plugin = plugin_list.pop()
        context = plugin.post(context)
    print __name__, 'Bye'


if __name__ == '__main__':
    run()
